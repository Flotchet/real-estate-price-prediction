import pandas as pd
import numpy as np
from dataclasses import dataclass

#Do the Municipal Taxes influence the median price by square meter of the propreties? If yes how?
#What kind of proprety I should buy if I want to make a new hotel based on the price by square meter?
@dataclass
class DataStructure():

    """
    Class that loads the data from the csv file into 
    a DataFrame and allows to add, drop and modify columns and rows

    Attributes
    ----------
    data_csv : str
        file path of the csv file

    data : pd.DataFrame
        DataFrame that contains the data from the csv file

    Non static methods
    ------------------
    get_data()

    save_data()

    add_column()

    add_columns()

    drop_column()

    drop_columns()

    drop_rows_by_column()

    drop_rows_by_columns()

    drop_rows_by_index()

    drop_rows_by_column_value()

    drop_rows_by_column_values()

    drop_rows_by_columns_values()

    drop_rows_by_column_value_range()

    drop_rows_by_column_value_range_and_bool()

    get_column()

    get_columns()

    get_columns_by_type()

    get_columns_by_types()

    get_columns_by_name()

    get_values_of_column()

    get_set_of_values_of_column()

    get_set_of_values_of_columns()

    drop_rows_by_column_value_range()

    drop_rows_by_column_value_range_and_bool()

    get_column()

    get_columns()

    get_columns_by_type()

    get_columns_by_types()

    get_columns_by_name()

    get_values_of_column()

    get_set_of_values_of_column()

    get_set_of_values_of_columns()

    Change_value_of_column()

    Change_value_of_columns()

    Change_values_of_column()
    
    new_column_by_separation()

    dropna()

    new_by_div()

    new_by_mult()

    new_by_add()

    new_by_sub()

    new_by_pow()

    new_by_log()

    new_by_sqrt()

    new_by_exp()

    new_by_sin()

    new_by_fft()

    new_by_ifft()

    Static methods
    --------------

    None
    """

    data_csv : str
    data : pd.DataFrame

#---------------------------------------------------------------------------------------------INIT

    def __init__(self , data_csv : str = "data_visualisation/data.csv") -> None:

        """
        Constructor that loads the data from the csv file into a DataFrame

        Parameters
        ----------
        data_csv : str
            file path of the csv file

        Returns
        -------
        None
        """
    
        self.data_csv = data_csv
        self.data = pd.DataFrame()
        self.data = pd.read_csv(data_csv)

        return None

#---------------------------------------------------------------------------------------------REPR

    def __repr__(self) -> str:

        """
        Returns a string representation of the class

        Parameters
        ----------
        None

        Returns
        -------
        repre : str
            string representation of the class
        """

        repre = f"""
        DataStructure object
        --------------------

        from file: {self.data_csv}

        Dataframe shape: {self.data.shape}

        Infos:

        {self.data.info()}

        First rows:

        {self.data.head()}

        Last rows:

        {self.data.tail()}
        """
            
        return repre

#----------------------------------------------------------------------------------------------QOF

    def get_data(self) -> pd.DataFrame:

        """
        Returns the data attribute of the class

        Parameters
        ----------
        None

        Returns
        -------
        self.data : pd.DataFrame
            DataFrame that contains the data from the csv file
        """

        return self.data

    def save_data(self , where : str = "") -> None:

        """
        Saves the data attribute of the class as a csv file

        Parameters
        ----------
        where : str
            file path where to save the csv file

        Returns
        -------
        None
        """

        self.data.to_csv(where + str(id(self)) + "_DataStructure.csv", index=False)

        return None

    def add_column(self , csv : str , corresponding_column : str) -> None:

        """
        Adds a column to the data attribute of the class

        Parameters
        ----------
        csv : str
            file path of the csv file to add

        corresponding_column : str
            name of the column that is common between the two csv files

        Returns
        -------
        None
        """

        new_data = pd.read_csv(csv)
        new_data = new_data.drop_duplicates(subset = corresponding_column)
        self.data = pd.merge(self.data, new_data, on = corresponding_column, how = 'inner')

        return None

    def add_columns(self , csvs : list[str] , corresponding_columns : list[str]) -> None:

        """
        Adds multiple columns to the data attribute of the class

        Parameters
        ----------
        csvs : list[str]
            file paths of the csv files to add

        corresponding_columns : list[str]
            names of the columns that are common between the two csv files

        Returns
        -------
        None
        """

        for i in range(len(csvs)):
            new_data = pd.read_csv(csvs[i])
            new_data = new_data.drop_duplicates(subset = corresponding_columns[i])
            self.data = pd.merge(self.data, new_data, on = corresponding_columns[i], how = 'inner')

        return None

    def drop_column(self , column : str) -> None:

        """
        Drops a column from the data attribute of the class
        
        Parameters
        ----------
        column : str
            name of the column to drop

        Returns
        -------
        None
        """
            
        self.data = self.data.drop(column, axis=1)
    
        return None

    def drop_columns(self , columns : list[str]) -> None:

        """
        Drops multiple columns from the data attribute of the class

        Parameters
        ----------
        columns : list[str]
            names of the columns to drop

        Returns
        -------
        None
        """

        self.data = self.data.drop(columns, axis=1)

        return None

    def drop_rows_by_column(self, column : str) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column : str
            name of the column to drop the rows of

        Returns
        -------
        None
        """
            
        self.data = self.data.dropna(subset=[column])
    
        return None
    
    def drop_rows_by_columns(self, columns : list[str]) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        columns : list[str]
            names of the columns to drop the rows of

        Returns
        -------
        None
        """

        self.data = self.data.dropna(subset=columns)

        return None

    def drop_rows_by_column_value(self, column : str , value : any) -> None:

        """
        Drops rows from the data attribute of the class
        
        Parameters
        ----------
        column : str
            name of the column to drop the rows of

        value : any
            value of the column to drop the rows of
        
        Returns
        -------
        None
        """
            
        self.data = self.data[self.data[column] != value]
    
        return None

    def drop_rows_by_column_values(self, column : str , values : list[any]) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column : str
            name of the column to drop the rows of

        values : list[any]
            values of the column to drop the rows of

        Returns
        -------
        None
        """
                    
        self.data = self.data[self.data[column].isin(values)]
        
        return None

    def drop_rows_by_columns_values(self, columns : list[str] , values : list[list[any]]):

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        columns : list[str]
            names of the columns to drop the rows of

        values : list[list[any]]
            values of the columns to drop the rows of

        Returns
        -------
        None
        """

        for i in range(len(columns)):
            self.data = self.data[self.data[columns[i]].isin(values[i])]

        return None

    def drop_rows_by_column_value_range(self, column : str , min : any , max : any) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column : str
            name of the column to drop the rows of

        min : any
            minimum value of the column to drop the rows of

        max : any
            maximum value of the column to drop the rows of

        Returns
        -------
        None
        """

        self.data = self.data[(self.data[column] > min) & (self.data[column] < max)]

        return None

    def drop_rows_by_column_value_range_and_bool(self, 
    column_of_bool : str, column_of_range : str , 
    min_t : any , max_t : any, min_f : any , max_f : any) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column_of_bool : str
            name of the column to drop the rows of

        column_of_range : str
            name of the column to drop the rows of  

        min_t : any
            minimum value of the column to drop the rows of

        max_t : any
            maximum value of the column to drop the rows of

        min_f : any
            minimum value of the column to drop the rows of

        max_f : any
            maximum value of the column to drop the rows of

        Returns
        -------
        None
        """

        self.data = self.data[
            (self.data[column_of_bool] == True) & 
            (self.data[column_of_range] > min_t) & 
            (self.data[column_of_range] < max_t) 
            | 
            (self.data[column_of_bool] == False) & 
            (self.data[column_of_range] > min_f) & 
            (self.data[column_of_range] < max_f)]

        return None

    def get_column(self , column : str) -> pd.DataFrame:

        """
        Parameters
        ----------
        column : str
            name of the column to get

        Returns
        -------
        pd.DataFrame
            the column asked
        """
            
        return self.data[column]

    def get_columns(self , columns : list[str]) -> pd.DataFrame:

        """
        Parameters
        ----------
        columns : list[str]
            names of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked
        """
                
        return self.data[columns]

    def get_columns_by_type(self , type : str) -> pd.DataFrame:

        """
        Parameters
        ----------
        type : str
            type of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked
        """
                
        return self.data.select_dtypes(include=[type])

    def get_columns_by_types(self , types : list[str]) -> pd.DataFrame:

        """
        Parameters
        ----------
        types : list[str]
            types of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked
        """
                    
        return self.data.select_dtypes(include=types)

    def get_columns_by_name(self , names : list[str]) -> pd.DataFrame:

        """
        Parameters
        ----------
        names : list[str]
            names of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked
        """

        return self.data[names]

    def get_values_of_column(self , column : str) -> np.ndarray:

        """
        Parameters
        ----------
        column : str
            name of the column to get the values of

        Returns
        -------
        np.ndarray
            the values of the column asked
        """
            
        return self.data[column].values

    def get_set_of_values_of_column(self , column : str) -> np.ndarray:

        """
        Parameters
        ----------
        column : str
            name of the column to get the values of

        Returns
        -------
        np.ndarray
            the set of values of the column asked
        """
                    
        return self.data[column].unique()

    def get_values_of_columns(self , columns : list[str]) -> np.ndarray:
            
        """
        Parameters
        ----------
        columns : list[str]
            names of the columns to get the values of

        Returns
        -------
        np.ndarray
            the values of the columns asked
        """
    
        return self.data[columns].values

    def get_set_of_values_of_column(self , column : list) -> np.ndarray:
    
        """
        Parameters
        ----------
        column : list
            name of the column to get the values of

        Returns
        -------
        np.ndarray
            the set of values of the column asked
        """

        
        return self.data[column].unique()

    def get_set_of_values_of_columns(self , columns : list[str]) -> np.ndarray:
                
        """
        Parameters
        ----------
        columns : list[str]
            names of the columns to get the values of

        Returns
        -------
        np.ndarray
            the set of values of the columns asked
        """
        
        return self.data[columns].unique()

    def Change_value_of_column(self , column : str , old_value : str , new_value : str):
            
        """
        Changes the value of a column
        
        Parameters
        ----------
        column : str
            name of the column to change the value of

        old_value : str
            old value of the column

        new_value : str
            new value of the column

        Returns
        -------

        None
        """

                
        self.data.loc[self.data[column] == old_value, column] = new_value
    
        return None

    def Change_value_of_columns(self , columns : list[str] , 
    old_values : list[str] , new_values : list[str]):
                    
        """
        Changes the value of a list of columns  
        
        Parameters
        ----------
        columns : list[str]
            names of the columns to change the value of

        old_values : list[str]
            old values of the columns

        new_values : list[str]
            new values of the columns

        Returns
        -------
        None
        """
                        
        for i in range(len(columns)):
            self.data.loc[self.data[columns[i]] == old_values[i], columns[i]] = new_values[i]
            
        return None

    def Change_values_of_column(self , column : str , 
    old_values : list[str] , new_values : list[str]):
        
        """
        Changes the values of a column

        Parameters
        ----------
        column : str
            name of the column to change the values of

        old_values : list[str]
            old values of the column

        new_values : list[str]
            new values of the column

        Returns
        -------
        None
        """

        for i in range(len(old_values)):
            self.data.loc[self.data[column] == old_values[i], column] = new_values[i]
        
        return None

    def new_column_by_separation(self , origin_column : str , new_column : str , 
    value_set1 : list[any] , value_set2 : list[any]) -> None:
                
        """
        Creates a new column by separating the values of an origin column

        Parameters
        ----------
        origin_column : str
            name of the origin column

        new_column : str
            name of the new column

        value_set1 : list[any]
            values of the new column that will be True

        value_set2 : list[any]
            values of the new column that will be False

        Returns
        -------
        None
        """
                        
        self.data[new_column] = self.data[origin_column].apply(
            lambda x: True if x in value_set1 else False if x in value_set2 else np.nan)
            
        return None

    def dropna(self, column : str) -> None:

        """
        Drops the rows with NaN values in a column

        Parameters
        ----------
        column : str
            name of the column to drop the NaN values of

        Returns
        -------
        None
        """

        self.data = self.data.dropna(subset=[column])

        return None

#--------------------------------------------------------------------------------------------MATH

    def new_by_div(self , col1 : str , col2 : str , new_col : str) -> None:

        """
        Creates a new column by dividing two columns

        Parameters
        ----------
        col1 : str
            name of the first column

        col2 : str
            name of the second column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """
            
        self.data[new_col] = self.data[col1] / self.data[col2]
    
        return None

    def new_by_mult(self , col1 : str , col2 : str , new_col : str) -> None:

        """
        Creates a new column by multiplying two columns

        Parameters
        ----------
        col1 : str
            name of the first column

        col2 : str
            name of the second column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """
                
        self.data[new_col] = self.data[col1] * self.data[col2]
        
        return None

    def new_by_add(self , col1 : str , col2 : str , new_col : str) -> None:

        """
        Creates a new column by adding two columns

        Parameters
        ----------
        col1 : str
            name of the first column

        col2 : str
            name of the second column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """
                        
        self.data[new_col] = self.data[col1] + self.data[col2]
                
        return None 

    def new_by_sub(self , col1 : str , col2 : str , new_col : str) -> None:

        """
        Creates a new column by subtracting two columns

        Parameters
        ----------
        col1 : str
            name of the first column

        col2 : str
            name of the second column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """

        self.data[new_col] = self.data[col1] - self.data[col2]
                
        return None 

    def new_by_pow(self , col1 : str , col2 : str , new_col : str) -> None:

        """
        Creates a new column by taking the power of two columns
        
        Parameters
        ----------
        col1 : str
            name of the first column

        col2 : str
            name of the second column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """
    
        self.data[new_col] = self.data[col1] ** self.data[col2]
                    
        return None

    def new_by_sqrt(self , col1 : str , new_col : str) -> None:

        """
        Creates a new column by taking the square root of the first column

        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """   

        self.data[new_col] = self.data[col1] ** 0.5
                            
        return None

    def new_by_log(self , col1 : str , new_col : str) -> None:

        """
        Creates a new column by taking the log of the first column

        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """

        self.data[new_col] = np.log(self.data[col1])
                                
        return None

    def new_by_exp(self , col1 : str , new_col : str) -> None:

        """
        Creates a new column by taking the exp of the first column

        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """

        self.data[new_col] = np.exp(self.data[col1])
                                    
        return None

    def new_by_sin(self , col1 : str , new_col : str) -> None:

        """
        Creates a new column by taking the sin of the first column
        
        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """

        self.data[new_col] = np.sin(self.data[col1])
                                        
        return None

    def new_by_fft(self , col1 : str , new_col : str) -> None:

        """
        Creates a new column by taking the fft of the first column
        
        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """
            
        self.data[new_col] = np.fft.fft(self.data[col1])
                                                
        return None

    def new_by_ifft(self , col1 : str , new_col : str) -> None:

        """
        Creates a new column by taking the ifft of the first column
        
        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        Returns
        -------
        None
        """

        self.data[new_col] = np.fft.ifft(self.data[col1])
                                                        
        return None
     

def make_more_data():

    """
    Creates the data for the visualisation
    """
    #get the data from xlsx by page
    data_2022 = pd.read_excel(
        "data_visualisation/Population_par_commune.xlsx", sheet_name="Population 2022")

    #get the data from xlsx by page
    data_2021 = pd.read_excel(
        "data_visualisation/Population_par_commune.xlsx", sheet_name="Population 2021")

    data_2022["Population variation"]  = (data_2022["Total"] - data_2021["Total"]
                                            )/data_2021["Total"]
    data_2022.dropna()
    data_2022.to_csv("data_visualisation/Population_par_commune.csv", index=False)

    INS = pd.read_excel("data_visualisation/INS.xlsx")
    INS.to_csv("data_visualisation/INS.csv", index=False)
    
    taxes = pd.read_excel("data_visualisation/taxes.xlsx")
    taxes.to_csv("data_visualisation/taxes.csv", index=False)


if __name__ == "__main__":

    data = DataStructure()
    #print all methods of data
    print(dir(data))

    data.add_column("data_visualisation/code-postaux.csv", "zipcode")
    data.add_column("data_visualisation/INS.csv", "zipcode")
    data.add_column("data_visualisation/Population_par_commune.csv", "INS")
    data.add_column("data_visualisation/taxes.csv", "INS")

    data.drop_columns(["Surface of the land", "Surface area of the plot of land", 
    "column_3", "column_4", "To rent", "Open fire", "coordonnees", "geom",
    "Terrace", "Area of the terrace", "INS", "Swimming pool", "Garden",
    "Area of the garden", "State of the building", "Fully equipped kitchen", 
    "Furnished", "Number of facades"])

    data.drop_rows_by_columns("Price")
    data.drop_rows_by_columns("Living Area")
    data.drop_rows_by_column_value_range_and_bool(
        "To sell" , "Price", 50_000 , 50_000_000, 200, 20_000)
    data.drop_rows_by_column_value_range("Living Area", 0, 20_000)
    data.dropna("Number of rooms")

    data.new_by_div("Price" , "Living Area" , "Price by M**2")

    data.drop_rows_by_column_value_range_and_bool(
        "To sell" , "Price by M**2", 200 , 20_000, 1, 1_000)


    old_types = ['Ferme', 'Appartement', 'Logementétudiant', 'Penthouse', 
                 'Appartementdeservice', 'Chalet', 'Maison', 'Rez-de-chaussée', 
                 'Maisondemaître', 'Autresbiens', 'Maisondecampagne', 'Loft', 
                 'Maisonbel-étage', 'Pavillon', 'Duplex', 'Triplex', 'Studio', 
                 'Immeublemixte', 'Bienexceptionnel', 'Château', 'Immeuble', 
                 'Manoir', 'Bungalow', 'Villa']

    new_types = ['Farm', 'Apartment', 'Student housing', 'Penthouse',
                 'Service apartment', 'Chalet', 'House', 'Ground floor',
                 'Master house', 'Other goods', 'Country house', 'Loft',
                 'Bel-etage house', 'Pavilion', 'Duplex', 'Triplex', 'Studio',
                 'Mixed building', 'Exceptional property', 'Castle', 'Building',
                 'Manor', 'Bungalow', 'Villa']

    appartments = ['Apartment', 'Student housing', 'Penthouse', 'Service apartment',
                    'Studio', 'Duplex', 'Triplex']

    houses = ['Farm', 'Chalet', 'House', 'Ground floor', 'Master house', 'Other goods',
                'Country house', 'Loft', 'Bel-etage house', 'Pavilion', 'Mixed building',
                'Exceptional property', 'Castle', 'Building', 'Manor', 'Bungalow', 'Villa']

    #divide new_types in two categories "house" or "appartment"


    data.Change_values_of_column("type", old_types, new_types)

    data.new_column_by_separation("type", "Appartment", appartments, houses)

    #data.save_data("data_visualisation/")
    

    

    print(data)