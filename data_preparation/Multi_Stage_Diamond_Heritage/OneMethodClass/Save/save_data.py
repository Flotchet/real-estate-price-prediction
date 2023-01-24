import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class save_data(SuperParent):

    def save_data(self, where : str = "") -> None:

        """
        Saves the data attribute of the class as a csv file

        Parameters
        ----------
        where : str
            file path where to save the csv file

        Returns
        -------
        None

        Raises
        ------
        Exception
            If where is not a string  
        """

        if type(where) != str:
            raise Exception("where must be a string")

        self.data.to_csv(where + str(id(self)) + "_DataFrameExtended.csv", index=False)

        return None
