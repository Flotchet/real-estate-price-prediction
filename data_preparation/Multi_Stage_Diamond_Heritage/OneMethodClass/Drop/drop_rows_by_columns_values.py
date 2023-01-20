import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class drop_rows_by_columns_values(SuperParent):

    def drop_rows_by_columns_values(self, columns : list[str] , values : list[list[any]]):

        """
        Drops rows from the data attribute of the class

        Parameters
        ----------
        columns : list[str]
            names of the columns to drop the rows of

        values : list[list[any]]
            values of the columns to drop the rows of

        Returns
        -------
        None

        Raises
        ------
        Exception
            If columns is not a list

        Exception
            If columns is not a list of strings

        Exception
            If columns is not in the data attribute of the class

        Exception
            If values is not a list

        Exception
            If values is not a list of lists
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")

        if type(values) != list:
            raise Exception("values must be a list")

        for value in values:
            if type(value) != list:
                raise Exception("values must be a list of lists")

        for i in range(len(columns)):
            self.data = self.data[self.data[columns[i]].isin(values[i])]

        return None

    