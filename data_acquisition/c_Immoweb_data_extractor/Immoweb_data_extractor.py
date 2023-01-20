#-I-QOF-----------------------------------------------------------------------------------------
import warnings
#-I-OS------------------------------------------------------------------------------------------
import os
#-I-PROGRESS------------------------------------------------------------------------------------
from tqdm import tqdm
#-I-REGEX---------------------------------------------------------------------------------------
import re
#-I-WEB-----------------------------------------------------------------------------------------
from bs4 import BeautifulSoup
#-I-txt-----------------------------------------------------------------------------------------
from unidecode import unidecode
#-----------------------------------------------------------------------------------------------

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
            data["Price"] = int(values[keys.index(key)])
            
            data["To rent"] = True
            data["To sell"] = False

        if ke == "prix":
            #print(ke,values[keys.index(key)])
            data["Price"] = int(values[keys.index(key)])
            data["To rent"] = False
            data["To sell"] = True

        if ke == "chambres":
            #print(ke,values[keys.index(key)])
            data["Number of rooms"] = int(values[keys.index(key)])

        if ke == "surfacehabitable":
            #print(ke,values[keys.index(key)])
            data["Living Area"] = values[keys.index(key)]

        if ke == "typedecuisine":
            #print(ke,values[keys.index(key)])
            tmp = values[keys.index(key)]
        
            data["Fully equipped kitchen"] = None
            if type(tmp) == str:
                tmp = tmp.lower()
                tmp = unidecode(tmp)
                tmp = tmp.replace(" ", "")   
                tmp = tmp.replace("\r", "")
                tmp = tmp.replace("\n", "")

                if "pas" in tmp:
                    data["Fully equipped kitchen"] = False
                elif "" == tmp:
                    data["Fully equipped kitchen"] = None
                else:
                    data["Fully equipped kitchen"] = True 

        if ke == "meuble":
            
            data["Furnished"] = values[keys.index(key)]

        if ke == "combiendefeuxouverts?" or ke == "combiendefeuouverts":
            #print(ke,values[keys.index(key)])
            if values[keys.index(key)] > 0:
                data["Open fire"] = True
            else:
                data["Open fire"] = False

        if ke == "terrasse":
            #print(ke,values[keys.index(key)])
            data["Terrace"] = values[keys.index(key)]

        if ke == "surfacedelaterrasse":
            #print(ke,values[keys.index(key)])
            data["Area of the terrace"] = values[keys.index(key)]
            data["Terrace"] = True

        if ke == "jardin":
            #print(ke,values[keys.index(key)])
            data["Garden"] = values[keys.index(key)]

        if ke == "surfacedujardin":
            #print(ke,values[keys.index(key)])
            data["Area of the garden"] = values[keys.index(key)]
            data["Garden"] = True

        if ke == "surfaceduterrain":
            #print(ke,values[keys.index(key)])
            data["Surface of the land"] = values[keys.index(key)]
            data["Surface area of the plot of land"] = values[keys.index(key)]

        if ke == "nombredefacades":
            #print(ke,values[keys.index(key)])
            data["Number of facades"] = int(values[keys.index(key)])

        if ke == "piscine":
            #print(ke,values[keys.index(key)])
            data["Swimming pool"] = values[keys.index(key)]

        if ke == "etatdubatiment":
            #print(ke,values[keys.index(key)])
            #remove all " "
            tmp = values[keys.index(key)]
            tmp = tmp.replace(" ", "")
            data["State of the building"] = tmp

    # optianal based on our logic
    # if Garden == None -> == false surface = 0
    if data["Garden"] == None:
        data["Garden"] = False
        data["Area of the garden"] = 0

    # if Terrace == None -> == false surface = 0
    if data["Terrace"] == None:
        data["Terrace"] = False
        data["Area of the terrace"] = 0

    # if Swimming pool == None -> == false
    if data["Swimming pool"] == None:
        data["Swimming pool"] = False

    # if Open fire == None -> == false
    if data["Open fire"] == None:
        data["Open fire"] = False

    return data

#-03-T------------------------------------------------------------------------------------------

def find_values_of_soups (soup : any) -> tuple[list[str], list[str]]:

    """
    Find the values and keys in the soup

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

    locality = soup.find_all("span", attrs={"class": "classified__information--address-row"})
    subtype_property = soup.find_all("h1",attrs={"class": "classified__title"})

    for elem in locality :
        pattern = "([0-9]{4})"
        elem_text = elem.text
        if re.findall(pattern, elem_text) :
            zip_code = re.findall(pattern, elem_text)
            zip_code_str = zip_code[0]

    for elem in subtype_property :
        elem_text = elem.text
        elem_text = elem_text.replace(" ","").replace("\n","")

        if elem_text.find("louer"):
            index_a = elem_text.find("à")
            s_type = elem_text[:index_a]
            
        elif elem_text.find("vendre"):
            index_vendre = elem_text.find("à")
            s_type = elem_text[:index_vendre] 

    data = clean_data(keys, values)

    data["zipcode"] = zip_code_str
    data["type"] = s_type

    return data

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

#-03-M------------------------------------------------------------------------------------------
if __name__ == "__main__":
    data = extract_data_from_html("data/html")
    print(data)