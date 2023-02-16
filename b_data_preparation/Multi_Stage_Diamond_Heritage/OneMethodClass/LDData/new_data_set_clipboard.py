import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_clipboard(SuperParent):

    def new_data_set_clipboard(self) -> None:
                                                    
        """
        Creates a new data set
                                    
        Parameters
        ----------
        None
                                    
        Returns
        -------
        None
                                    
        Raises
        ------
        None
        """
                                    
        self.Additional_data["clipboard"] = pd.read_clipboard()
        self.Original_data["clipboard"] = pd.read_clipboard()
                                    
        return None

    