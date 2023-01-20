#-I-QOF-----------------------------------------------------------------------------------------
import traceback
#-I-OS------------------------------------------------------------------------------------------
import os
import shutil
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-P-Import--------------------------------------------------------------------------------------
from a_Immoweb_URL_scraper.Immoweb_URL_scraper import *
from b_Immoweb_HTML_scraper.Immoweb_HTML_scraper import *
from c_Immoweb_data_extractor.Immoweb_data_extractor import *
from d_Immoweb_raw_csv_maker.Immoweb_raw_csv_maker import *
#-----------------------------------------------------------------------------------------------

#-P-scraper-------------------------------------------------------------------------------------
def immoweb_scraper() -> None:

    """
    The main function of the program
    
    Returns
    -------
    None
    """


    print("starting fist phase: getting all the urls to scrape")
    #delete the file urls.csv if it exists
    if os.path.exists("urls.csv"):
        os.remove("urls.csv")

    immoweb_url_scraper()

    #delete the file geckodriver.log if it exists
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log")



    print("starting second phase: scraping the in the csv file (getting all the html files)")
    #move all files from Raw_HTML_a to Raw_HTML with os library 
    for file in os.listdir("/home/flotchet/server/first_pool/Raw_HTML"):
        shutil.move(
            "/home/flotchet/server/first_pool/Raw_HTML/" + file, 
            "/home/flotchet/server/first_pool/Raw_HTML_a")

    #rename Raw_HTML_a in Raw_HTML_b
    os.rename( 
        "/home/flotchet/server/first_pool/Raw_HTML_a", 
        "/home/flotchet/server/first_pool/Raw_HTML_b")

    #rename Raw_HTML in Raw_HTML_a
    os.rename(
        "/home/flotchet/server/first_pool/Raw_HTML", 
        "/home/flotchet/server/first_pool/Raw_HTML_a")

    #rename Raw_HTML_b in Raw_HTML
    os.rename(
        "/home/flotchet/server/first_pool/Raw_HTML_b", 
        "/home/flotchet/server/first_pool/Raw_HTML")

    immoweb_page_scraper(folder_path = "/home/flotchet/server/first_pool/Raw_HTML")
    
    #delete the file geckodriver.log if it exists
    if os.path.exists("geckodriver.log"):
        os.remove("geckodriver.log")



    print("starting third phase: extracting the data from the html files")

    html_a_louer_vendre_excluder(
        a_louer_html_folder  = "/home/flotchet/server/first_pool/Raw_HTML_a",
        a_vendre_html_folder = "/home/flotchet/server/first_pool/Raw_HTML_a")


    data = extract_data_from_html("/home/flotchet/server/first_pool/Raw_HTML_a")



    print("starting fourth phase: saving the data to a csv file")
    #delete data_a.csv if it exists
    if os.path.exists("data_a.csv"):
        os.remove("data_a.csv")

    save_data_to_csv(data, csv_name = "data_a.csv")



    print("starting fifth phase: calculating the average price to rent and to buy")
    #load data_a.csv with collumns names using pandas
    data_a = pd.read_csv("data_a.csv")
    print(data_a)
    #variable collumn price where to_rent collumn is True with pandas
    data_a_to_rent = data_a[data_a["To rent"] == True]["Price"]
    #variable collumn price where to_rent collumn is False with pandas
    data_a_to_buy = data_a[data_a["To rent"] == False]["Price"]

    #remove None values
    data_a_to_rent = data_a_to_rent.dropna()
    data_a_to_buy = data_a_to_buy.dropna()
    multiplicator = data_a_to_buy.mean() / data_a_to_rent.mean()

    #print average
    print("average price to rent: ", data_a_to_rent.mean())
    print("average price to buy: ", data_a_to_buy.mean())
    print("average value multiplicator: ", multiplicator)

    return None

if __name__ == "__main__":

    try:
        immoweb_scraper()

    except KeyboardInterrupt:
        print("""Keyboard interupt""")
        
    except Exception as e:

        # print the exception
        print(traceback.format_exc())
        
        # print the exception
        print(e)