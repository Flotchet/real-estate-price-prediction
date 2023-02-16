import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class append_data(SuperParent):

    def append_data(self, new : pd.DataFrame) -> None:
                
        """
        Appends the data attribute of the class with a new DataFrame
        
        Parameters
        ----------
        new : pd.DataFrame
            new DataFrame to append
        
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
        
        self.data = self.data.append(new)
        
        return None

    