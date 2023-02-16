#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
from dataclasses import dataclass
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS

@dataclass
class SuperParent():

    """
    Class that extends the pandas DataFrame class

    Attributes
    ----------
    data_csv : str
        file path of the csv file

    Original_data : dict[str : pd.DataFrame]
        dictionary that contains the original data

    data : pd.DataFrame
        DataFrame that contains the data from the csv file

    Additional_data : dict[str : pd.DataFrame]
        dictionary that contains the additional data

    data_for_AI : pd.DataFrame
        DataFrame that contains the data for the AI

    data_for_V : pd.DataFrame
        DataFrame that contains the data for the visualisation
    """

    data_csv : str
    Original_data : dict[str : pd.DataFrame]
    data : pd.DataFrame
    Additional_data : dict[str : pd.DataFrame]
    data_for_AI : pd.DataFrame
    data_for_V : pd.DataFrame

#---------------------------------------------------------------------------------------------INIT

    def __init__(self, data_csv : str = "data.csv") -> None:

        """
        Constructor that loads the data from the csv file into a DataFrame

        Parameters
        ----------
        data_csv : str
            file path of the csv file

        Returns
        -------
        None

        Raises
        ------
        
        Exception
            If the file path is not a csv file

        Exception
            If data_csv is not a string
        """

        if type(data_csv) != str:
            raise Exception("data_csv must be a string")

        if data_csv[-4:] != ".csv":
            raise Exception("data_csv must be a csv file")
    
        self.data_csv = data_csv
        self.data = pd.DataFrame()
        self.data = pd.read_csv(data_csv)

        self.Original_data = {}
        self.Original_data[data_csv] = self.data.copy()

        self.Additional_data = {}

        return None

#---------------------------------------------------------------------------------------------REPR
    
    def __repr__(self) -> str:

        """
        Returns a string representation of the class

        Parameters
        ----------
        None

        Returns
        -------
        repre : str
            string representation of the class
        """

        repre = f"""
        DataFrameExtended object
        --------------------

        from file: {self.data_csv}

        Dataframe shape: {self.data.shape}

        Infos:

        {self.data.info()}

        First rows:

        {self.data.head()}

        Last rows:

        {self.data.tail()}
        """
            
        return repre