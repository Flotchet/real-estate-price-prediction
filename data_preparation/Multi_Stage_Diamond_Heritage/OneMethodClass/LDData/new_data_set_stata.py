import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_stata(SuperParent):

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
