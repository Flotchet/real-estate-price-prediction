import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_excel(SuperParent):

    def new_data_set_excel(self, excels : str, page : str) -> None:
            
        """
        Creates a new data set
    
        Parameters
        ----------
        excels : str
            name of the excel file to create a new data set from
    
        page : str
            name of the page in the excel file to create a new data set from
    
        Returns
        -------
        None
    
        Raises
        ------
        Exception
            If excels is not a string
    
        Exception
            If excels is not a excel file
    
        Exception
            If page is not a string
    
        Exception
            If page is not in the excel file
        """
    
        if type(excels) != str:
            raise Exception("excels must be a string")
    
        if excels[-5:] != ".xlsx":
            raise Exception("excels must be a excel file")
    
        if page is not None:
            if type(page) != str:
                raise Exception("page must be a string")
    
            if page not in pd.ExcelFile(excels).sheet_names:
                raise Exception("page must be in the excel file")
    
        self.Additional_data[excels] = pd.read_excel(excels, sheet_name = page)
        self.Original_data[excels] = pd.read_excel(excels, sheet_name = page)
    
        return None
