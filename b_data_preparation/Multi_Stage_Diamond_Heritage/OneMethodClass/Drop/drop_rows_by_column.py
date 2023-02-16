import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class drop_rows_by_column(SuperParent):

    def drop_rows_by_column(self, column : str) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column : str
            name of the column to drop the rows of

        Returns
        -------
        None

        Raises
        ------
        Exception
            If column is not a string
        """

        if type(column) != str:
            raise Exception("column must be a string")
            
        self.data = self.data.dropna(subset=[column])
    
        return None
