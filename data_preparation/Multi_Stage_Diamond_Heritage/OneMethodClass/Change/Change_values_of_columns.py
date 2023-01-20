import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Change_values_of_columns(SuperParent):

    def Change_values_of_column(self, column : str , 
    old_values : list[str] , new_values : list[str]) -> None:
        
        """
        Changes the values of a column

        Parameters
        ----------
        column : str
            name of the column to change the values of

        old_values : list[str]
            old values of the column

        new_values : list[str]
            new values of the column

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
            If old_values is not a list

        Exception
            If old_values is not a list of strings

        Exception
            If old_values are not in the column asked
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        if type(old_values) != list:
            raise Exception("old_values must be a list")

        for old_value in old_values:
            if type(old_value) != str:
                raise Exception("old_values must be a list of strings")

        for old_value in old_values:
            if old_value not in self.data[column].unique():
                raise Exception("old_values must be in the column asked")

        for i in range(len(old_values)):
            self.data.loc[self.data[column] == old_values[i], column] = new_values[i]
        
        return None
