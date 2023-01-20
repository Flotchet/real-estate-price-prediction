#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/OneMethodClass/Change")

#-P-IMPORT--------------------------------------------------------------------------------------
from Change_value_of_column import Change_value_of_column
from Change_value_of_columns import Change_value_of_columns
from Change_values_of_columns import Change_values_of_columns
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Change(Change_value_of_column,
             Change_value_of_columns,
             Change_values_of_columns):
        
    pass