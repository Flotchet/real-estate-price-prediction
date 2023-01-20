import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_tsv(SuperParent):

    def new_data_set_tsv(self, tsv : str) -> None:
                                                
        """
        Creates a new data set
                                    
        Parameters
        ----------
        tsv : str
            name of the tsv file to create a new data set from
                                    
        Returns
        -------
        None
                                    
        Raises
        ------
        Exception
            If tsv is not a string
                                    
        Exception
            If tsv is not a tsv file
        """
                                    
        if type(tsv) != str:
            raise Exception("tsv must be a string")
                                    
        if tsv[-4:] != ".tsv":
            raise Exception("tsv must be a tsv file")
                                    
        self.Additional_data[tsv] = pd.read_csv(tsv, sep = "\t")
        self.Original_data[tsv] = pd.read_csv(tsv, sep = "\t")
                                    
        return None