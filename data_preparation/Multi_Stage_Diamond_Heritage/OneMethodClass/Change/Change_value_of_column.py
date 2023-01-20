import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Change_value_of_column(SuperParent):

    def Change_value_of_column(self, column : str , old_value : any , new_value : any) -> None:
            
        """
        Changes the value of a column
        
        Parameters
        ----------
        column : str
            name of the column to change the value of

        old_value : any
            old value of the column

        new_value : any
            new value of the column

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
            If old_value is not in the column asked  
        """

        if type(column) != str:
            raise Exception("column must be a string")

        if column not in self.data.columns:
            raise Exception("column must be in the data attribute of the class")

        if old_value not in self.data[column].unique():
            raise Exception("old_value must be in the column asked")
                
        self.data.loc[self.data[column] == old_value, column] = new_value
    
        return None