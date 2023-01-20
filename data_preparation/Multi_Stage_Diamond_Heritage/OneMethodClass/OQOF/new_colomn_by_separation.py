import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import numpy as np
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_colomn_by_separation(SuperParent):

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

    