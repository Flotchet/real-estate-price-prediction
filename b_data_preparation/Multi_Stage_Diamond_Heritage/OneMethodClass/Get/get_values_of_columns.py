import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import numpy as np
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class get_values_of_columns(SuperParent):

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

    