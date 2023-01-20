import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class add_columns(SuperParent):

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
