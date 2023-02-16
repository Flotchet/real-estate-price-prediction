import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class apply(SuperParent):

    def apply(self, func : callable  , columns : list[str]) -> None:
            
        """
        Applies a function to a list of columns
            
        Parameters
        ----------
        func : function
            function to apply
            
        columns : list[str]
            list of columns to apply the function to
            
        Returns
        -------
        None
            
        Raises
        ------
        Exception
            If func is not a function
            
        Exception
            If columns is not a list
            
        Exception
            If columns is not a list of strings
        """
            
        if type(func) != function:
            raise Exception("func must be a function")
            
        if type(columns) != list:
            raise Exception("columns must be a list")
            
        for column in columns:
            if type(column) != str:
                raise Exception("columns must be a list of strings")
            
        self.data[columns] = self.data[columns].apply(func)
            
        return None

    