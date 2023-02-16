#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/OneMethodClass/Drop")

#-P-IMPORT--------------------------------------------------------------------------------------
from drop_column import drop_column
from drop_columns import drop_columns
from drop_rows_by_column_value_range_and_bool import drop_rows_by_column_value_range_and_bool
from drop_rows_by_column_value_range import drop_rows_by_column_value_range
from drop_rows_by_column_value import drop_rows_by_column_value
from drop_rows_by_column_values import drop_rows_by_column_values
from drop_rows_by_column import drop_rows_by_column
from drop_rows_by_columns_values import drop_rows_by_columns_values
from drop_rows_by_columns import drop_rows_by_columns
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Drop(drop_column,
           drop_columns,
           drop_rows_by_column_value_range_and_bool,
           drop_rows_by_column_value_range,
           drop_rows_by_column_value,
           drop_rows_by_column_values,
           drop_rows_by_column,
           drop_rows_by_columns_values,
           drop_rows_by_columns):
    
     pass
