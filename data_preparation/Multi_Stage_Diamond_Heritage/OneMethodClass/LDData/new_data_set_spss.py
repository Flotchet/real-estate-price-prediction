import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_spss(SuperParent):

    def new_data_set_spss(self, spss : str) -> None:
                                    
        """
        Creates a new data set
                            
        Parameters
        ----------
        spss : str
            name of the spss file to create a new data set from
                            
        Returns
        -------
        None
                            
        Raises
        ------
        Exception
            If spss is not a string
                            
        Exception
            If spss is not a spss file
        """
                            
        if type(spss) != str:
            raise Exception("spss must be a string")
                            
        if spss[-5:] != ".spss":
            raise Exception("spss must be a spss file")
                            
        self.Additional_data[spss] = pd.read_spss(spss)
        self.Original_data[spss] = pd.read_spss(spss)
                            
        return None

    