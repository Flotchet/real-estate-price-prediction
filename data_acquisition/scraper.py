import itertools 
import time
import os
import psutil
import warnings
import gc

from multiprocessing import Pool

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver





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

def immoweb_page_href(url : str = "") -> list[str]:
    """Extract the href of the houses from the immoweb page.

    Parameters
    ----------
    url : str
        The url of the immoweb page.

    Returns
    -------
    list[str]
        The href of the houses.

    Raises
    ------
    Exception
        If the url is not a string.
    """

    if not isinstance(url, str):
        raise Exception("The url is not a string.")

    html = scrape_html_with_selenium(url)
    soup = BeautifulSoup(html, "html.parser")

    return [a["href"] for a in soup.find_all("a", {"class": "card__title-link"})]

def immoweb_page_hrefs(urls : list[str] = []) -> list[str]:
    """Extract the href of the houses from the immoweb pages.

    Parameters
    ----------
    urls : list[str]
        The urls of the immoweb pages.

    Returns
    -------
    list[str]
        The href of the houses.

    Raises
    ------
    Exception
        If the urls is not a list of strings.
    """

    if not isinstance(urls, list):
        raise Exception("The urls is not a list of strings.")

    return [immoweb_page_href(url) for url in urls]

def scrape_html_with_selenium(url : list[str] or str) -> list[str]:
    """Scrape the html of the page with selenium.

    Parameters
    ----------
    urls : list[str] or str
        The urls of the page.

    Returns
    -------
    list[str]
        The html of the pages.

    Raises
    ------
    Exception
        If the url is not a string or a list of strings.
    """

    if isinstance(url, str):
        driver = webdriver.Firefox()
        driver.get(url)
        html = driver.page_source
        driver.close()
        return html

    elif isinstance(url, list):
        driver = webdriver.Firefox()
        htmls = []
        for u in url:
            driver.get(u)
            htmls.append(driver.page_source)
        driver.close()
        return htmls

    else:
        raise Exception("The url is not a string or a list of strings.")

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
        driver.delete_all_cookies()

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


def immoweb_url_scrapping() -> None:
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
   

def immoweb_page_scrapping(csv_name : str = "urls.csv", 
                           folder_path : str = "./raw_html", 
                           time_stamp : bool = False, 
                           tries : int = 10) -> None:
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

    #check if the filename finish by .csv
    if csv_name[-4:] != ".csv":
        raise Exception("The file name must finish by .csv")

    #get the keys the set of all keys in the dictionaries (and the string "id" as fisrt value)
    keys = {"id"}
    for dictionaries in data.values():
        for dictionary in dictionaries:
            keys.update(list(dictionary.keys()))

    #create a dataframe with the keys as columns
    df = pd.DataFrame(columns = keys)

    #fill the dataframe with the data
    for id, dictionaries in data.items():
        for dictionary in dictionaries:
            df = df.append({**dictionary, "id" : id}, ignore_index = True)

    #save the dataframe to a csv file
    df.to_csv(csv_name, index = False)

    return None



if __name__ == "__main__":
    immoweb_page_scrapping(folder_path = "/home/flotchet/server/first_pool/Raw_HTML")