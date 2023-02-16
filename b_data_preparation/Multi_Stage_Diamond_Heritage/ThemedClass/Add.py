#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/OneMethodClass/Add")

#-P-IMPORT--------------------------------------------------------------------------------------
from add_column import add_column
from add_columns import add_columns
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Add(add_column,
          add_columns):
    
    pass