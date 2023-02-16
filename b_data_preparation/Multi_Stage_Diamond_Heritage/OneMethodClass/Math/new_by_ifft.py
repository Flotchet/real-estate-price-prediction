import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import numpy as np
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_by_ifft(SuperParent):

    def new_by_ifft(self, col1 : str , new_col : str) -> None:

        """
        Creates a new column by taking the ifft of the first column
        
        Parameters
        ----------
        col1 : str
            name of the first column

        new_col : str
            name of the new column

        Returns
        -------
        None

        Raises
        ------
        Exception
            If col1 is not a string

        Exception
            If col1 is not in the data attribute of the class

        Exception
            If new_col is not a string
        """   

        if type(col1) != str:
            raise Exception("col1 must be a string")  

        if col1 not in self.data.columns:
            raise Exception("col1 must be in the data attribute of the class")

        if type(new_col) != str:
            raise Exception("new_col must be a string")

        self.data[new_col] = np.fft.ifft(self.data[col1])
                                                        
        return None

    