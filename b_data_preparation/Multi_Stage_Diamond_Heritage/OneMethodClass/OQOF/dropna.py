import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class dropna(SuperParent):

    def dropna(self, column : str) -> None:

        """
        Drops the rows with NaN values in a column

        Parameters
        ----------
        column : str
            name of the column to drop the NaN values of

        Returns
        -------
        None

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        self.data = self.data.dropna(subset=[column])

        return None
