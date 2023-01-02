from requests import Session
import bs4
import warnings



def get_page_content(url : str , 
                     endpoint : str or None = None , 
                     session : any or None = None , 
                     error : bool = False , 
                     warns : bool = True 
                                                    ) -> tuple[str, int]:


    """
    get the content of a page
    takes a url and an endpoint
    return the content of the page
    """

    if session is None:
        session = Session()

    if endpoint is not None:
        url = url + endpoint

    req = session.get(url=url)

    # check if status is 200
    if req.status_code != 200:

        message = url + " " + str(req.status_code)

        if warns:
            warnings.warn(message)

        if error:
            raise Exception(message)

        return message, req.status_code

    return req.text, req.status_code



def get_first_wiki_paragraph(url : str ,
                        endpoint : str,
                        session : any or None = None,
                        error : bool = False,
                        warns : bool = True
                                                     ) -> tuple[str, int]:

    """
    get the first paragraph of a wikipedia page
    takes a url and an endpoint
    return the first paragraph of the page
    """

    if session is None:
        session = Session()

    if endpoint is not None:
        url = url + endpoint

    req = session.get(url=url)

    # check if status is 200
    if req.status_code != 200:

        message = url + " " + str(req.status_code)

        if warns:
            warnings.warn(message)

        if error:
            raise Exception(message)

        return message, req.status_code

    soup = bs4.BeautifulSoup(req.text, "html.parser")

    for paragraph in soup.find_all('p'):

        for _ in paragraph.find_all('b'):

            text = paragraph.text
            return text, req.status_code

    return "No paragraph found", req.status_code



def get_multiple_page_content(urls : list[str] , 
                              endpoints : list[str] or None = None , 
                              session : any or None = None , 
                              error : bool = False , 
                              warns : bool = True 
                                                            ) -> tuple[dict[str : str] , dict[str : int]]:

    """
    get the content of multiple pages
    takes a lsit url and a list of endpoint
    return the content of the pages as a dict
    """

    if session is None:
        session = Session()

    if endpoints is not None:
        urls = [url + endpoint for url, endpoint in zip(urls, endpoints)]

    reqs = [session.get(url=url) for url in urls]

    # check if status is 200
    if any(req.status_code != 200 for req in reqs):

        messages = {url + " " + str(req.status_code) : req.status_code for url, req in zip(urls, reqs)}

        if warns:
            for message in messages:
                warnings.warn(message)

        if error:
            raise Exception("One or more scraping have failed")

        return messages, messages

    return {url : req.text for url, req in zip(urls, reqs)}, {url : req.status_code for url, req in zip(urls, reqs)}


def get_multiple_endpoint_content(url : str , 
                                  endpoints : list[str] or None = None , 
                                  session : any or None = None , 
                                  error : bool = False , 
                                  warns : bool = True 
                                                                        ) -> tuple[dict[str : str] or str, dict[str : int] or int]:
    """
    get the content of multiple pages
    takes a url and a list of endpoint
    return the content of the pages as a dict
    """

    if endpoints is None:
        return get_page_content(url)

    if session is None:
        session = Session()

    urls = [url + endpoint for endpoint in endpoints]

    reqs = [session.get(url=url) for url in urls]

    # check if status is 200
    if any(req.status_code != 200 for req in reqs):
            
            messages = {url + " " + str(req.status_code) : req.status_code for url, req in zip(urls, reqs)}
    
            if warns:
                for message in messages:
                    warnings.warn(message)
    
            if error:
                raise Exception("One or more scraping have failed")
    
            return messages, messages

    return {url : req.text for url, req in zip(urls, reqs)}, {url : req.status_code for url, req in zip(urls, reqs)}



#main function
def main():
    exemple_url = "https://fr.wikipedia.org"
    exemple_endpoint = "/wiki/Charles_de_Gaulle"
    exemple_urls = ["https://fr.wikipedia.org", "https://fr.wikipedia.org"]
    exemple_endpoints = ["/wiki/Charles_de_Gaulle", "/wiki/Charles_de_Gaulle"]

    print(get_page_content(exemple_url, exemple_endpoint))
    print(get_first_wiki_paragraph(exemple_url, exemple_endpoint))
    print(get_multiple_page_content(exemple_urls, exemple_endpoints))
    print(get_multiple_endpoint_content(exemple_url, exemple_endpoints))

if __name__ == "__main__":
    main()
