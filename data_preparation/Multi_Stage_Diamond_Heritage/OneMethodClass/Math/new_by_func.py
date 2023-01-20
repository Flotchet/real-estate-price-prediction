import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_by_func(SuperParent):

    def new_by_func(self, func : callable , new_col : str) -> None:
            
        """
        Creates a new column by taking the func of the first column
            
        Parameters
        ----------
        func : function
            function to apply to the data
    
        new_col : str
            name of the new column
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If func is not a function
    
        Exception
            If new_col is not a string
        """   
    
        if type(func) != function:
            raise Exception("func must be a function")  
    
        if type(new_col) != str:
            raise Exception("new_col must be a string")
    
        self.data[new_col] = func(self.data)
                                                                    
        return None

    