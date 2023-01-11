import pandas as pd
import numpy as np

class immoweb_data():

    """
    Class that loads the data from the csv file into 
    a DataFrame and allows to add, drop and modify columns and rows
    """

#---------------------------------------------------------------------------------------------INIT

    def __init__(self , data_csv : str = "data_visualisation/data.csv"):

        """
        Constructor that loads the data from the csv file into a DataFrame
        :param data_csv: file path of the csv file
        """
    
        self.data_csv = data_csv
        self.data = pd.DataFrame()
        self.data = pd.read_csv(data_csv)

        return None

#---------------------------------------------------------------------------------------------REPR

    def __repr__(self):

        """
        String representation of the class that shows the file path, shape of the dataframe, head and tail of the dataframe
        :return: string representation of the class
        """

        repre = f"""
        immoweb_data object
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

    def get_data(self):

        """
        :return: the data attribute of the class
        """

        return self.data

    def save_data(self , where : str = ""):

        """
        Saves the data attribute of the class into a csv file
        :param where: file path where to save the csv file
        :return: None
        """

        self.data.to_csv(where + str(id(self)) + "_immoweb_data.csv", index=False)

        return None

    def add_column(self , csv : str , corresponding_column : str):

        """
        Adds a column to the data attribute of the class
        :param csv: file path of the csv file to add
        :param corresponding_column: name of the column that is common between the two csv files
        """

        new_data = pd.read_csv(csv)
        new_data = new_data.drop_duplicates(subset = corresponding_column)
        self.data = pd.merge(self.data, new_data, on = corresponding_column, how = 'inner')

        return None

    def add_columns(self , csvs : list[str] , corresponding_columns : list[str]):

        """
        Adds multiple columns to the data attribute of the class
        :param csvs: file paths of the csv files to add
        :param corresponding_columns: names of the columns that are common between the two csv files
        """

        for i in range(len(csvs)):
            new_data = pd.read_csv(csvs[i])
            new_data = new_data.drop_duplicates(subset = corresponding_columns[i])
            self.data = pd.merge(self.data, new_data, on = corresponding_columns[i], how = 'inner')

        return None

    def drop_column(self , column : str):

        """
        Drops a column from the data attribute of the class
        :param column: name of the column to drop
        """
            
        self.data = self.data.drop(column, axis=1)
    
        return None

    def drop_columns(self , columns : list[str]):

        """
        Drops multiple columns from the data attribute of the class
        :param columns: names of the columns to drop
        """

        self.data = self.data.drop(columns, axis=1)

        return None

    def drop_rows_by_collumns(self, column : str):

        """
        Drops rows from the data attribute of the class
        :param column: name of the column to drop the rows of
        """
            
        self.data = self.data.dropna(subset=[column])
    
        return None
    
    def drop_rows_by_collumns(self, columns : list[str]):

        """
        Drops rows from the data attribute of the class
        :param columns: names of the columns to drop the rows of
        """

        self.data = self.data.dropna(subset=columns)

        return None

    def drop_rows_by_collumn_value(self, column : str , value : any):

        """
        Drops rows from the data attribute of the class
        :param column: name of the column to drop the rows of
        :param value: value of the column to drop the rows of
        """
            
        self.data = self.data[self.data[column] != value]
    
        return None

    def dropna(self, column : str):

        """
        Drops rows from the data attribute of the class
        :param column: name of the column to drop the rows of
        """

        self.data = self.data.dropna(subset=[column])

        return None

    def drop_rows_by_collumn_values(self, column : str , values : list[any]):

        """
        Drops rows from the data attribute of the class
        :param column: name of the column to drop the rows of
        :param values: values of the column to drop the rows of
        """
                    
        self.data = self.data[self.data[column].isin(values)]
        
        return None

    def drop_rows_by_collumns_values(self, columns : list[str] , values : list[list[any]]):

        """
        Drops rows from the data attribute of the class
        :param columns: names of the columns to drop the rows of
        :param values: values of the columns to drop the rows of
        """

        for i in range(len(columns)):
            self.data = self.data[self.data[columns[i]].isin(values[i])]

        return None

    def drop_rows_by_collumn_value_range(self, column : str , min : any , max : any):

        """
        Drops rows from the data attribute of the class
        :param column: name of the column to drop the rows of
        :param min: minimum value of the column to drop the rows of
        :param max: maximum value of the column to drop the rows of
        """

        self.data = self.data[(self.data[column] > min) & (self.data[column] < max)]

        return None

    def drop_rows_by_collumn_value_range_and_bool(self, 
    column_of_bool : str, column_of_range : str , 
    min_t : any , max_t : any, min_f : any , max_f : any):

        """
        Drops rows from the data attribute of the class
        :param column_of_bool: name of the column to drop the rows of
        :param column_of_range: name of the column to drop the rows of
        :param min_t: minimum value of the column to drop the rows of
        :param max_t: maximum value of the column to drop the rows of
        :param min_f: minimum value of the column to drop the rows of
        :param max_f: maximum value of the column to drop the rows of
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

    def get_column(self , column : str):

        """
        :param column: name of the column to get
        :return: the column asked
        """
            
        return self.data[column]

    def get_columns(self , columns : list[str]):

        """
        :param columns: names of the columns to get
        :return: the columns asked
        """
                
        return self.data[columns]

    def get_columns_by_type(self , type : str):

        """
        :param type: type of the columns to get
        :return: the columns asked
        """
                
        return self.data.select_dtypes(include=[type])

    def get_columns_by_types(self , types : list):

        """
        :param types: types of the columns to get
        :return: the columns asked
        """
                    
        return self.data.select_dtypes(include=types)

    def get_columns_by_name(self , names : list[str]):

        """
        :param names: names of the columns to get
        :return: the columns asked
        """

        return self.data[names]

    def get_values_of_collumn(self , column : str):

        """
        :param column: name of the column to get the values of
        :return: the values of the column asked
        """
            
        return self.data[column].values

    def get_set_of_values_of_collumn(self , column : str):

        """
        :param column: name of the column to get the values of
        :return: the set of values of the column asked
        """
                    
        return self.data[column].unique()

    def get_values_of_collumns(self , columns : list[str]):
            
        """
        :param columns: names of the columns to get the values of
        :return: the values of the columns asked
        """
    
        return self.data[columns].values

    def get_set_of_values_of_collumns(self , columns : list[str]):
                
        """
        :param columns: names of the columns to get the values of
        :return: the set of values of the columns asked
        """
        
        return self.data[columns].unique()

    def Change_value_of_collumn(self , column : str , old_value : str , new_value : str):
            
        """
        Changes the value of a column
        :param column: name of the column to change the value of
        :param old_value: old value of the column
        :param new_value: new value of the column
        """
                
        self.data.loc[self.data[column] == old_value, column] = new_value
    
        return None

    def Change_value_of_collumns(self , columns : list[str] , 
    old_values : list[str] , new_values : list[str]):
                    
        """
        Changes the value of a column
        :param columns: names of the columns to change the value of
        :param old_values: old values of the columns
        :param new_values: new values of the columns
        """
                        
        for i in range(len(columns)):
            self.data.loc[self.data[columns[i]] == old_values[i], columns[i]] = new_values[i]
            
        return None

    def Change_values_of_collumn(self , column : str , 
    old_values : list[str] , new_values : list[str]):
        
        """
        Changes a list of values of a column
        :param column: name of the column to change the value of
        :param old_values: old values of the column
        :param new_values: new values of the column
        """

        for i in range(len(old_values)):
            self.data.loc[self.data[column] == old_values[i], column] = new_values[i]
        
        return None

    def new_collumn_by_separation(self , origin_column : str , new_column : str , 
    value_set1 : list[any] , value_set2 : list[any]):
                
        """
        Creates a new column by separating the values of an other column
        :param origin_column: name of the column to separate
        :param new_column: name of the new column
        :param value_set1: set of values to put in the new column
        :param value_set2: set of values to put in the new column
        """
                        
        self.data[new_column] = self.data[origin_column].apply(
            lambda x: True if x in value_set1 else False if x in value_set2 else np.nan)
            
        return None



#--------------------------------------------------------------------------------------------MATH

    def new_by_div(self , col1 : str , col2 : str , new_col : str):

        """
        Creates a new column by dividing two columns
        :param col1: name of the first column
        :param col2: name of the second column
        :param new_col: name of the new column
        """
            
        self.data[new_col] = self.data[col1] / self.data[col2]
    
        return None

    def new_by_mult(self , col1 : str , col2 : str , new_col : str):

        """
        Creates a new column by multiplying two columns
        :param col1: name of the first column
        :param col2: name of the second column
        :param new_col: name of the new column
        """
                
        self.data[new_col] = self.data[col1] * self.data[col2]
        
        return None

    def new_by_add(self , col1 : str , col2 : str , new_col : str):

        """
        Creates a new column by adding two columns
        :param col1: name of the first column
        :param col2: name of the second column
        :param new_col: name of the new column
        """
                        
        self.data[new_col] = self.data[col1] + self.data[col2]
                
        return None 

    def new_by_sub(self , col1 : str , col2 : str , new_col : str):

        """
        Creates a new column by subtracting two columns
        :param col1: name of the first column
        :param col2: name of the second column
        :param new_col: name of the new column
        """

        self.data[new_col] = self.data[col1] - self.data[col2]
                
        return None 

    def new_by_pow(self , col1 : str , col2 : str , new_col : str):

        """
        Creates a new column by raising the first column to the power of the second column
        :param col1: name of the first column
        :param col2: name of the second column
        :param new_col: name of the new column
        """
    
        self.data[new_col] = self.data[col1] ** self.data[col2]
                    
        return None

    def new_by_sqrt(self , col1 : str , new_col : str):

        """
        Creates a new column by taking the square root of the first column
        :param col1: name of the first column
        :param new_col: name of the new column
        """

        self.data[new_col] = self.data[col1] ** 0.5
                            
        return None

    def new_by_log(self , col1 : str , new_col : str):

        """
        Creates a new column by taking the log of the first column
        :param col1: name of the first column
        :param new_col: name of the new column
        """

        self.data[new_col] = np.log(self.data[col1])
                                
        return None

    def new_by_exp(self , col1 : str , new_col : str):

        """
        Creates a new column by taking the exp of the first column
        :param col1: name of the first column
        :param new_col: name of the new column
        """

        self.data[new_col] = np.exp(self.data[col1])
                                    
        return None

    def new_by_sin(self , col1 : str , new_col : str):

        """
        Creates a new column by taking the sin of the first column
        :param col1: name of the first column
        :param new_col: name of the new column
        """

        self.data[new_col] = np.sin(self.data[col1])
                                        
        return None

    def new_by_fft(self , col1 : str , new_col : str):

        """
        Creates a new column by taking the fft of the first column
        :param col1: name of the first column
        :param new_col: name of the new column
        """

            
        self.data[new_col] = np.fft.fft(self.data[col1])
                                                
        return None

    def new_by_ifft(self , col1 : str , new_col : str):

        """
        Creates a new column by taking the ifft of the first column
        :param col1: name of the first column
        :param new_col: name of the new column
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

    data = immoweb_data()

    data.add_column("data_visualisation/code-postaux.csv", "zipcode")
    data.add_column("data_visualisation/INS.csv", "zipcode")
    data.add_column("data_visualisation/Population_par_commune.csv", "INS")
    data.add_column("data_visualisation/taxes.csv", "INS")

    data.drop_columns(["Surface of the land", "Surface area of the plot of land", 
    "column_3", "column_4", "To rent", "Open fire", "coordonnees", "geom",
    "Terrace", "Area of the terrace", "INS", "Swimming pool", "Garden",
    "Area of the garden", "State of the building", "Fully equipped kitchen", 
    "Furnished", "Number of facades"])

    data.drop_rows_by_collumns("Price")
    data.drop_rows_by_collumns("Living Area")
    data.drop_rows_by_collumn_value_range_and_bool(
        "To sell" , "Price", 50_000 , 50_000_000, 200, 20_000)
    data.drop_rows_by_collumn_value_range("Living Area", 0, 20_000)
    data.dropna("Number of rooms")

    data.new_by_div("Price" , "Living Area" , "Price by M**2")

    data.drop_rows_by_collumn_value_range_and_bool(
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


    data.Change_values_of_collumn("type", old_types, new_types)

    data.new_collumn_by_separation("type", "Appartment", appartments, houses)

    data.save_data("data_visualisation/")
    

    

    print(data)