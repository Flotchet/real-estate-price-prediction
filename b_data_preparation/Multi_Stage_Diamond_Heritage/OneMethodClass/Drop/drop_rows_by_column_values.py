import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class drop_rows_by_column_values(SuperParent):

    def drop_rows_by_column_values(self, column : str , values : list[any]) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column : str
            name of the column to drop the rows of

        values : list[any]
            values of the column to drop the rows of

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
                    
        self.data = self.data[self.data[column].isin(values)]
        
        return None

