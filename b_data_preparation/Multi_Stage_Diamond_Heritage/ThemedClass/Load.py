#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/OneMethodClass/LDData")

#-P-IMPORT--------------------------------------------------------------------------------------
from new_data_set_clipboard import new_data_set_clipboard
from new_data_set_csv import new_data_set_csv
from new_data_set_excel import new_data_set_excel
from new_data_set_feather import new_data_set_feather
from new_data_set_html import new_data_set_html
from new_data_set_json import new_data_set_json
from new_data_set_parquet import new_data_set_parquet
from new_data_set_pickle import new_data_set_pickle
from new_data_set_sas import new_data_set_sas
from new_data_set_spss import new_data_set_spss
from new_data_set_sql import new_data_set_sql
from new_data_set_sqlite import new_data_set_sqlite
from new_data_set_stata import new_data_set_stata
from new_data_set_text import new_data_set_text
from new_data_set_tsv import new_data_set_tsv
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Load(new_data_set_clipboard,
          new_data_set_csv,
          new_data_set_excel,
          new_data_set_feather,
          new_data_set_html,
          new_data_set_json,
          new_data_set_parquet,
          new_data_set_pickle,
          new_data_set_sas,
          new_data_set_spss,
          new_data_set_sql,
          new_data_set_sqlite,
          new_data_set_stata,
          new_data_set_text,
          new_data_set_tsv):

    def new_data_set(self, file : str = None) -> None:

        """
        Creates a new data set from an file of type
        .csv, .dta, .feather, .parquet, .sas, .spss, .tsv
        .pickle, .txt, .json, .html, .sqlite, .stata, .pkl

        if None create from clipboard

        Parameters
        ----------
        file : str
            name of the file to create a new data set from

        Returns
        -------
        None

        Raises
        ------
        Exception
            If file is not a string or None
            
        Exception
            If file is not a file of type
            .csv, .dta, .feather, .parquet, .sas, .spss, .tsv
            .pickle, .txt, .json, .html, .sqlite, .stata, .pkl
        """
            
        if type(file) != str and file != None:
            raise Exception("file must be a string or None")
    
        if file != None:
    
            if file[-4:] == ".csv":
                self.new_data_set_csv(file)
    
            elif file[-4:] == ".dta":
                self.new_data_set_stata(file)
    
            elif file[-8:] == ".feather":
                self.new_data_set_feather(file)
    
            elif file[-8:] == ".parquet":
                self.new_data_set_parquet(file)
    
            elif file[-4:] == ".sas":
                self.new_data_set_sas(file)
    
            elif file[-5:] == ".spss":
                self.new_data_set_spss(file)
    
            elif file[-4:] == ".tsv":
                self.new_data_set_tsv(file)
    
            elif file[-7:] == ".pickle":
                self.new_data_set_pickle(file)

            elif file[-4:] == ".pkl":
                self.new_data_set_pickle(file)
    
            elif file[-4:] == ".txt":
                self.new_data_set_text(file)
    
            elif file[-5:] == ".json":
                self.new_data_set_json(file)
    
            elif file[-5:] == ".html":
                self.new_data_set_html(file)
    
            elif file[-7:] == ".sqlite":
                self.new_data_set_sqlite(file)
    
            elif file[-6:] == ".stata":
                self.new_data_set_stata(file)
    
            else:
                raise Exception("file must be a file of type .csv, .dta, .feather, .parquet, .sas, .spss, .tsv .pickle, .txt, .json, .html, .sqlite, .stata, .pkl")
    
        else:
            self.new_data_set_clipboard()
    
        return None 

