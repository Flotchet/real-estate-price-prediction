import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class drop_rows_by_column_value_range_and_bool(SuperParent):

    def drop_rows_by_column_value_range_and_bool(self, 
    column_of_bool : str, column_of_range : str , 
    min_t : any , max_t : any, min_f : any , max_f : any) -> None:

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        column_of_bool : str
            name of the column to drop the rows of

        column_of_range : str
            name of the column to drop the rows of  

        min_t : any
            minimum value of the column to drop the rows of

        max_t : any
            maximum value of the column to drop the rows of

        min_f : any
            minimum value of the column to drop the rows of

        max_f : any
            maximum value of the column to drop the rows of

        Returns
        -------
        None

        Raises
        ------
        Exception
            If column_of_bool is not a string

        Exception
            If column_of_bool is not in the data attribute of the class

        Exception
            If column_of_range is not a string

        Exception
            If column_of_range is not in the data attribute of the class

        Exception
            If min_t is greater than max_t

        Exception
            If min_t is equal to max_t

        Exception
            If min_f is greater than max_f

        Exception
            If min_f is equal to max_f
        """

        if type(column_of_bool) != str:
            raise Exception("column_of_bool must be a string")

        if column_of_bool not in self.data.columns:
            raise Exception("column_of_bool must be in the data attribute of the class")

        if type(column_of_range) != str:
            raise Exception("column_of_range must be a string")

        if column_of_range not in self.data.columns:
            raise Exception("column_of_range must be in the data attribute of the class")

        if min_t > max_t:
            raise Exception("min_t must be less than or equal to max_t")

        if min_t == max_t:
            raise Exception("min_t must be less than max_t")

        if min_f > max_f:
            raise Exception("min_f must be less than or equal to max_f")

        if min_f == max_f:
            raise Exception("min_f must be less than max_f")

        self.data = self.data[
            (self.data[column_of_bool] == True) & 
            (self.data[column_of_range] > min_t) & 
            (self.data[column_of_range] < max_t) 
            | 
            (self.data[column_of_bool] == False) & 
            (self.data[column_of_range] > min_f) & 
            (self.data[column_of_range] < max_f)]

        return None
