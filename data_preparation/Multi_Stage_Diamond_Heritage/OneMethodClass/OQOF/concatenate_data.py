import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class concatenate_data(SuperParent):

    def concatenate_data(self, new : pd.DataFrame) -> None:
            
        """
        Concatanates the data attribute of the class with a new DataFrame
    
        Parameters
        ----------
        new : pd.DataFrame
            new DataFrame to concatanate
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If new is not a DataFrame
        """
    
        if type(new) != pd.DataFrame:
            raise Exception("new must be a DataFrame")
    
        self.data = pd.concat([self.data, new], axis=0)
    
        return None

    