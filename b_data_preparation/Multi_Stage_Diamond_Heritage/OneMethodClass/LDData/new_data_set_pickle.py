import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_pickle(SuperParent):

    def new_data_set_pickle(self, pickle : str) -> None:
                                                                    
        """
        Creates a new data set
                                                            
        Parameters
        ----------
        pickle : str
            name of the pickle file to create a new data set from
                                                            
        Returns
        -------
        None
                                                            
        Raises
        ------
        Exception
            If pickle is not a string
                                                            
        Exception
            If pickle is not a pickle file
        """
                                                            
        if type(pickle) != str:
            raise Exception("pickle must be a string")
                                                            
        if pickle[-7:] != ".pickle" and pickle[-4:] != ".pkl":
            raise Exception("pickle must be a pickle file")
                                                            
        self.Additional_data[pickle] = pd.read_pickle(pickle)
        self.Original_data[pickle] = pd.read_pickle(pickle)
                                                            
        return None

     