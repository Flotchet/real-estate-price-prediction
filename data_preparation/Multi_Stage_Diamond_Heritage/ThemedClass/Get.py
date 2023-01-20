#import path
import sys
sys.path.append("data_preparation/Multi_Stage_Diamond_Heritage/OneMethodClass/Get")

#-P-IMPORT--------------------------------------------------------------------------------------
from get_column import get_column
from get_columns_by_name import get_columns_by_name
from get_columns_by_type import get_columns_by_type
from get_columns_by_types import get_columns_by_types
from get_columns import get_columns
from get_data import get_data
from get_set_of_values_of_column import get_set_of_values_of_column
from get_set_of_values_of_columns import get_set_of_values_of_columns
from get_values_of_column import get_values_of_column
from get_values_of_columns import get_values_of_columns
#-----------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------CLASS
class Get(get_column,
          get_columns_by_name,
          get_columns_by_type,
          get_columns_by_types,
          get_columns,
          get_data,
          get_set_of_values_of_column,
          get_set_of_values_of_columns,
          get_values_of_column,
          get_values_of_columns):

    pass