import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_text(SuperParent):

    def new_data_set_text(self, text : str) -> None:
                                                            
        """
        Creates a new data set
                                            
        Parameters
        ----------
        text : str
            name of the text file to create a new data set from
                                            
        Returns
        -------
        None
                                            
        Raises
        ------
        Exception
            If text is not a string
                                            
        Exception
            If text is not a text file
        """
                                            
        if type(text) != str:
            raise Exception("text must be a string")
                                            
        if text[-4:] != ".txt":
            raise Exception("text must be a text file")
                                            
        self.Additional_data[text] = pd.read_csv(text, sep = "\t")
        self.Original_data[text] = pd.read_csv(text, sep = "\t")
                                            
        return None 

    