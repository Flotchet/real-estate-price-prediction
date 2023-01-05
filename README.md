# real-estate-price-prediction

## Current state

Currently in polishing state

## prerequises

Python 3.10

Firefox

* time
* os
* psutil
* warnings
* gc
* tqdm
* re
* multiprocessing
* numpy
* pandas
* itertools
* bs4
* selenium
* unidecode

## What it does

this project creates a dataset from immoweb (be-fr) in the form of a csv file

### First part

1. Generates somes url to scrape ne announce
2. Scrap the urls and get the hrefs in each pages
3. Clean the hrefs by excluding all urls that are not starting by https://www.immoweb.be/fr/annonce/
4. Store the freshly obtained urls into a csv file

### Second part

1. open and read the csv file of the first part
2. get all the urls in the file
3. scrap all the webcontent of each webpage attached to the url
4. save each webcontent into a large ammount of html files

### Third part

1. open and read each html file
2. exctrat the data with bs4 and transform the data into usable types (int,bool etc.)
3. make a dictionary with this structure

    {id :{

    ...

    key1 : value1,

    key2 : value2,

    key3 : value3,

    ...

    }

    }

### Final part

store the previous dictionary as a csv file 



## How to use it

just run scraper.py and it should do the trick but your can import the file as a library and use the functions in your own project

## Informations about the functions
