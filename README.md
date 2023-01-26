# real-estate-price-prediction (Global README.md)

## Project descritpion

This project is part of the data science training from Becode.org.

It aims to predict prices for houses or appartment considering the current state of the market.

It includes: web scraping, data cleaning, data visualisation,  machine learning, data engineering and a GUI.

## Current state

* [X] data acquisition from immoweb
* [X] data acquisition from statbel
* [X] data preparation for visualization
* [X] data preparation for modelisation
* [X] data visualization
* [X] modeling
* [ ] result analysis
* [ ] deploiment

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

## Combine other dataset to the previous one and Cleaning the data

1. get new data from external sources xlsx and csv
2. Combine different data set to add features
3. clean the data by removing outliers and droping NaN and None
4. Create new features based on t
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

## Display Graphs

1. display some graphs about the distribution and some relations between features like these one

![1673950769757](image/README/1673950769757.png)
![1673950769757](image/README/1673950972633.png)
![1673950769757](image/README/1673950803242.png)
![1673950769757](image/README/1673950860011.png)

## Train the models

* Prepare the data
* separate the datset into provinces - region - country
* adapt each dataset depending on the model
* Train the models

| Model                                                       | Average Prceision in %                      |
| ----------------------------------------------------------- | ------------------------------------------- |
| DecisionTreeRegressor                                       | 77,38                                       |
| ElasticNet                                                  | 67,67                                       |
| GradientBoostingRegressor                                   | 80,47                                       |
| KNeighborsRegressor<br />k = 10-200                         | 76,11 k=200 to 78,87 k=21                   |
| Lasso                                                       | 76,96                                       |
| LinearRegression                                            | 76,95                                       |
| RandomForestRegressor<br />d  = 50 - 350<br />n = 20 - 295 | 80,28 d=350 & n=20<br />81,33 d=150 & n=170 |
| Ridge                                                       | 76,95                                       |
| SVR                                                         | 71,11                                       |
| XGBoost<br />Absolute error mode                            | 69,86                                       |
| XGBoost<br />Squared  error mode                           | 80,78                                       |

## How to use it

You can launch the main.py to get a simple user interface to launch the project or part of it.

You can also launch each part of the project independently or import part of the project as a library (part of the project are already capable of working on any kind of website or data)

## Prerequises (Global)

Python 3.11.1 64-bit

Firefox

*Tested on Fedora release 37 (Thirty Seven) x86_64 kernel 6.0.15-300.fc37.x86_64 but it should works on most linux distro

* PySimpleGUI

Other requierements can be directly installed from the user interface from main.py

## Recommended system requirements

CPU: 8core (Intel i7-10875H)

RAM: 64GB (works with 32GB with no other software running)

GPU: /

Vram: /

HDD: 15GB of free space (SSD recommanded because of the large number of small files)
