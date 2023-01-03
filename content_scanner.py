import bs4 as BeautifulSoup
import os
import re
import sys
import time

import numpy as np
import pandas as pd

def html_loader(file_name : str or list[str]) -> str or list[str]:
    """Load the html file.
    
    Parameters
    ----------
    file_name : str or list[str]
        The name of the html file.
    
    Returns
    -------
    str or list[str]
        The html file.
    
    Raises
    ------
    TypeError
        If the file_name is not a string or a list of strings.
    FileNotFoundError
        If the file does not exist.
    """
    if isinstance(file_name, str):
        #verify if the file exists before reading it
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The file {} does not exist.".format(file_name))
        with open(file_name, "r") as f:
            html = f.read()
        return html
    elif isinstance(file_name, list):
        html = []
        for file_n in file_name:
            #verify if the file exists before reading it
            if not os.path.isfile(file_n):
                raise FileNotFoundError("The file {} does not exist.".format(file_n))
            with open(file_n, "r") as f:
                html.append(f.read())
        return html
    else:
        raise TypeError("The file_name is not a string or a list of strings.")


def main():
    #load the html file
    html = html_loader("raw_html/10306068.html")
    #parse the html file
    soup = BeautifulSoup.BeautifulSoup(html, "html.parser")
    #find all the links
    values = soup.find_all("td")

    keys= soup.find_all("th")
    values = [i.text.replace(" ","").replace("\n","") for i in values]
    keys = [i.text.replace(" ","").replace("\n","") for i in keys]

    stri = "vhhigiudggzoezd65432igzeozaey   ipzezagfuez"





    index = None
    for i,value in enumerate(values):
        value = value.lower()

        if "oui" in value:
            values[i] = True
        elif "Adresse" in keys[i]:
            continue 
        elif "noncommuniqué" in value:
            values[i] = None
        elif "non" in value:
            values[i] = False
        elif re.findall(r"[0-9]+", value):
            values[i] = int(re.findall(r"[0-9]+", value)[0])
        elif "assurezcebienassurezcebiencontrelesincendiesavecimmowebprotectvoirmondevis" in value:
            index = i
        else:
            continue

    if index != None:
        # remove element i from the list
        values.remove(values[index])


    #remove element "" from keys
    keys = [i for i in keys if i != ""]
    #remove element last element from values
    values = values[:-1]
    #remove half of the string in values that correspond of the indice 
    #of "Loyermensueldemandé" in keys

    for i in range(len(values)):
        print(keys[i], values[i])

if __name__ == "__main__":
    main()