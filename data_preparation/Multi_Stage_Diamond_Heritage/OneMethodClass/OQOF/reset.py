import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-I-QOF-----------------------------------------------------------------------------------------
import warnings
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class reset(SuperParent):

    def reset(self) -> None:
            
        """
        Resets the data set to the Original_data set
    
        Parameters
        ----------
        None
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If the data set in the Original_data dict is not a DataFrame
    
        warning
            If the data set in the Original_data dict is empty
        """
        
        if type(self.Original_data[self.data_csv]) != pd.DataFrame:
            raise Exception("the data set in the Original_data dict must be a DataFrame")
        
        if self.Original_data[self.data_csv].empty:
            warnings.warn("the data set in the Original_data is empty")
        
        self.Additional_data[self.data_csv] = self.data
        self.data = self.Original_data[self.data_csv].copy()
        
        return None 
