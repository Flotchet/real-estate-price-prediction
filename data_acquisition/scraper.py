#-I-QOF-----------------------------------------------------------------------------------------
import itertools 
#-I-OS------------------------------------------------------------------------------------------
import time
import os
import psutil
import warnings
import gc
from tqdm import tqdm
#-I-REGEX---------------------------------------------------------------------------------------
import re
#-I-PERF----------------------------------------------------------------------------------------
from multiprocessing import Pool
#-I-DS------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
#-I-WEB-----------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver
#-I-txt-----------------------------------------------------------------------------------------
from unidecode import unidecode
#-----------------------------------------------------------------------------------------------

#-01-S------------------------------------------------------------------------------------------

def url_cleaner(hrefs : list[str]):
    """Clean the urls. by removing urls that not 
    start with 'https://www.immoweb.be/fr/annonce/'.

    Parameters
    ----------
    hrefs : table[str]
        The urls of the houses.

    Returns
    -------
    table[str]
        The cleaned urls of the houses.

    Raises
    ------
    Exception
        If the url is not a list of strings.
    """

    if not isinstance(hrefs, list):
        raise Exception("The hrefs is not a list of strings.")

    return [href for href in hrefs if href.startswith("https://www.immoweb.be/fr/annonce/")]

#-01-T------------------------------------------------------------------------------------------

def scrape_html_href_with_selenium(url : list[str] or str) -> list[str]:
    """Scrape the html of the page with selenium.

    Parameters
    ----------
    urls : list[str] or str
        The urls of the page.

    Returns
    -------
    list[str]
        The href of the pages.

    Raises
    ------
    Exception
        If the url is not a string or a list of strings.
    """

    if isinstance(url, str):

        driver = webdriver.Firefox()

        driver.get(url)
        html = driver.page_source

        driver.quit()
        driver.close()

        soup = BeautifulSoup(html, "html.parser")

        return [a["href"] for a in soup.find_all("a", {"class": "card__title-link"})]

    elif isinstance(url, list):

        driver = webdriver.Firefox()
        #clear the cache of the driver
        #open the driver and set it up
        driver = webdriver.Firefox()
        driver.set_window_size(1080, 3840)
        driver.set_window_position(0, 0)
        driver.set_page_load_timeout(30)
        driver.set_script_timeout(30)
        driver.implicitly_wait(30)

        htmls = []

        for u in url:

            driver.get(u)
            html = driver.page_source

            soup = BeautifulSoup(html, "html.parser")

            htmls.append([a["href"] for a in soup.find_all("a", {"class": "card__title-link"})])


        driver.quit()
        driver.close()

        return htmls

    else:

        raise Exception("The url is not a string or a list of strings.")

#-01-S------------------------------------------------------------------------------------------

def multi_process_scrape_html_href_with_selenium(urls : list[str],
                                                 n_process : int = 4
                                                 ) -> list[str]:
    """Scrape the html of the pages with selenium.

    Parameters
    ----------
    urls : list[str]
        The urls of the pages.

    Returns
    -------
    list[str]
        The html of the pages.
    """
    
    #Divide the work with numpy as a list of list of urls
    urls = np.array_split(urls, n_process)
    #transform nparray to list
    urls = [url.tolist() for url in urls]

    #Create the pool of workers
    with Pool(n_process) as pool:
        return pool.map(scrape_html_href_with_selenium, urls)

#-01-S------------------------------------------------------------------------------------------

def immoweb_url_constructor(n : int = 333) -> list[str]:
    """Construct the urls of the immoweb pages.

    Parameters
    ----------
    n : int
        The number of pages to scrape.
        per province and selling type

    Returns
    -------
    list[str]
        The urls of the immoweb pages.
    """
    belgian_provinces = ["anvers", 
                        "limbourg", 
                        "flandre-orientale", 
                        "brabant-flamand", 
                        "flandre-occidentale", 
                        "brabant-wallon", 
                        "hainaut", 
                        "liege", 
                        "luxembourg", 
                        "namur"]

    selling = ["louer", "vendre"]
    page_number = range(1,n+1)
    urls = [f"https://www.immoweb.be/fr/recherche/maison-et-appartement/a-{sell}/{province}/province?countries=BE&page={page}&orderBy=relevance" 
    for sell, province, page in itertools.product(selling, belgian_provinces, page_number)]

    return urls

#-01-P-------------------------------------------------------------------------------------------

def immoweb_url_scraper() -> None:
    """Scrape the urls of the houses from immoweb.
    """
    
    urls = immoweb_url_constructor()
    urls = multi_process_scrape_html_href_with_selenium(urls, 16)
    
    #transform the list of list of str to list of str
    urls = list(itertools.chain.from_iterable(urls))
    #Flatten the list of list into a list
    urls = [item for sublist in urls for item in sublist]
    urls = url_cleaner(urls)
    #Remove duplicates 
    urls = list(dict.fromkeys(urls))
    #save the list as a csv
    pd.DataFrame(urls).to_csv("urls.csv", index = False)

#-02-S------------------------------------------------------------------------------------------

def scrape_html_with_selenium_with_save(urls : list[str] or str, 
                                        folder_path : str = "./raw_html", 
                                        time_stamp : bool = False,
                                        headless : bool = False,
                                        cache : bool = False,
                                        css : bool = False
                                        ) -> int:
    """Scrape the html of the page with selenium.
    and saves each file to a folder as name+time_stamp.html

    Parameters
    ----------
    urls : list[str] or str
        The urls of the page.

    folder_path : str = "./raw_html"
        The path to the folder where the files will be stored

    time_stamp : bool = True
        make a time stamp to each file

    headless : bool = False
        If the browser is headless

    cache : bool = False
        If the cache is cleared

    css : bool = False
        If the css is loaded


    Returns
    -------
    int
        The number of files saved

    Raises
    ------
    Exception
        If the urls is not a string or a list of strings.

    Exception
        If the folder_path is not a string.

    Exception
        If the time_stamp is not a boolean.
    
    Exception
        If the folder_path does not exist.

    Exception
        If the folder_path is not a folder.
    
    Exception
        If the folder_path is not writable.

    Exception
        If the headless is not a boolean.

    Exception
        If the cache is not a boolean.

    Exception
        If the css is not a boolean.

    Warning
        If the folder_path is not empty.

    Warning
        If the memory usage is too high
    """

    #check if the url is a string or a list of strings
    if not isinstance(urls, str) and not isinstance(urls, list):
        raise Exception("The url is not a string or a list of strings.")

    #check if the folder_path is a string
    if not isinstance(folder_path, str):
        raise Exception("The folder_path is not a string.")

    #check if the time_stamp is a boolean
    if not isinstance(time_stamp, bool):
        raise Exception("The time_stamp is not a boolean.")

    #check if the folder_path exists
    if not os.path.exists(folder_path):
        raise Exception("The folder_path does not exist.")

    #check if the folder_path is a folder
    if not os.path.isdir(folder_path):
        raise Exception("The folder_path is not a folder.")

    #check if the folder_path is writable
    if not os.access(folder_path, os.W_OK):
        raise Exception("The folder_path is not writable.")

    #check if the headless is a boolean
    if not isinstance(headless, bool):
        raise Exception("The headless is not a boolean.")

    #check if the cache is a boolean
    if not isinstance(cache, bool):
        raise Exception("The cache is not a boolean.")

    #check if the css is a boolean
    if not isinstance(css, bool):
        raise Exception("The css is not a boolean.")

    #check if the folder_path is empty
    if os.listdir(folder_path):
        warnings.warn("The folder_path is not empty.")

    #check if the url is a string
    if isinstance(urls, str):
        urls = [urls]

    #open the driver and set it up
    driver = webdriver.Firefox()
    driver.set_window_size(1080, 3840)
    driver.set_window_position(0, 0)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.implicitly_wait(30)

    #set the driver to headless for firefox
    if headless:
        driver.set_headless()

    #set css loader for firefox
    if not css:  
        driver.execute_script("document.styleSheets[0].disabled = true;")
    

    for url in urls:
        #check if the file already exists an pass if it's the case
        if time_stamp:
            if os.path.isfile(f"{folder_path}/{url.split('/')[-1]}_{time.time()}.html"):
                continue
        else:
            if os.path.isfile(f"{folder_path}/{url.split('/')[-1]}.html"):
                continue


        driver.get(url)

        if time_stamp:
            with open(f"{folder_path}/{url.split('/')[-1]}_{time.time()}.html", "w") as f:
                f.write(driver.page_source)
        else:
            with open(f"{folder_path}/{url.split('/')[-1]}.html", "w") as f:
                f.write(driver.page_source)

        time.sleep(1)

        #clear the cache for firefox
        if not cache:
            driver.execute_script("window.localStorage.clear();")
            driver.execute_script("window.sessionStorage.clear();")
            # delete the cookies
            driver.delete_all_cookies()
            #delete cache
            driver.execute_script("window.caches.keys().then(function(names) { for (let name of names) caches.delete(name); });")

        #check the percentage of ram used and close everithing if > 90 percent
        #make a warning with a timestamp and process name
        if psutil.virtual_memory().percent > 98:
            warnings.warn(f"WARNING memory usage too high stropping the scraping ... : {time.time()} - {psutil.Process().name()} - {psutil.virtual_memory().percent}")       
            break

        #clear ram cache
        gc.collect()
        
    driver.quit()
    driver.close()

    return len(urls)

#-02-P------------------------------------------------------------------------------------------

def immoweb_page_scraper(csv_name : str = "urls.csv", 
                        folder_path : str = "./raw_html", 
                        time_stamp : bool = False, 
                        tries : int = 10
                        ) -> None:
    """Scrape the pages of the houses from immoweb
    in a memory optimized way and store the files.

    Parameters
    ----------
    csv_name : str = "urls.csv"
        The path to the files that contains url

    folder_path : str = "./raw_html"
        The path to the folder where the files will be stored

    time_stamp : bool = True
        make a time stamp to each file

    tries : int = 10
        The number of tries to scrape the page

    Returns
    -------
    None

    Raises
    ------
    Exception
        If the csv_name is not a string
    Exception
        If the csv_name does not finish by .csv
    """

    #check if the csv_name is a string
    if not isinstance(csv_name, str):
        raise Exception("The csv_name must be a string")

    #check if the filename finish by .csv
    if csv_name[-4:] != ".csv":
        raise Exception("The file name must finish by .csv")

    #read the csv file
    urls = pd.read_csv(csv_name).values.tolist()
    urls = urls

    #Flatten the list of list into a list
    urls = [item for sublist in urls for item in sublist]

    #create a folder to store the html files
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    #This task is IO limited so we can use a lot of process at the same
    #time to speed up the process even if they are more process than the
    #number of cpus

    #Get the number of logical cpus
    multiplier = 2
    n_cpus = os.cpu_count()
    n_process = n_cpus * multiplier

    #Divide the work with numpy as a list of list of urls
    urls = np.array_split(urls, n_process)
    #transform nparray to list
    urls = [url.tolist() for url in urls]

    folder_path = [folder_path]*n_process
    time_stamp = [time_stamp]*n_process

    # if the nuùber of files in folder is different than the number of urls retries n times
    
    while len(os.listdir(folder_path[0])) != len(urls[0]) and tries > 0:
        #Create the pool of workers
        with Pool(n_process) as pool:
            print(pool.starmap(scrape_html_with_selenium_with_save, zip(urls, folder_path, time_stamp)))
        tries -= 1

    #kill all firefox and Web Content process
    os.system("killall firefox")
    os.system("killall Web Content")

    return None

#-03-O------------------------------------------------------------------------------------------
# Apparently error pages also contains info about a house/appartement
def html_errors_excluder(html_folder : str = 
                            "/home/flotchet/server/first_pool/Raw_HTML", 
                         excluded_html_folder : str = 
                            "/home/flotchet/server/first_pool/Raw_HTML_Rejected" 
                        ) -> None:

    """Exclude the html files that have errors.

    Parameters
    ----------
    html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML"
        The path to the folder where the html files are stored

    excluded_html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML_Rejected"
        The path to the folder where the html files with errors will be stored

    Returns
    -------
    None

    Raises
    ------
    Exception
        If the html_folder is not a string
    Exception
        If the excluded_html_folder is not a string
    Warning
        If the html_folder does not exist or is empty

    """

    #check if the html_folder is a string
    if not isinstance(html_folder, str):
        raise Exception("The html_folder must be a string")

    #check if the excluded_html_folder is a string
    if not isinstance(excluded_html_folder, str):
        raise Exception("The excluded_html_folder must be a string")

    #check if the html_folder exist and is not empty
    if not os.path.exists(html_folder) or len(os.listdir(html_folder)) == 0:
        warnings.warn("The html_folder does not exist or is empty")

    #create a folder to store the html files with errors
    if not os.path.exists(excluded_html_folder):
        os.mkdir(excluded_html_folder)

    #get the list of html files
    html_files = os.listdir(html_folder)

    #go throught the files and move the ones that contains error ie files that contains
    #the string "Malheureusement," and the string "404" or "500" to the excluded_html_folder
    # and show a progress bar
    for html_file in tqdm(html_files):
        with open(html_folder + "/" + html_file, "r") as f:
            html = f.read()
        if "Malheureusement," in html and ("404" in html or "500" in html):
            os.system("mv " + html + " " + excluded_html_folder)

    return None
                   
#-03-O------------------------------------------------------------------------------------------
# Apparently error pages also contains info about a house/appartement
def html_a_louer_vendre_excluder(html_folder : str = 
                                    "/home/flotchet/server/first_pool/Raw_HTML", 
                                 a_louer_html_folder : str = 
                                    "/home/flotchet/server/first_pool/Raw_HTML_a_louer", 
                                 a_vendre_html_folder : str =
                                    "/home/flotchet/server/first_pool/Raw_HTML_a_vendre"
                        ) -> None:

    """
    Exclude the html files that have à vendre between two title tags.
    Exclude the html files that have à louer between two title tags.

    Parameters
    ----------
    html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML"
        The path to the folder where the html files are stored

    a_louer_html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML_a_louer"
        The path to the folder where the html files with à louer will be stored

    a_vendre_html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML_a_vendre"
        The path to the folder where the html files with à vendre will be stored

    Returns
    -------
    None

    Raises
    ------
    Exception
        If the html_folder is not a string

    Exception
        If the a_louer_html_folder is not a string

    Exception
        If the a_vendre_html_folder is not a string

    Warning
        If the html_folder does not exist or is empty

    """

    #check if the html_folder is a string
    if not isinstance(html_folder, str):
        raise Exception("The html_folder must be a string")

    #check if the a_louer_html_folder is a string
    if not isinstance(a_louer_html_folder, str):    
        raise Exception("The a_louer_html_folder must be a string")

    #check if the a_vendre_html_folder is a string
    if not isinstance(a_vendre_html_folder, str):
        raise Exception("The a_vendre_html_folder must be a string")

    #check if the html_folder exist and is not empty
    if not os.path.exists(html_folder) or len(os.listdir(html_folder)) == 0:
        warnings.warn("The html_folder does not exist or is empty")

    #create a folder to store the html files with à louer
    if not os.path.exists(a_louer_html_folder):
        os.mkdir(a_louer_html_folder)

    #create a folder to store the html files with à vendre
    if not os.path.exists(a_vendre_html_folder):
        os.mkdir(a_vendre_html_folder)

    #get the list of html files
    html_files = os.listdir(html_folder)


    #find the string between <title> and </title>
    for html_file in tqdm(html_files):
        with open(html_folder + "/" + html_file, "r") as f:
            html = f.read()

        title = html[html.find("<title>") + len("<title>") : html.find("</title>")]

        if "louer" in title:
            os.system("mv " + html_folder + "/" + html_file + " " + a_louer_html_folder)

        if "vendre" in title:
            os.system("mv " + html_folder + "/" + html_file + " " + a_vendre_html_folder)

    return None

#-03-T------------------------------------------------------------------------------------------

def clean_data(keys : list[str], values : list[str]) -> dict[str : bool or int or float or str]:

    """
    Clean the data and return a dictionary with the keys and the values

    Parameters
    ----------
    keys : list[str]
        The keys

    values : list[str]
        The values

    Returns
    -------
    dict[str : bool or int or float or str]
        The dictionary with the keys and the values

    Raises
    ------
    Exception
        If the keys is not a list

    Exception
        If the values is not a list

    """


    """
    The keys and the values are the following:
    - To rent
    - To sell
    - Price : Loyermensueldemandé or prix
    - Number of rooms : Chambres
    - Living Area : Surfacehabitable
    - Fully equipped kitchen (Yes/No) : Typedecuisine
    - Furnished (Yes/No) : Meublé
    - Open fire (Yes/No) : Foyer
    - Terrace (Yes/No) : Terrasse
    - If yes: Area : Surfacedelaterasse
    - Garden (Yes/No) : Jardin
    - If yes: Area : Surfacedujardin
    - Surface of the land : Surfaceareabâtir
    - Surface area of the plot of land : Jardin + Surfaceareabâtir
    - Number of facades : Nombredefaçades
    - Swimming pool (Yes/No) : Piscine
    - State of the building (New, to be renovated, ...) : Étatdubâtiment
    
    """

    #create the dictionary 
    data = {
        "To rent" : None,
        "To sell" : None,
        "Price" : None,
        "Number of rooms" : None,
        "Living Area" : None,
        "Fully equipped kitchen" : None,
        "Furnished" : None,
        "Open fire" : None,
        "Terrace" : None,
        "Area of the terrace" : None,
        "Garden" : None,
        "Area of the garden" : None,
        "Surface of the land" : None,
        "Surface area of the plot of land" : None,
        "Number of facades" : None,
        "Swimming pool" : None,
        "State of the building" : None
    }


    if len(keys) > len(values):
        #remove element "" from keys
        keys = [i for i in keys if i != ""]
        #remove element "" from values
        values = [i for i in values if i != ""]

    
    #remove " " and "" from the keys
    keys = [i for i in keys if i != " " and i != ""]

    index = None
    for i,value in enumerate(values):
        value = value.lower()

        if "oui" in value:
            values[i] = True 
        elif "noncommuniqué" in value:
            values[i] = None
        elif "non" in value:
            values[i] = False
        elif re.findall(r"[0-9]+", value):
            values[i] = int(re.findall(r"[0-9]+[.]*[0-9]*", value)[0].replace(".",""))
        elif "assurezcebienassurezcebiencontrelesincendiesavecimmowebprotectvoirmondevis" in value:
            index = i
        else:
            continue





    if index != None:
        # remove element i from the list
        values.remove(values[index])

  
    #find the index of the values that correspond to the keys
    for key in keys:

        ke = unidecode(key)
        ke = ke.lower()
        ke = ke.replace(" ", "")   
        #replace carriage
        ke = ke.replace("\r", "")
        #replace newline
        ke = ke.replace("\n", "")
        # if loyer in key.lower()
        if ke == "loyermensueldemande":
            #print(ke,values[keys.index(key)])
            data["Price"] = values[keys.index(key)]
            
            data["To rent"] = True
            data["To sell"] = False

        if ke == "prix":
            #print(ke,values[keys.index(key)])
            data["Price"] = values[keys.index(key)]
            data["To rent"] = False
            data["To sell"] = True

        if ke == "chambres":
            #print(ke,values[keys.index(key)])
            data["Number of rooms"] = values[keys.index(key)]

        if ke == "surfacehabitable":
            #print(ke,values[keys.index(key)])
            data["Living Area"] = values[keys.index(key)]

        if ke == "typedecuisine":
            #print(ke,values[keys.index(key)])
            data["Fully equipped kitchen"] = values[keys.index(key)]

        if ke == "meuble":
            
            data["Furnished"] = values[keys.index(key)]

        if ke == "foyer":
            #print(ke,values[keys.index(key)])
            data["Open fire"] = values[keys.index(key)]

        if ke == "terrasse":
            #print(ke,values[keys.index(key)])
            data["Terrace"] = values[keys.index(key)]

        if ke == "surfacedelaterasse":
            #print(ke,values[keys.index(key)])
            data["Area of the terrace"] = values[keys.index(key)]
            data["Terrace"] = True

        if ke == "jardin":
            #print(ke,values[keys.index(key)])
            data["Garden"] = values

        if ke == "surfacedujardin":
            #print(ke,values[keys.index(key)])
            data["Area of the garden"] = values[keys.index(key)]
            data["Garden"] = True

        if ke == "surfaceareabatir":
            #print(ke,values[keys.index(key)])
            data["Surface of the land"] = values[keys.index(key)]

        if ke == "nombredefacades":
            #print(ke,values[keys.index(key)])
            data["Number of facades"] = values[keys.index(key)]

        if ke == "piscine":
            #print(ke,values[keys.index(key)])
            data["Swimming pool"] = values[keys.index(key)]

        if ke == "etatdubatiment":
            #print(ke,values[keys.index(key)])
            data["State of the building"] = values[keys.index(key)]

    return data
    


#-03-T------------------------------------------------------------------------------------------

def find_values_of_soups (soup : any) -> tuple[list[str], list[str]]:

    """
    Find the values of the keys in the soup

    Parameters
    ----------
    soup : any
        The soup

    Returns
    -------
    tuple[list[str], list[str]]
        The keys and the values

    Raises
    ------
    Exception
        If the soup is not a BeautifulSoup object

    """

    #check if the soup is a BeautifulSoup object
    if not isinstance(soup, BeautifulSoup):
        raise Exception("The soup must be a BeautifulSoup object")
    

    keys = soup.find_all("th")
    values = soup.find_all("td")

    keys = [k.text for k in keys]
    values = [v.text for v in values]

    return (keys, values)


#-03-S------------------------------------------------------------------------------------------

def extract_data(html_content : str) -> dict[str : bool or int or float or str]:
    
    """
    Extract the data from the html file and return a dictionnary with the data
    
    Parameters
    ----------
    html_content : str
    The html file
    
    Returns
    -------
    dict[str : bool or int or float or str]
        The data extracted from the html file

    Raises
    ------
    Exception
        If the html_content is not a string
    
    """
    
    #check if the html_content is a string
    if not isinstance(html_content, str):
        raise Exception("The html_content must be a string")


    soup = BeautifulSoup(html_content , "html.parser")

    keys, values = find_values_of_soups(soup)

    return clean_data(keys, values)

    
#-03-P------------------------------------------------------------------------------------------

def extract_data_from_html(path : str) -> dict[str : dict[str : bool or int or float or str]]:

    """
    Extract the data from the html files and return a dictionnary with the data

    Parameters
    ----------

    path : str
        The path to the folder where the html files are stored

    Returns
    -------
    dict[str : dict[str : bool or int or float or str]]
        The data extracted from the html files

        structure 
    {id :{
        Addresse : str 
        Price : int
        ...
        key1 : value1,
        key2 : value2,
        key3 : value3,
        ...
        keyn : valuen
        postcode : int
        }
    }

    Raises
    ------
    Exception
        If the html is not a string or a list of strings

    Exception
        If the path is not a string

    Warning
        If the path does not exist or is empty

    """

    #check if the path is a string
    if not isinstance(path, str): 
        raise Exception("The path must be a string")

    #check if the path exist and is not empty
    if not os.path.exists(path) or len(os.listdir(path)) == 0:
        warnings.warn("The path does not exist or is empty")

    #the data extracted from the html files
    data = {}

    #get all the html files
    html = os.listdir(path)

    #extract the data from the html files
    for html_file in tqdm(html):
        with open(path + "/" + html_file, "r") as f:
            html_content = f.read()

        #without .html
        id = int(html_file[:-5])

        data[id] = extract_data(html_content)

    return data

#-04-P------------------------------------------------------------------------------------------

def save_data_to_csv(data : dict[int : dict[str : any]], csv_name : str = "data.csv") -> None:
    """Save the data to a csv file 
    with keys of the dictionarry as
    first collumn rows and all of the keys of 
    the dictionaries inside the main dictionnary 
    as collumns (keys could be different for each 
    dictionary) and the values of these inside
    the corresponding row. all empty cells will
    have the value None.

    Parameters
    ----------
    data : dict[int : dict[str : any]]
        The data to save

    structure 
    {id :{
        Addresse : str 
        Price : int
        ...
        key1 : value1,
        key2 : value2,
        key3 : value3,
        ...
        keyn : valuen
        postcode : int
        }
    }

    csv_name : str = "data.csv"
        The name of the csv file

    Returns
    -------
    None

    Raises
    ------

    Exception
        If the csv_name is not a string

    Exception
        If the csv_name does not finish by .csv
    """

    #check if the csv_name is a string
    if not isinstance(csv_name, str):
        raise Exception("The csv_name must be a string")

    #check if the csv_name finish by .csv
    if not csv_name.endswith(".csv"): 
        raise Exception("The csv_name must finish by .csv")

    # Convert the dictionary to a Pandas dataframe
    df = pd.DataFrame.from_dict(data, orient='index')

    # Save the dataframe to a CSV file
    df.to_csv('data.csv')


    return None

#-05-M------------------------------------------------------------------------------------------

if __name__ == "__main__":
    pass


    #immoweb_url_scraper()
    #immoweb_page_scraper(folder_path = "/home/flotchet/server/first_pool/Raw_HTML")
    #html_errors_excluder()
    #html_a_louer_vendre_excluder()
    data = extract_data_from_html("/home/flotchet/server/first_pool/Raw_HTML_a_louer_normal")
    save_data_to_csv(data, csv_name = "data_a_louer_normal.csv")