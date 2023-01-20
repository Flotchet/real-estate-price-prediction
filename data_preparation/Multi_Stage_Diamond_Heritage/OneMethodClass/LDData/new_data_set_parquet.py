import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_parquet(SuperParent):

    def new_data_set_parquet(self, parquet : str) -> None:
                    
        """
        Creates a new data set
            
        Parameters
        ----------
        parquet : str
            name of the parquet file to create a new data set from
            
        Returns
        -------
        None
            
        Raises
        ------
        Exception
            If parquet is not a string
            
        Exception
            If parquet is not a parquet file
        """
            
        if type(parquet) != str:
            raise Exception("parquet must be a string")
            
        if parquet[-8:] != ".parquet":
            raise Exception("parquet must be a parquet file")
            
        self.Additional_data[parquet] = pd.read_parquet(parquet)
        self.Original_data[parquet] = pd.read_parquet(parquet)
            
        return None

    