#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/ThemedClass")

#-P-IMPORT--------------------------------------------------------------------------------------
from ThemedClass.Add import Add
from ThemedClass.Change import Change
from ThemedClass.Drop import Drop
from ThemedClass.Get import Get
from ThemedClass.Load import Load
from ThemedClass.Math import Math
from ThemedClass.QualityOfLife import QualityOfLife
from ThemedClass.Save import Save
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class DiamondDataClass(Add,
                       Change,
                       Drop,
                       Get,
                       Load,
                       Math,
                       QualityOfLife,
                       Save):

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

    pass