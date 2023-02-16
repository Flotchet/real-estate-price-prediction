import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_csv(SuperParent):

    def new_data_set_csv(self, csv : str) -> None:
            
        """
        Creates a new data set
    
        Parameters
            ----------
        csv : str
            name of the csv file to create a new data set from
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
                If csv is not a string
    
        Exception
            If csv is not a csv file
    

        """
    
        if type(csv) != str:
            raise Exception("csv must be a string")
    
        if csv[-4:] != ".csv":
            raise Exception("csv must be a csv file")

    
        self.Additional_data[csv] = pd.read_csv(csv)
        self.Original_data[csv] = pd.read_csv(csv)
    
        return None

    