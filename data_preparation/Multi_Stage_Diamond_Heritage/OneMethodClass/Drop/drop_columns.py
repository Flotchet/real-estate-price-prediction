import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class drop_columns(SuperParent):

    def drop_columns(self, columns : list[str]) -> None:

        """
        Drops multiple columns from the data attribute of the class

        Parameters
        ----------
        columns : list[str]
            names of the columns to drop

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
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")

        self.data = self.data.drop(columns, axis=1)

        return None

    