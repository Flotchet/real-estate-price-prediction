import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_sqlite(SuperParent):

    def new_data_set_sqlite(self, sqlite : str) -> None:
            
        """
        Creates a new data set
    
        Parameters
        ----------
        sqlite : str
            name of the sqlite file to create a new data set from
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If sqlite is not a string
    
        Exception
            If sqlite is not a sqlite file
        """
    
        if type(sqlite) != str:
            raise Exception("sqlite must be a string")
    
        if sqlite[-7:] != ".sqlite":
            raise Exception("sqlite must be a sqlite file")
    
        self.Additional_data[sqlite] = pd.read_sqlite(sqlite)
        self.Original_data[sqlite] = pd.read_sqlite(sqlite)
    
        return None

    