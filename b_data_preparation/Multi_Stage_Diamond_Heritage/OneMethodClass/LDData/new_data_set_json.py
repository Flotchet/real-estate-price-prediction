import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_json(SuperParent):

    def new_data_set_json(self, json : str) -> None:
                        
        """
        Creates a new data set
                
        Parameters
        ----------
        json : str
            name of the json file to create a new data set from
                
        Returns
        -------
        None
                
        Raises
        ------
        Exception
            If json is not a string
                
        Exception
            If json is not a json file
        """
                
        if type(json) != str:
            raise Exception("json must be a string")
                
        if json[-5:] != ".json":
            raise Exception("json must be a json file")
                
        self.Additional_data[json] = pd.read_json(json)
        self.Original_data[json] = pd.read_json(json)
                
        return None

    