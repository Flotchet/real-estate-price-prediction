import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-I-QOF-----------------------------------------------------------------------------------------
import warnings
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class switch(SuperParent):

    def switch(self, name : str) -> None:

        """
        Switches the data set 

        Parameters
        ----------
        name : str
            name of the data set to switch to from the Original_data dict

        Returns
        -------
        None

        Raises
        ------
        Exception
            If name is not a string

        Exception
            If the data set in the Original_data dict is not a DataFrame

        warning
            If the data set in the Original_data dict is empty

        """

        if type(name) != str:
            raise Exception("name must be a string")

        if name not in self.Additional_data:
            raise Exception("name must be in the Additional_data dict")

        if type(self.Additional_data[name]) != pd.DataFrame:
            raise Exception("the data set in the Additional_data dict must be a DataFrame")

        if self.Additional_data[name].empty:
            warnings.warn("the data set in the Additional_data is empty")

        self.Additional_data[self.data_csv] = self.data
        self.data_csv = name
        self.data = self.Additional_data[name].copy()

        return None

    