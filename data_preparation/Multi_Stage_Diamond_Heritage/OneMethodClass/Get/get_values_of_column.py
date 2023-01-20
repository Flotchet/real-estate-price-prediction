import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import numpy as np
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class get_values_of_column(SuperParent):

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

    