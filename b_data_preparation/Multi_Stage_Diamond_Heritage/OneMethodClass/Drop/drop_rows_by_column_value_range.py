import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class drop_rows_by_column_value_range(SuperParent):

    def drop_rows_by_column_value_range(self, column : str , min : any , max : any) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column : str
            name of the column to drop the rows of

        min : any
            minimum value of the column to drop the rows of

        max : any
            maximum value of the column to drop the rows of

        Returns
        -------
        None

        Raises
        ------
        Exception
            If column is not a string

        Exception
            If column is not in the data attribute of the class

        Exception
            If min is not a number

        Exception
            If max is not a number

        Exception
            If min is greater than max

        Exception
            If min is equal to max
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        if type(min) != int and type(min) != float:
            raise Exception("min must be a number")

        if type(max) != int and type(max) != float:
            raise Exception("max must be a number")

        if min > max:
            raise Exception("min must be less than or equal to max")

        if min == max:
            raise Exception("min must be less than max")

        self.data = self.data[(self.data[column] > min) & (self.data[column] < max)]

        return None
