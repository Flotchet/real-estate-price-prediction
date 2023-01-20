import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_sas(SuperParent):

    def new_data_set_sas(self, sas : str) -> None:
                            
        """
        Creates a new data set
                    
        Parameters
        ----------
        sas : str
            name of the sas file to create a new data set from
                    
        Returns
        -------
        None
                    
        Raises
        ------
        Exception
            If sas is not a string
                    
        Exception
            If sas is not a sas file
        """
                    
        if type(sas) != str:
            raise Exception("sas must be a string")
                    
        if sas[-4:] != ".sas":
            raise Exception("sas must be a sas file")
                    
        self.Additional_data[sas] = pd.read_sas(sas)
        self.Original_data[sas] = pd.read_sas(sas)
                    
        return None
