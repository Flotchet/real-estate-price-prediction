import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/SuperClass")
#-P-IMPORT--------------------------------------------------------------------------------------
from SuperParent import SuperParent
#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class new_data_set_sql(SuperParent):

    def new_data_set_sql(self, sql : str, con : str) -> None:
                
        """
        Creates a new data set
        
        Parameters
        ----------
        sql : str
            name of the sql table to create a new data set from
        
        con : str
            name of the connection to create a new data set from
        
        Returns
        -------
        None
        
        Raises
        ------
        Exception
            If sql is not a string
        
        Exception
            If con is not a string
        """
        
        if type(sql) != str:
            raise Exception("sql must be a string")
        
        if type(con) != str:
            raise Exception("con must be a string")
        
        self.Additional_data[sql] = pd.read_sql(sql, con)
        self.Original_data[sql] = pd.read_sql(sql, con)
        
        return None
