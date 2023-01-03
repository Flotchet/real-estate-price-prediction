import itertools 
import time

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

def immoweb_page_scrapping() -> None:
    """Scrape the pages of the houses from immoweb.
    """
    
    urls = pd.read_csv("urls.csv").values.tolist()
    urls = list(urls)
    #Flatten the list of list into a list
    urls = [item for sublist in urls for item in sublist]

    interval = 4096
    segmented = list(map(list, zip(*([iter(urls)]*interval))))
    if len(urls) % interval != 0:
        segmented.append(urls[-(len(urls) % interval):])

    for i, urls in enumerate(segmented):
        time.sleep(5)
        html = multi_process_scrape_html_content_with_selenium(urls, 8)

        #transform the list of list of str to list of str
        html = list(itertools.chain.from_iterable(html))

        #create a html file for each url with html content as content in the rew_html folder
        for url, h in zip(urls, html):
            with open(f"./raw_html/{url.split('/')[-1]}.html", "w") as f:
                f.write(h)


if __name__ == "__main__":
    immoweb_page_scrapping()