# real-estate-price-prediction (Global README.md)

## Current state

Data visualisation

Total number of data : 78193 

Total number of features : 29

Total number of excluded features : 17

## Prerequises (Scraping part)

Python 3.11.1 64-bit

Firefox

*Tested on Fedora release 37 (Thirty Seven) x86_64 kernel 6.0.15-300.fc37.x86_64 but it should works on most linux distro

* bs4
* gc
* itertools
* multiprocessing
* numpy
* os
* pandas
* psutil
* re
* selenium
* shutil
* time
* tqdm
* traceback
* unidecode
* warnings

## Prerequises (data visualisation)

Python 3.11.1 64-bit

Firefox

*Tested on Fedora release 37 (Thirty Seven) x86_64 kernel 6.0.15-300.fc37.x86_64 but it should works on most linux distro

* pandas
* matplotlib
* seaborn
* numpy
* openpyxl


## Recommended system requirements

CPU: 8core (Intel i7-10875H)

RAM: 32GB

GPU: /

Vram: /

HDD: 15GB of free space (SSD recommanded because of the large number of small files)

## What it does (Scraping part)

this project creates a dataset from immoweb (be-fr) in the form of a csv file of this shape

| URLS (name of the column not present in the csv) |
| ------------------------------------------------ |
| url 1                                            |
| url 2                                            |
| ...                                              |
| url i                                            |
| ...                                              |
| url n-1                                          |
| url n                                            |

### First part

1. Generates somes url to scrape ne announce
2. Scrap the urls and get the hrefs in each pages
3. Clean the hrefs by excluding all urls that are not starting by https://www.immoweb.be/fr/annonce/
4. Store the freshly obtained urls into a csv file

### Second part

1. Open and read the csv file of the first part
2. Get all the urls in the file
3. Scrap all the webcontent of each webpage attached to the url
4. Save each webcontent into a large ammount of html files

### Third part

1. Open and read each html file
2. Exctrat the data with bs4 and transform the data into usable types (int,bool etc.)
3. Make a dictionary with this structure:

   Dictionnary:

   * id : Inner dictionnary

   Inner dictionnary:

   * To rent : bool
   * To sell : bool
   * Price : int
   * Number of rooms : int
   * Living Area : float
   * Fully equipped kitchen : bool
   * Furnished : bool
   * Open fire : bool
   * Terrace : bool
   * Area of the terrace : float
   * Garden : bool
   * Area of the garde : float
   * Surface of the land : float
   * Surface area of the plot of land : float
   * Number of facades : int
   * Swimming pool : bool
   * State of the building : str
   * zipcode : int
   * type : str

### Final part

1. Store the previous dictionary as a csv file of the shape below
2. Print the average rent, the average price and a multiplicator in months to have the value of the house

| ID     | To rent | To sell | Price  | Number of rooms | ... | zipcode | type        |
| ------ | ------- | ------- | ------ | --------------- | --- | ------- | ----------- |
| id 1   | False   | True    | 97000  | 3               | ... | 4000    | Appartement |
| id 2   | True    | False   | 800000 | None            | ... | 1825    | Penthouse   |
| ...    | ...     | ...     | ...    | ...             | ... | ...     | ...         |
| id i   | None    | None    | None   | None            | ... | None    | None        |
| ...    | ...     | ...     | ...    | ...             | ... | ...     | ...         |
| id n-1 | None    | None    | 54000  | 5               | ... | 1000    | Maison      |
| id n   | True    | False   | 1000   | 85              | ... | 1010    | Bugalow     |

## How to use it

just run scraper.py and it should do the trick but your can import the file as a library and use the functions in your own project

---

## Informations about the functions

### scraper.py

#### First part

##### url_cleaner(hrefs : list[str]) -> list[str]

remove all urls that don't start with "https://www.immoweb.be/fr/annonce/"

##### multi_process_scrape_html_href_with_selenium(urls : list[str] , n_process : int = 4) -> list[str]

Scrape all the hrefs in the html of the pages with selenium

##### immoweb_url_constructor(n : int = 333) -> list[str]

Generates a list of urls to scrape with this shape

"https://www.immoweb.be/fr/recherche/maison-et-appartement/a-{sell}/{province}/province?countries=BE&page={page}&orderBy=relevance"

##### immoweb_url_scraper() -> None

Scrape the urls of the houses from immoweb and save the data into a csv with this shape

| URLS (name of the column not present in the csv) |
| ------------------------------------------------ |
| url 1                                            |
| url 2                                            |
| ...                                              |
| url i                                            |
| ...                                              |
| url n-1                                          |
| url n                                            |

#### **Second part**

##### scrape_html_with_selenium_with_save(urls : list[str] or str ,  folder_path : str = "./raw_html" , time_stamp : bool = False , headless : bool = False , cache : bool = False , css : bool = True) -> int

Scrape the html of the page with selenium and saves each file to a folder as name+time_stamp.html if the file doesn't already exist in the destination folder.

**Warning:** could have some memory leackage because of selenium -> driver firefox and will stop if memory usage is more than 98 percents

##### immoweb_page_scraper(csv_name : str = "urls.csv", folder_path : str = "./raw_html", time_stamp : bool = False , tries : int = 1) -> None

Scrape the html of the page with selenium and saves each file to a folder as name+time_stamp.html if the file doesn't already exist in the destination folder in a multiprocess fashion.

**Warning:** could have some memory leackage because of selenium. -> driver firefox and will stop some process if memory usage is more than 98 percents.

#### Third part

##### html_errors_excluder(html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML" , excluded_html_folder :str = "/home/flotchet/server/first_pool/Raw_HTML_Rejected") -> None

Exclude the html files that have errors 404 or 500.

##### html_a_louer_vendre_excluder(html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML",a_louer_html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML_a_louer" , a_vendre_html_folder : str = "/home/flotchet/server/first_pool/Raw_HTML_a_vendre") -> None

Exclude the html files that contains "à louer" in their title in a folder and the html files that contains "à vendre" in a second folder.

##### clean_data(keys : list[str] , values : list[str]) -> dict[str : bool or int or float or str]

Extract some data if a corresponding key is in the list

 The keys and the values are the following:

    - To rent / set : based of data already obtained

    - To sell / set : based of data already obtained

    - Price : Loyermensueldemandé or prix

    - Number of rooms : Chambres

    - Living Area : Surfacehabitable

    - Fully equipped kitchen (Yes/No) : Typedecuisine

    - Furnished (Yes/No) : meublé

    - Open fire (Yes/No) : combiendefeuxouverts?

    - Terrace (Yes/No) : Terrasse

    - If yes: Area : Surfacedelaterrasse

    - Garden (Yes/No) : Jardin

    - If yes: Area : surfacedujardin

    - Surface of the land : surfaceduterrain

    - Surface area of the plot of land : / computed : surfaceduterrain

    - Number of facades : Nombredefaçades

    - Swimming pool (Yes/No) : Piscine

    - State of the building (New, to be renovated, ...) : Étatdubâtiment

##### find_values_of_soups (soup : any) -> tuple[list[str] , list[str]]

Find the values and keys in the soup based on th and td tags

##### extract_data(html_content : str) -> dict[str : bool or int or float or str]

Extract the data from the html file and return a dictionnary with the data

List of data:

* To rent
* To sell
* Price
* Number of rooms
* Living Area
* Fully equipped kitchen
* Furnished
* Open fire
* Terrace
* Area of the terrace
* Garden
* Area of the garde
* Surface of the land
* Surface area of the plot of land
* Number of facades
* Swimming pool
* State of the building
* zipcode
* type

##### extract_data_from_html(path : str) -> dict[str : dict[str : bool or int or float or str]]

Extract the data from the html files and return a dictionnary of dictionnaries with the data

Dictionnary:

* id : Inner dictionnary

 Inner dictionnary:

* To rent : bool
* To sell : bool
* Price : int
* Number of rooms : int
* Living Area : float
* Fully equipped kitchen : bool
* Furnished : bool
* Open fire : bool
* Terrace : bool
* Area of the terrace : float
* Garden : bool
* Area of the garde : float
* Surface of the land : float
* Surface area of the plot of land : float
* Number of facades : int
* Swimming pool : bool
* State of the building : str
* zipcode : int
* type : str

#### Fourth part

##### save_data_to_csv(data : dict[int : dict[str : any]] , csv_name : str = "data.csv") -> None

Save the data as a csv file of this shape

| ID     | To rent | To sell | Price  | Number of rooms | ... | zipcode | type        |
| ------ | ------- | ------- | ------ | --------------- | --- | ------- | ----------- |
| id 1   | False   | True    | 97000  | 3               | ... | 4000    | Appartement |
| id 2   | True    | False   | 800000 | None            | ... | 1825    | Penthouse   |
| ...    | ...     | ...     | ...    | ...             | ... | ...     | ...         |
| id i   | None    | None    | None   | None            | ... | None    | None        |
| ...    | ...     | ...     | ...    | ...             | ... | ...     | ...         |
| id n-1 | None    | None    | 54000  | 5               | ... | 1000    | Maison      |
| id n   | True    | False   | 1000   | 85              | ... | 1010    | Bugalow     |
