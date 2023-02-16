import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_html(SuperParent):

    def new_data_set_html(self, html : str) -> None:
                                                            
        """
        Creates a new data set
                                                
        Parameters
        ----------
        html : str
            name of the html file to create a new data set from
                                                
        Returns
        -------
        None
                                                
        Raises
        ------
        Exception
            If html is not a string
                                                
        Exception
            If html is not a html file
        """
                                                
        if type(html) != str:
            raise Exception("html must be a string")
                                                
        if html[-5:] != ".html":
            raise Exception("html must be a html file")
                                                
        self.Additional_data[html] = pd.read_html(html)
        self.Original_data[html] = pd.read_html(html)
                                                
        return None

    