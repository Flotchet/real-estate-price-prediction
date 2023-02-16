import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class get_data(SuperParent):

    def get_data(self) -> pd.DataFrame:

        """
        Returns the data attribute of the class

        Parameters
        ----------
        None

        Returns
        -------
        self.data : pd.DataFrame
            DataFrame that contains the data from the csv file
        """

        return self.data

    