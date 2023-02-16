import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class get_columns_by_types(SuperParent):

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
