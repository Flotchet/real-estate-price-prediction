import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Change_value_of_columns(SuperParent):
    
    def Change_value_of_columns(self, columns : list[str] , 
    old_values : list[any] , new_values : list[any]) -> None:
                    
        """
        Changes the value of a list of columns  
        
        Parameters
        ----------
        columns : list[str]
            names of the columns to change the value of

        old_values : list[str]
            old values of the columns

        new_values : list[str]
            new values of the columns

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
            If old_values is not in the columns asked
        """

        if type(columns) != list:
            raise Exception("columns must be a list")

        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")

        for column in columns:
            if column not in self.data.columns:
                raise Exception("columns must be in the data attribute of the class")
                        
        for i in range(len(columns)):

            if old_values[i] not in self.data[columns[i]].unique():
                raise Exception("old_values must be in the columns asked")

            self.data.loc[self.data[columns[i]] == old_values[i], columns[i]] = new_values[i]
            
        return None
