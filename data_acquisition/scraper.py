import itertools 
import time
import os

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
    """

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
    """

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
        driver.close()
        soup = BeautifulSoup(html, "html.parser")
        return [a["href"] for a in soup.find_all("a", {"class": "card__title-link"})]

    elif isinstance(url, list):
        driver = webdriver.Firefox()
        htmls = []
        for u in url:
            driver.get(u)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")
            htmls.append([a["href"] for a in soup.find_all("a", {"class": "card__title-link"})])
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
    """

    return [href for href in hrefs if href.startswith("https://www.immoweb.be/fr/annonce/")]


def multi_process_scrape_html_href_with_selenium(urls : list[str], n_process : int = 4) -> list[str]:
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

def multi_process_scrape_html_content_with_selenium(urls : list[str], n_process : int = 4) -> list[str]:
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
        return pool.map(scrape_html_with_selenium, urls)


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


def scrape_html_with_selenium_with_save(urls : list[str] or str, folder_path : str = "./raw_html", time_stamp : bool = True) -> int:
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

    Returns
    -------
    int
        The number of files saved

    Raises
    ------
    Exception
        If the url is not a string or a list of strings.

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

    #check if the url is a string
    if isinstance(urls, str):
        urls = [urls]

    #open the driver
    driver = webdriver.Firefox()
    for url in urls:
        driver.get(url)
        if time_stamp:
            with open(f"{folder_path}/{url.split('/')[-1]}_{time.time()}.html", "w") as f:
                f.write(driver.page_source)
        else:
            with open(f"{folder_path}/{url.split('/')[-1]}.html", "w") as f:
                f.write(driver.page_source)
    driver.close()

    return len(urls)
   

def immoweb_page_scrapping(csv_name : str = "urls.csv", folder_path : str = "./raw_html", time_stamp : bool = True) -> None:
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
    if not os.path.exists("./raw_html"):
        os.mkdir("./raw_html")

    #This task is IO limited so we can use a lot of process at the same
    #time to speed up the process even if they are more process than the
    #number of cpus

    #Get the number of logical cpus
    n_cpus = os.cpu_count()
    n_process = n_cpus*4

    #Divide the work with numpy as a list of list of urls
    urls = np.array_split(urls, n_process)
    #transform nparray to list
    urls = [url.tolist() for url in urls]

    folder_path = [folder_path]*n_process
    time_stamp = [time_stamp]*n_process

    #Create the pool of workers
    with Pool(n_process) as pool:
        pool.starmap(scrape_html_with_selenium_with_save, zip(urls, folder_path, time_stamp))




def main():
    pass


if __name__ == "__main__":
    immoweb_page_scrapping()