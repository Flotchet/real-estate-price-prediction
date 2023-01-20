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
class reset_all(SuperParent):

    def reset_all(self) -> None:
                    
        """
        Resets all the data sets to the Original_data sets
            
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
            
        for key in self.Original_data:
            if type(self.Original_data[key]) != pd.DataFrame:
                raise Exception("the data set in the Original_data dict must be a DataFrame")
                
        if self.Original_data[key].empty:
                warnings.warn("the data set in the Original_data is empty")
            
        self.Additional_data = self.Original_data
        self.data = self.Original_data[self.data_csv].copy()
            
        return None 

