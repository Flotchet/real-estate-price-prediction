#-I-QOF-----------------------------------------------------------------------------------------
import itertools 
#-I-PERF----------------------------------------------------------------------------------------
from multiprocessing import Pool
#-I-DS------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd
#-I-WEB-----------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
from selenium import webdriver
#-----------------------------------------------------------------------------------------------



#-01-S------------------------------------------------------------------------------------------

def url_cleaner(hrefs : list[str]) ->  list[str]:
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
        #open the driver and set it up
        driver = webdriver.Firefox()
        driver.set_window_size(1080, 3840)

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

#-01-M------------------------------------------------------------------------------------------
if __name__ == "__main__":
    immoweb_url_scraper()