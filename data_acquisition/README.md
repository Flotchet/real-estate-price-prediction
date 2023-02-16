# real-estate-price-prediction (Data aquisition README.md)

## Project descritpion

This project is part of the data science training from Becode.org.

It aims to predict prices for houses or appartment considering the current state of the market.

## Current state

* Finalized

## What it does (In order)

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

### Scrape all href from immoweb

1. Generates somes url to scrape ne announce
2. Scrap the urls and get the hrefs in each pages
3. Clean the hrefs by excluding all urls that are not starting by https://www.immoweb.be/fr/annonce/
4. Store the freshly obtained urls into a csv file

### Scrape all the webcontent corresponding to the previously found urls

1. Open and read the csv file of the first part
2. Get all the urls in the file
3. Scrap all the webcontent of each webpage attached to the url
4. Save each webcontent into a large ammount of html files

### Exctract the data from the previously found webcontent

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

### Saving the data in a csv file

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

### Combine other dataset to the previous one and Cleaning the data

1. get new data from external sources xlsx and csv
2. Combine different data set to add features
3. clean the data by removing outliers and droping NaN and None
4. Create new features and remove others
5. Remove features that we don't need for the data visualization and create a new csv with the processed data of this form

| ID     | To sell | Price  | Number of rooms | ... | A-Taxe | Price by M**2 | Appartment |
| ------ | ------- | ------ | --------------- | --- | ------ | ------------- | ---------- |
| id 1   | True    | 97000  | 3               | ... | 92     | 4000          | True       |
| id 2   | True    | 800000 | 2               | ... | 100    | 2132          | False      |
| ...    | ...     | ...    | ...             | ... | ...    | ...           |            |
| id i   | False   | 555    | 1               | ... | 97.2   | 12.3          | False      |
| ...    | ...     | ...    | ...             | ... | ...    | ...           |            |
| id n-1 | True    | 54000  | 5               | ... | 93     | 1100          | True       |
| id n   | False   | 1000   | 85              | ... | 98     | 17            | True       |

### Recommended system requirements

CPU: 8core (Intel i7-10875H)

RAM: 64GB (works with 32GB with no other software running)

GPU: /

Vram: /

HDD: 15GB of free space (SSD recommanded because of the large number of small files)
