import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_feather(SuperParent):

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

    