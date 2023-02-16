#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-P-Import--------------------------------------------------------------------------------------
from DiamondDataClass import DiamondDataClass as ddc
#-----------------------------------------------------------------------------------------------

#-F-DataPreparationForVisualization--------------------------------------------------------------
def data_assembler() -> None:
    """
    This function is used to assemble the data for regression.

    Parameters
    ----------
    None

    Returns
    -------
    None
    
    """

    data = ddc()

    data.drop_rows_by_columns("Price")
    data.drop_rows_by_columns("Living Area")
    data.drop_rows_by_column_value_range_and_bool(
        "To sell" , "Price", 50_000 , 50_000_000, 200, 20_000)
    data.drop_rows_by_column_value_range("Living Area", 9, 1000)
    data.dropna("Number of rooms")

    data.new_by_div("Price" , "Living Area" , "Price by M**2")

    data.drop_rows_by_column_value_range_and_bool(
        "To sell" , "Price by M**2", 200 , 20_000, 1, 1_000)

    data.save_data()



if __name__ == "__main__":
    data_assembler()