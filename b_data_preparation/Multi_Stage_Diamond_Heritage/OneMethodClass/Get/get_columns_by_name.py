import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class get_columns_by_name(SuperParent):

    def get_columns_by_name(self, names : list[str]) -> pd.DataFrame:

        """
        Parameters
        ----------
        names : list[str]
            names of the columns to get

        Returns
        -------
        pd.DataFrame
            the columns asked

        Raises
        ------
        Exception
            If names is not a list

        Exception
            If names is not a list of strings

        Exception
            If names is not in the data attribute of the class
        """

        if type(names) != list:
            raise Exception("names must be a list")

        for name in names:
            if type(name) != str:
                raise Exception("names must be a list of strings")

        for name in names:
            if name not in self.data.columns:
                raise Exception("names must be in the data attribute of the class")

        return self.data[names]

    