import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class add_column(SuperParent):
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

    