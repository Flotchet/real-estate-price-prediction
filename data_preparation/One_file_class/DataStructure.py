#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
from dataclasses import dataclass
#-I-QOF-----------------------------------------------------------------------------------------
import warnings
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS

@dataclass
class DataFrameExtended():

    """
    Class that extends the pandas DataFrame class

    Attributes
    ----------
    data_csv : str
        file path of the csv file

    Original_data : dict[str : pd.DataFrame]
        dictionary that contains the original data

    data : pd.DataFrame
        DataFrame that contains the data from the csv file

    Additional_data : dict[str : pd.DataFrame]
        dictionary that contains the additional data

    data_for_AI : pd.DataFrame
        DataFrame that contains the data for the AI

    data_for_V : pd.DataFrame
        DataFrame that contains the data for the visualisation
    """

    data_csv : str
    Original_data : dict[str : pd.DataFrame]
    data : pd.DataFrame
    Additional_data : dict[str : pd.DataFrame]
    data_for_AI : pd.DataFrame
    data_for_V : pd.DataFrame

#-------------------------------------------------------------------------------------------INIT

    def __init__(self, data_csv : str = "data.csv") -> None:

        """
        Constructor that loads the data from the csv file into a DataFrame

        Parameters
        ----------
        data_csv : str
            file path of the csv file

        Returns
        -------
        None

        Raises
        ------
        
        Exception
            If the file path is not a csv file

        Exception
            If data_csv is not a string
        """

        if type(data_csv) != str:
            raise Exception("data_csv must be a string")

        if data_csv[-4:] != ".csv":
            raise Exception("data_csv must be a csv file")
    
        self.data_csv = data_csv
        self.data = pd.DataFrame()
        self.data = pd.read_csv(data_csv)

        self.Original_data = {}
        self.Original_data[data_csv] = self.data.copy()

        self.Additional_data = {}

        return None

#-------------------------------------------------------------------------------------------REPR
    
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
        DataFrameExtended object
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

#--------------------------------------------------------------------------------------------QOF

#--------------------------------------------------------------------------------------------GET
    
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

        
    def get_column(self, column : str) -> pd.DataFrame:

        """
        Parameters
        ----------
        column : str
            name of the column to get

        Returns
        -------
        pd.DataFrame
            the column asked

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")
            
        return self.data[column]

    
    def get_columns(self, columns : list[str]) -> pd.DataFrame:

        """
        Parameters
        ----------
        columns : list[str]
            names of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")
                
        return self.data[columns]

    
    def get_columns_by_type(self, type : str) -> pd.DataFrame:

        """
        Parameters
        ----------
        type : str
            type of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked

        Raises
        ------
        Exception
            If type is not a string

        Exception
            If type is not a valid type

        Exception
            If type is not in the data attribute of the class
        """

        if type(type) != str:
            raise Exception("type must be a string")
            
        if type not in ["int64" , "float64" , "object" , "bool"]:
            raise Exception("type must be a valid type")

        if type not in self.data.dtypes:
            raise Exception("type must be in the data attribute of the class")
           
        return self.data.select_dtypes(include=[type])

    
    def get_columns_by_types(self, types : list[str]) -> pd.DataFrame:

        """
        Parameters
        ----------
        types : list[str]
            types of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked

        Raises
        ------
        Exception
            If types is not a list

        Exception
            If types is not a list of strings

        Exception
            If types is not a list of valid types

        Exception
            If types is not in the data attribute of the class
        """

        if type(types) != list:
            raise Exception("types must be a list")

        for type in types:
            if type(type) != str:
                raise Exception("types must be a list of strings")

        for type in types:
            if type not in ["int64" , "float64" , "object" , "bool"]:
                raise Exception("types must be a list of valid types")

        for type in types:
            if type not in self.data.dtypes:
                raise Exception("types must be in the data attribute of the class")
                    
        return self.data.select_dtypes(include=types)

    
    def get_columns_by_name(self, names : list[str]) -> pd.DataFrame:

        """
        Parameters
        ----------
        names : list[str]
            names of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked

        Raises
        ------
        Exception
            If names is not a list

        Exception
            If names is not a list of strings

        Exception
            If names is not in the data attribute of the class
        """

        if type(names) != list:
            raise Exception("names must be a list")

        for name in names:
            if type(name) != str:
                raise Exception("names must be a list of strings")

        for name in names:
            if name not in self.data.columns:
                raise Exception("names must be in the data attribute of the class")

        return self.data[names]

    
    def get_values_of_column(self, column : str) -> np.ndarray:

        """
        Parameters
        ----------
        column : str
            name of the column to get the values of

        Returns
        -------
        np.ndarray
            the values of the column asked

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")
            
        return self.data[column].values

    
    def get_set_of_values_of_column(self, column : str) -> np.ndarray:

        """
        Parameters
        ----------
        column : str
            name of the column to get the values of

        Returns
        -------
        np.ndarray
            the set of values of the column asked

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")
                    
        return self.data[column].unique()

    
    def get_values_of_columns(self, columns : list[str]) -> np.ndarray:
            
        """
        Parameters
        ----------
        columns : list[str]
            names of the columns to get the values of

        Returns
        -------
        np.ndarray
            the values of the columns asked

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")
    
        return self.data[columns].values

    
    def get_set_of_values_of_columns(self, columns : list[str]) -> np.ndarray:
                
        """
        Parameters
        ----------
        columns : list[str]
            names of the columns to get the values of

        Returns
        -------
        np.ndarray
            the set of values of the columns asked

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")
        
        return self.data[columns].unique()

#-------------------------------------------------------------------------------------------SAVE

    def save_data(self, where : str = "") -> None:

        """
        Saves the data attribute of the class as a csv file

        Parameters
        ----------
        where : str
            file path where to save the csv file

        Returns
        -------
        None

        Raises
        ------
        Exception
            If where is not a string  
        """

        if type(where) != str:
            raise Exception("where must be a string")

        self.data.to_csv(where + str(id(self)) + "_DataFrameExtended.csv", index=False)

        return None

#--------------------------------------------------------------------------------------------ADD
    
    def add_column(self, csv : str , corresponding_column : str) -> None:

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

        Raises
        ------
        Exception
            If csv is not a string

        Exception
            If corresponding_column is not a string

        Exception
            If corresponding_column is not in the data attribute of the class

        Exception
            If corresponding_column is not in the csv file
        """

        if type(csv) != str:
            raise Exception("csv must be a string")

        if type(corresponding_column) != str:
            raise Exception("corresponding_column must be a string")

        if corresponding_column not in self.data.columns:
            raise Exception("corresponding_column must be in the data attribute of the class")

        if csv[-4:] != ".csv":
            raise Exception("data_csv must be a csv file")

        new_data = pd.read_csv(csv)
        new_data = new_data.drop_duplicates(subset = corresponding_column)
        self.data = pd.merge(self.data, new_data, on = corresponding_column, how = 'inner')

        return None

    
    def add_columns(self, csvs : list[str] , corresponding_columns : list[str]) -> None:

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

        Raises
        ------
        Exception
            If csvs is not a list

        Exception
            If corresponding_columns is not a list

        Exception
            If csvs and corresponding_columns do not have the same length

        Exception
            If csvs is not a list of strings

        Exception
            If corresponding_columns is not a list of strings

        Exception
            If corresponding_columns is not in the data attribute of the class

        Exception
            If corresponding_columns is not in the csv file
        """

        if type(csvs) != list:
            raise Exception("csvs must be a list")

        if type(corresponding_columns) != list:
            raise Exception("corresponding_columns must be a list")

        if len(csvs) != len(corresponding_columns):
            raise Exception("csvs and corresponding_columns must have the same length")

        for csv in csvs:
            if type(csv) != str:
                raise Exception("csvs must be a list of strings")

        for corresponding_column in corresponding_columns:
            if type(corresponding_column) != str:
                raise Exception("corresponding_columns must be a list of strings")

        for corresponding_column in corresponding_columns:
            if corresponding_column not in self.data.columns:
                raise Exception("corresponding_columns must be in the data attribute of the class")

        for csv in csvs:
            if csv[-4:] != ".csv":
                raise Exception("data_csv must be a csv file")

        for i in range(len(csvs)):
            new_data = pd.read_csv(csvs[i])
            new_data = new_data.drop_duplicates(subset = corresponding_columns[i])
            self.data = pd.merge(self.data, new_data, on = corresponding_columns[i], how = 'inner')

        return None

#-------------------------------------------------------------------------------------------DROP
    
    def drop_column(self, column : str) -> None:

        """
        Drops a column from the data attribute of the class
        
        Parameters
        ----------
        column : str
            name of the column to drop

        Returns
        -------
        None

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")
            
        self.data = self.data.drop(column, axis=1)
    
        return None

    
    def drop_columns(self, columns : list[str]) -> None:

        """
        Drops multiple columns from the data attribute of the class

        Parameters
        ----------
        columns : list[str]
            names of the columns to drop

        Returns
        -------
        None

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")

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

        Raises
        ------
        Exception
            If column is not a string
        """

        if type(column) != str:
            raise Exception("column must be a string")
            
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

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")

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

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")
            
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

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")
                    
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

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class

        Exception
            If values is not a list

        Exception
            If values is not a list of lists
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")

        if type(values) != list:
            raise Exception("values must be a list")

        for value in values:
            if type(value) != list:
                raise Exception("values must be a list of lists")

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

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class

        Exception
            If min is not a number

        Exception
            If max is not a number

        Exception
            If min is greater than max

        Exception
            If min is equal to max
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        if type(min) != int and type(min) != float:
            raise Exception("min must be a number")

        if type(max) != int and type(max) != float:
            raise Exception("max must be a number")

        if min > max:
            raise Exception("min must be less than or equal to max")

        if min == max:
            raise Exception("min must be less than max")

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

        Raises
        ------
        Exception
            If column_of_bool is not a string

        Exception
            If column_of_bool is not in the data attribute of the class

        Exception
            If column_of_range is not a string

        Exception
            If column_of_range is not in the data attribute of the class

        Exception
            If min_t is greater than max_t

        Exception
            If min_t is equal to max_t

        Exception
            If min_f is greater than max_f

        Exception
            If min_f is equal to max_f
        """

        if type(column_of_bool) != str:
            raise Exception("column_of_bool must be a string")

        if column_of_bool not in self.data.columns:
            raise Exception("column_of_bool must be in the data attribute of the class")

        if type(column_of_range) != str:
            raise Exception("column_of_range must be a string")

        if column_of_range not in self.data.columns:
            raise Exception("column_of_range must be in the data attribute of the class")

        if min_t > max_t:
            raise Exception("min_t must be less than or equal to max_t")

        if min_t == max_t:
            raise Exception("min_t must be less than max_t")

        if min_f > max_f:
            raise Exception("min_f must be less than or equal to max_f")

        if min_f == max_f:
            raise Exception("min_f must be less than max_f")

        self.data = self.data[
            (self.data[column_of_bool] == True) & 
            (self.data[column_of_range] > min_t) & 
            (self.data[column_of_range] < max_t) 
            | 
            (self.data[column_of_bool] == False) & 
            (self.data[column_of_range] > min_f) & 
            (self.data[column_of_range] < max_f)]

        return None

#-----------------------------------------------------------------------------------------CHANGE
    
    def Change_value_of_column(self, column : str , old_value : any , new_value : any) -> None:
            
        """
        Changes the value of a column
        
        Parameters
        ----------
        column : str
            name of the column to change the value of

        old_value : any
            old value of the column

        new_value : any
            new value of the column

        Returns
        -------
        None

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class

        Exception
            If old_value is not in the column asked  
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        if old_value not in self.data[column].unique():
            raise Exception("old_value must be in the column asked")
                
        self.data.loc[self.data[column] == old_value, column] = new_value
    
        return None

    
    def Change_value_of_columns(self, columns : list[str] , 
    old_values : list[any] , new_values : list[any]) -> None:
                    
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

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class

        Exception
            If old_values is not in the columns asked
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")
                        
        for i in range(len(columns)):

            if old_values[i] not in self.data[columns[i]].unique():
                raise Exception("old_values must be in the columns asked")

            self.data.loc[self.data[columns[i]] == old_values[i], columns[i]] = new_values[i]
            
        return None

    
    def Change_values_of_column(self, column : str , 
    old_values : list[str] , new_values : list[str]) -> None:
        
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

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class

        Exception
            If old_values is not a list

        Exception
            If old_values is not a list of strings

        Exception
            If old_values are not in the column asked
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        if type(old_values) != list:
            raise Exception("old_values must be a list")

        for old_value in old_values:
            if type(old_value) != str:
                raise Exception("old_values must be a list of strings")

        for old_value in old_values:
            if old_value not in self.data[column].unique():
                raise Exception("old_values must be in the column asked")

        for i in range(len(old_values)):
            self.data.loc[self.data[column] == old_values[i], column] = new_values[i]
        
        return None

#--------------------------------------------------------------------------------------------QOF
    
    def new_column_by_separation(self, origin_column : str , new_column : str , 
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

        Raises
        ------
        Exception
            If origin_column is not a string

        Exception
            If origin_column is not in the data attribute of the class

        Exception
            If new_column is not a string

        Exception
            If value_set1 is not a list

        Exception
            If value_set2 is not a list
        """

        if type(origin_column) != str:
            raise Exception("origin_column must be a string")

        if origin_column not in self.data.columns:
            raise Exception("origin_column must be in the data attribute of the class")

        if type(new_column) != str:
            raise Exception("new_column must be a string")

        if type(value_set1) != list:
            raise Exception("value_set1 must be a list")

        if type(value_set2) != list:
            raise Exception("value_set2 must be a list")
                        
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

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        self.data = self.data.dropna(subset=[column])

        return None

    
    def concatenate_data(self, new : pd.DataFrame) -> None:
            
        """
        Concatanates the data attribute of the class with a new DataFrame
    
        Parameters
        ----------
        new : pd.DataFrame
            new DataFrame to concatanate
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If new is not a DataFrame
        """
    
        if type(new) != pd.DataFrame:
            raise Exception("new must be a DataFrame")
    
        self.data = pd.concat([self.data, new], axis=0)
    
        return None

    
    def append_data(self, new : pd.DataFrame) -> None:
                
        """
        Appends the data attribute of the class with a new DataFrame
        
        Parameters
        ----------
        new : pd.DataFrame
            new DataFrame to append
        
        Returns
        -------
        None
        
        Raises
        ------
        Exception
            If new is not a DataFrame
        """
        
        if type(new) != pd.DataFrame:
            raise Exception("new must be a DataFrame")
        
        self.data = self.data.append(new)
        
        return None

    
    def apply(self, func : callable  , columns : list[str]) -> None:
            
        """
        Applies a function to a list of columns
            
        Parameters
        ----------
        func : function
            function to apply
            
        columns : list[str]
            list of columns to apply the function to
            
        Returns
        -------
        None
            
        Raises
        ------
        Exception
            If func is not a function
            
        Exception
            If columns is not a list
            
        Exception
            If columns is not a list of strings
        """
            
        if type(func) != function:
            raise Exception("func must be a function")
            
        if type(columns) != list:
            raise Exception("columns must be a list")
            
        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")
            
        self.data[columns] = self.data[columns].apply(func)
            
        return None

    
    def switch(self, name : str) -> None:

        """
        Switches the data set 

        Parameters
        ----------
        name : str
            name of the data set to switch to from the Original_data dict

        Returns
        -------
        None

        Raises
        ------
        Exception
            If name is not a string

        Exception
            If the data set in the Original_data dict is not a DataFrame

        warning
            If the data set in the Original_data dict is empty

        """

        if type(name) != str:
            raise Exception("name must be a string")

        if name not in self.Additional_data:
            raise Exception("name must be in the Additional_data dict")

        if type(self.Additional_data[name]) != pd.DataFrame:
            raise Exception("the data set in the Additional_data dict must be a DataFrame")

        if self.Additional_data[name].empty:
            warnings.warn("the data set in the Additional_data is empty")

        self.Additional_data[self.data_csv] = self.data
        self.data_csv = name
        self.data = self.Additional_data[name]

        return None

    
    def reset(self) -> None:
            
        """
        Resets the data set to the Original_data set
    
        Parameters
        ----------
        None
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If the data set in the Original_data dict is not a DataFrame
    
        warning
            If the data set in the Original_data dict is empty
        """
        
        if type(self.Original_data[self.data_csv]) != pd.DataFrame:
            raise Exception("the data set in the Original_data dict must be a DataFrame")
        
        if self.Original_data[self.data_csv].empty:
            warnings.warn("the data set in the Original_data is empty")
        
        self.Additional_data[self.data_csv] = self.data
        self.data = self.Original_data[self.data_csv]
        
        return None 

        
    def reset_all(self) -> None:
                    
        """
        Resets all the data sets to the Original_data sets
            
        Parameters
        ----------
        None
            
        Returns
        -------
        None
            
        Raises
        ------
        Exception
            If the data set in the Original_data dict is not a DataFrame
            
        warning
            If the data set in the Original_data dict is empty
        """
            
        for key in self.Original_data:
            if type(self.Original_data[key]) != pd.DataFrame:
                raise Exception("the data set in the Original_data dict must be a DataFrame")
                
        if self.Original_data[key].empty:
                warnings.warn("the data set in the Original_data is empty")
            
        self.Additional_data = self.Original_data
        self.data = self.Original_data[self.data_csv]
            
        return None 


#---------------------------------------------------------------------------------------NEW-DATA

    
    def new_data_set_csv(self, csv : str) -> None:
            
        """
        Creates a new data set
    
        Parameters
            ----------
        csv : str
            name of the csv file to create a new data set from
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
                If csv is not a string
    
        Exception
            If csv is not a csv file
    

        """
    
        if type(csv) != str:
            raise Exception("csv must be a string")
    
        if csv[-4:] != ".csv":
            raise Exception("csv must be a csv file")

    
        self.Additional_data[csv] = pd.read_csv(csv)
        self.Original_data[csv] = pd.read_csv(csv)
    
        return None

    
    def new_data_set_excel(self, excels : str, page : str) -> None:
            
        """
        Creates a new data set
    
        Parameters
        ----------
        excels : str
            name of the excel file to create a new data set from
    
        page : str
            name of the page in the excel file to create a new data set from
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If excels is not a string
    
        Exception
            If excels is not a excel file
    
        Exception
            If page is not a string
    
        Exception
            If page is not in the excel file
        """
    
        if type(excels) != str:
            raise Exception("excels must be a string")
    
        if excels[-5:] != ".xlsx":
            raise Exception("excels must be a excel file")
    
        if page is not None:
            if type(page) != str:
                raise Exception("page must be a string")
    
            if page not in pd.ExcelFile(excels).sheet_names:
                raise Exception("page must be in the excel file")
    
        self.Additional_data[excels] = pd.read_excel(excels, sheet_name = page)
        self.Original_data[excels] = pd.read_excel(excels, sheet_name = page)
    
        return None

    
    def new_data_set_sql(self, sql : str, con : str) -> None:
                
        """
        Creates a new data set
        
        Parameters
        ----------
        sql : str
            name of the sql table to create a new data set from
        
        con : str
            name of the connection to create a new data set from
        
        Returns
        -------
        None
        
        Raises
        ------
        Exception
            If sql is not a string
        
        Exception
            If con is not a string
        """
        
        if type(sql) != str:
            raise Exception("sql must be a string")
        
        if type(con) != str:
            raise Exception("con must be a string")
        
        self.Additional_data[sql] = pd.read_sql(sql, con)
        self.Original_data[sql] = pd.read_sql(sql, con)
        
        return None

    
    def new_data_set_json(self, json : str) -> None:
                        
        """
        Creates a new data set
                
        Parameters
        ----------
        json : str
            name of the json file to create a new data set from
                
        Returns
        -------
        None
                
        Raises
        ------
        Exception
            If json is not a string
                
        Exception
            If json is not a json file
        """
                
        if type(json) != str:
            raise Exception("json must be a string")
                
        if json[-5:] != ".json":
            raise Exception("json must be a json file")
                
        self.Additional_data[json] = pd.read_json(json)
        self.Original_data[json] = pd.read_json(json)
                
        return None

    
    def new_data_set_clipboard(self) -> None:
                                                    
        """
        Creates a new data set
                                    
        Parameters
        ----------
        None
                                    
        Returns
        -------
        None
                                    
        Raises
        ------
        None
        """
                                    
        self.Additional_data["clipboard"] = pd.read_clipboard()
        self.Original_data["clipboard"] = pd.read_clipboard()
                                    
        return None

    
    def new_data_set_html(self, html : str) -> None:
                                                            
        """
        Creates a new data set
                                                
        Parameters
        ----------
        html : str
            name of the html file to create a new data set from
                                                
        Returns
        -------
        None
                                                
        Raises
        ------
        Exception
            If html is not a string
                                                
        Exception
            If html is not a html file
        """
                                                
        if type(html) != str:
            raise Exception("html must be a string")
                                                
        if html[-5:] != ".html":
            raise Exception("html must be a html file")
                                                
        self.Additional_data[html] = pd.read_html(html)
        self.Original_data[html] = pd.read_html(html)
                                                
        return None

    
    def new_data_set_pickle(self, pickle : str) -> None:
                                                                    
        """
        Creates a new data set
                                                            
        Parameters
        ----------
        pickle : str
            name of the pickle file to create a new data set from
                                                            
        Returns
        -------
        None
                                                            
        Raises
        ------
        Exception
            If pickle is not a string
                                                            
        Exception
            If pickle is not a pickle file
        """
                                                            
        if type(pickle) != str:
            raise Exception("pickle must be a string")
                                                            
        if pickle[-7:] != ".pickle" and pickle[-4:] != ".pkl":
            raise Exception("pickle must be a pickle file")
                                                            
        self.Additional_data[pickle] = pd.read_pickle(pickle)
        self.Original_data[pickle] = pd.read_pickle(pickle)
                                                            
        return None

            
    def new_data_set_sqlite(self, sqlite : str) -> None:
            
        """
        Creates a new data set
    
        Parameters
        ----------
        sqlite : str
            name of the sqlite file to create a new data set from
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If sqlite is not a string
    
        Exception
            If sqlite is not a sqlite file
        """
    
        if type(sqlite) != str:
            raise Exception("sqlite must be a string")
    
        if sqlite[-7:] != ".sqlite":
            raise Exception("sqlite must be a sqlite file")
    
        self.Additional_data[sqlite] = pd.read_sqlite(sqlite)
        self.Original_data[sqlite] = pd.read_sqlite(sqlite)
    
        return None

    
    def new_data_set_stata(self, stata : str) -> None:
            
        """
        Creates a new data set
    
        Parameters
        ----------
        stata : str
            name of the stata file to create a new data set from
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If stata is not a string
    
        Exception
            If stata is not a stata file
        """
    
        if type(stata) != str:
            raise Exception("stata must be a string")
    
        if stata[-6:] != ".stata" and stata[-4:] != ".dta":
            raise Exception("stata must be a stata file")
    
        self.Additional_data[stata] = pd.read_stata(stata)
        self.Original_data[stata] = pd.read_stata(stata)
    
        return None

    
    def new_data_set_feather(self, feather : str) -> None:
                
        """
        Creates a new data set
        
        Parameters
        ----------
        feather : str
            name of the feather file to create a new data set from
        
        Returns
        -------
        None
        
        Raises
        ------
        Exception
            If feather is not a string
        
        Exception
            If feather is not a feather file
        """
        
        if type(feather) != str:
            raise Exception("feather must be a string")
        
        if feather[-8:] != ".feather":
            raise Exception("feather must be a feather file")
        
        self.Additional_data[feather] = pd.read_feather(feather)
        self.Original_data[feather] = pd.read_feather(feather)
        
        return None

    
    def new_data_set_parquet(self, parquet : str) -> None:
                    
        """
        Creates a new data set
            
        Parameters
        ----------
        parquet : str
            name of the parquet file to create a new data set from
            
        Returns
        -------
        None
            
        Raises
        ------
        Exception
            If parquet is not a string
            
        Exception
            If parquet is not a parquet file
        """
            
        if type(parquet) != str:
            raise Exception("parquet must be a string")
            
        if parquet[-8:] != ".parquet":
            raise Exception("parquet must be a parquet file")
            
        self.Additional_data[parquet] = pd.read_parquet(parquet)
        self.Original_data[parquet] = pd.read_parquet(parquet)
            
        return None

    
    def new_data_set_sas(self, sas : str) -> None:
                            
        """
        Creates a new data set
                    
        Parameters
        ----------
        sas : str
            name of the sas file to create a new data set from
                    
        Returns
        -------
        None
                    
        Raises
        ------
        Exception
            If sas is not a string
                    
        Exception
            If sas is not a sas file
        """
                    
        if type(sas) != str:
            raise Exception("sas must be a string")
                    
        if sas[-4:] != ".sas":
            raise Exception("sas must be a sas file")
                    
        self.Additional_data[sas] = pd.read_sas(sas)
        self.Original_data[sas] = pd.read_sas(sas)
                    
        return None

    
    def new_data_set_spss(self, spss : str) -> None:
                                    
        """
        Creates a new data set
                            
        Parameters
        ----------
        spss : str
            name of the spss file to create a new data set from
                            
        Returns
        -------
        None
                            
        Raises
        ------
        Exception
            If spss is not a string
                            
        Exception
            If spss is not a spss file
        """
                            
        if type(spss) != str:
            raise Exception("spss must be a string")
                            
        if spss[-5:] != ".spss":
            raise Exception("spss must be a spss file")
                            
        self.Additional_data[spss] = pd.read_spss(spss)
        self.Original_data[spss] = pd.read_spss(spss)
                            
        return None

    
    def new_data_set_tsv(self, tsv : str) -> None:
                                                
        """
        Creates a new data set
                                    
        Parameters
        ----------
        tsv : str
            name of the tsv file to create a new data set from
                                    
        Returns
        -------
        None
                                    
        Raises
        ------
        Exception
            If tsv is not a string
                                    
        Exception
            If tsv is not a tsv file
        """
                                    
        if type(tsv) != str:
            raise Exception("tsv must be a string")
                                    
        if tsv[-4:] != ".tsv":
            raise Exception("tsv must be a tsv file")
                                    
        self.Additional_data[tsv] = pd.read_csv(tsv, sep = "\t")
        self.Original_data[tsv] = pd.read_csv(tsv, sep = "\t")
                                    
        return None

    
    def new_data_set_text(self, text : str) -> None:
                                                            
        """
        Creates a new data set
                                            
        Parameters
        ----------
        text : str
            name of the text file to create a new data set from
                                            
        Returns
        -------
        None
                                            
        Raises
        ------
        Exception
            If text is not a string
                                            
        Exception
            If text is not a text file
        """
                                            
        if type(text) != str:
            raise Exception("text must be a string")
                                            
        if text[-4:] != ".txt":
            raise Exception("text must be a text file")
                                            
        self.Additional_data[text] = pd.read_csv(text, sep = "\t")
        self.Original_data[text] = pd.read_csv(text, sep = "\t")
                                            
        return None 

    
    def new_data_set(self, file : str = None) -> None:

        """
        Creates a new data set from an file of type
        .csv, .dta, .feather, .parquet, .sas, .spss, .tsv
        .pickle, .txt, .json, .html, .sqlite, .stata, .pkl

        if None create from clipboard

        Parameters
        ----------
        file : str
            name of the file to create a new data set from

        Returns
        -------
        None

        Raises
        ------
        Exception
            If file is not a string or None
            
        Exception
            If file is not a file of type
            .csv, .dta, .feather, .parquet, .sas, .spss, .tsv
            .pickle, .txt, .json, .html, .sqlite, .stata, .pkl
        """
            
        if type(file) != str and file != None:
            raise Exception("file must be a string or None")
    
        if file != None:
    
            if file[-4:] == ".csv":
                self.new_data_set_csv(file)
    
            elif file[-4:] == ".dta":
                self.new_data_set_stata(file)
    
            elif file[-8:] == ".feather":
                self.new_data_set_feather(file)
    
            elif file[-8:] == ".parquet":
                self.new_data_set_parquet(file)
    
            elif file[-4:] == ".sas":
                self.new_data_set_sas(file)
    
            elif file[-5:] == ".spss":
                self.new_data_set_spss(file)
    
            elif file[-4:] == ".tsv":
                self.new_data_set_tsv(file)
    
            elif file[-7:] == ".pickle":
                self.new_data_set_pickle(file)

            elif file[-4:] == ".pkl":
                self.new_data_set_pickle(file)
    
            elif file[-4:] == ".txt":
                self.new_data_set_text(file)
    
            elif file[-5:] == ".json":
                self.new_data_set_json(file)
    
            elif file[-5:] == ".html":
                self.new_data_set_html(file)
    
            elif file[-7:] == ".sqlite":
                self.new_data_set_sqlite(file)
    
            elif file[-6:] == ".stata":
                self.new_data_set_stata(file)
    
            else:
                raise Exception("file must be a file of type .csv, .dta, .feather, .parquet, .sas, .spss, .tsv .pickle, .txt, .json, .html, .sqlite, .stata, .pkl")
    
        else:
            self.new_data_set_clipboard()
    
        return None 


#--------------------------------------------------------------------------------------------MATH

    
    def new_by_div(self, col1 : str , col2 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If col2 is not a string

        Exception
            If col2 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """

        if type(col1) != str:
            raise Exception("col1 must be a string")

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(col2) != str:
            raise Exception("col2 must be a string")

        if col2 not in self.data.columns:
            raise Exception("col2 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")
            
        self.data[new_col] = self.data[col1] / self.data[col2]
    
        return None

    
    def new_by_mult(self, col1 : str , col2 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If col2 is not a string

        Exception
            If col2 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """

        if type(col1) != str:
            raise Exception("col1 must be a string")

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(col2) != str:
            raise Exception("col2 must be a string")

        if col2 not in self.data.columns:
            raise Exception("col2 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")
                
        self.data[new_col] = self.data[col1] * self.data[col2]
        
        return None

    
    def new_by_add(self, col1 : str , col2 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If col2 is not a string

        Exception
            If col2 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """

        if type(col1) != str:
            raise Exception("col1 must be a string")

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(col2) != str:
            raise Exception("col2 must be a string")

        if col2 not in self.data.columns:
            raise Exception("col2 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")
                        
        self.data[new_col] = self.data[col1] + self.data[col2]
                
        return None 

    
    def new_by_sub(self, col1 : str , col2 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If col2 is not a string

        Exception
            If col2 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """

        if type(col1) != str:
            raise Exception("col1 must be a string")

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(col2) != str:
            raise Exception("col2 must be a string")

        if col2 not in self.data.columns:
            raise Exception("col2 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")

        self.data[new_col] = self.data[col1] - self.data[col2]
                
        return None 

    
    def new_by_pow_col(self, col1 : str , col2 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If col2 is not a string

        Exception
            If col2 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """

        if type(col1) != str:
            raise Exception("col1 must be a string")

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(col2) != str:
            raise Exception("col2 must be a string")

        if col2 not in self.data.columns:
            raise Exception("col2 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")
    
        self.data[new_col] = self.data[col1] ** self.data[col2]
                    
        return None

    
    def new_by_pow(self, col1 : str , new_col : str , power : float) -> None:

        """
        Creates a new column by taking the power of a column

        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        power : float
            power to raise the column to

        Returns
        -------
        None

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """

        if type(col1) != str:
            raise Exception("col1 must be a string")

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")
        
        self.data[new_col] = self.data[col1] ** power
                    
        return None

    
    def new_by_sqrt(self, col1 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """   

        if type(col1) != str:
            raise Exception("col1 must be a string")  

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")

        self.data[new_col] = self.data[col1] ** 0.5
                            
        return None

    
    def new_by_log(self, col1 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """   

        if type(col1) != str:
            raise Exception("col1 must be a string")  

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")

        self.data[new_col] = np.log(self.data[col1])
                                
        return None

    
    def new_by_exp(self, col1 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """   

        if type(col1) != str:
            raise Exception("col1 must be a string")  

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")

        self.data[new_col] = np.exp(self.data[col1])
                                    
        return None

    
    def new_by_sin(self, col1 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """   

        if type(col1) != str:
            raise Exception("col1 must be a string")  

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")

        self.data[new_col] = np.sin(self.data[col1])
                                        
        return None

    
    def new_by_fft(self, col1 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """   

        if type(col1) != str:
            raise Exception("col1 must be a string")  

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")
            
        self.data[new_col] = np.fft.fft(self.data[col1])
                                                
        return None

    
    def new_by_ifft(self, col1 : str , new_col : str) -> None:

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

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """   

        if type(col1) != str:
            raise Exception("col1 must be a string")  

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")

        self.data[new_col] = np.fft.ifft(self.data[col1])
                                                        
        return None

    
    def new_by_func(self, func : callable , new_col : str) -> None:
            
        """
        Creates a new column by taking the func of the first column
            
        Parameters
        ----------
        func : function
            function to apply to the data
    
        new_col : str
            name of the new column
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If func is not a function
    
        Exception
            If new_col is not a string
        """   
    
        if type(func) != function:
            raise Exception("func must be a function")  
    
        if type(new_col) != str:
            raise Exception("new_col must be a string")
    
        self.data[new_col] = func(self.data)
                                                                    
        return None

    
    def new_by_func_on_col(self, func : callable , col1 : str , new_col : str) -> None:
                    
        """
        Creates a new column by taking the func of the first column
                
        Parameters
        ----------
        func : function
            function to apply to the data
        
        col1 : str
            name of the first column
        
        new_col : str
            name of the new column
        
        Returns
        -------
        None
        
        Raises
        ------
        Exception
            If func is not a function
        
        Exception
            If col1 is not a string
        
        Exception
            If col1 is not in the data attribute of the class
        
        Exception
            If new_col is not a string
        """   
        
        if type(func) != function:
            raise Exception("func must be a function")  
        
        if type(col1) != str:
            raise Exception("col1 must be a string")  
        
        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")
        
        if type(new_col) != str:
            raise Exception("new_col must be a string")
        
        self.data[new_col] = func(self.data[col1])
                                                                            
        return None






def make_more_data() -> None:

    """
    Creates the data for the visualisation

    Parameters
    ----------
    None

    Returns
    -------
    None
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

    data = DataFrameExtended()
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
    data.save_data("data_visualisation/", "data_visualisation/")
    

    

    print(data)