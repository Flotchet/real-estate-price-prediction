#-I-QOF-----------------------------------------------------------------------------------------
import warnings
#-I-OS------------------------------------------------------------------------------------------
import time
import os
import psutil
import gc
#-I-PERF----------------------------------------------------------------------------------------
from multiprocessing import Pool
#-I-DS------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
#-I-WEB-----------------------------------------------------------------------------------------
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import urllib3
#-----------------------------------------------------------------------------------------------

#-02-S------------------------------------------------------------------------------------------

def scrape_html_with_selenium_with_save(urls : list[str] or str, 
                                        folder_path : str = "./raw_html", 
                                        time_stamp : bool = False,
                                        headless : bool = False,
                                        cache : bool = False,
                                        css : bool = True
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

    css : bool = True
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

    #close the driver      
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
    url_tot = len(urls)

    folder_path = [folder_path]*n_process
    time_stamp = [time_stamp]*n_process

    # if the nuùber of files in folder is different than the number of urls retries n times
    
    try:
        for _ in range(tries):
            #Create the pool of workers
            with Pool(n_process) as pool:
                pool.starmap(scrape_html_with_selenium_with_save, zip(urls, folder_path, time_stamp))

            #check if the number of files in folder is less than the total number of urls
            if len(os.listdir(folder_path[0])) < len(url_tot):
                break

    except urllib3.exceptions.MaxRetryError:
        warnings.warn("MaxRetryError occured in immoweb_page_scraper")

    except WebDriverException:
        warnings.warn("WebDriverException occured in immoweb_page_scraper")

    except Exception:
        warnings.warn("An exception occured in immoweb_page_scraper")

    #kill all firefox and Web Content process
    os.system("killall firefox")

    return None

#-02-M------------------------------------------------------------------------------------------
if __name__ == "__main__":
    immoweb_page_scraper()