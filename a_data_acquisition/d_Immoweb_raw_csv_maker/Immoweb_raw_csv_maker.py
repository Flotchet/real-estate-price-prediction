#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#-04-P------------------------------------------------------------------------------------------

def save_data_to_csv(data : dict[int : dict[str : any]], csv_name : str = "data.csv") -> None:
    """Save the data to a csv file 
    with keys of the dictionarry as
    first collumn rows and all of the keys of 
    the dictionaries inside the main dictionnary 
    as collumns (keys could be different for each 
    dictionary) and the values of these inside
    the corresponding row. all empty cells will
    have the value None.

    Parameters
    ----------
    data : dict[int : dict[str : any]]
        The data to save

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

    csv_name : str = "data.csv"
        The name of the csv file

    Returns
    -------
    None

    Raises
    ------

    Exception
        If the csv_name is not a string

    Exception
        If the csv_name does not finish by .csv
    """

    #check if the csv_name is a string
    if not isinstance(csv_name, str):
        raise Exception("The csv_name must be a string")

    #check if the csv_name finish by .csv
    if not csv_name.endswith(".csv"): 
        raise Exception("The csv_name must finish by .csv")

    # Convert the dictionary to a Pandas dataframe
    df = pd.DataFrame.from_dict(data, orient='index')

    # Save the dataframe to a CSV file
    df.to_csv(csv_name)

    return None

#-04-M------------------------------------------------------------------------------------------
if __name__ == "__main__":
    d = {0 : {"A" : 0}}
    save_data_to_csv(d)