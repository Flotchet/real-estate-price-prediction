import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class get_columns_by_type(SuperParent):

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
