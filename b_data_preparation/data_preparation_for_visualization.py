#-I-DS------------------------------------------------------------------------------------------
import pandas as pd
#-P-Import--------------------------------------------------------------------------------------
from Multi_Stage_Diamond_Heritage.DiamondDataClass import DiamondDataClass as ddc
#-----------------------------------------------------------------------------------------------

#-F-DataPreparationForVisualization--------------------------------------------------------------
def data_assembler() -> None:
    """
    This function is used to assemble the data for the visualization.

    Parameters
    ----------
    None

    Returns
    -------
    None

    """

    #get the data from xlsx by page
    data_2022 = pd.read_excel(
        "data_visualisation/Population_par_commune.xlsx", sheet_name="Population 2022")

    #get the data from xlsx by page
    data_2021 = pd.read_excel(
        "data_visualisation/Population_par_commune.xlsx", sheet_name="Population 2021")

    data_2022["Population variation"]  = (data_2022["Total"] - data_2021["Total"]
                                            )/data_2021["Total"]
    data_2022.dropna()
    data_2022.to_csv("data_visualisation/Population_par_commune.csv", index=False)

    INS = pd.read_excel("data_visualisation/INS.xlsx")
    INS.to_csv("data_visualisation/INS.csv", index=False)
    
    taxes = pd.read_excel("data_visualisation/taxes.xlsx")
    taxes.to_csv("data_visualisation/taxes.csv", index=False)

    data = ddc()

    data.add_column("data_visualisation/code-postaux.csv", "zipcode")
    data.add_column("data_visualisation/INS.csv", "zipcode")
    data.add_column("data_visualisation/Population_par_commune.csv", "INS")
    data.add_column("data_visualisation/taxes.csv", "INS")

    data.drop_rows_by_columns("Price")
    data.drop_rows_by_columns("Living Area")
    data.drop_rows_by_column_value_range_and_bool(
        "To sell" , "Price", 50_000 , 50_000_000, 200, 20_000)
    data.drop_rows_by_column_value_range("Living Area", 0, 20_000)
    data.dropna("Number of rooms")

    data.new_by_div("Price" , "Living Area" , "Price by M**2")

    data.drop_rows_by_column_value_range_and_bool(
        "To sell" , "Price by M**2", 200 , 20_000, 1, 1_000)


    old_types = ['Ferme', 'Appartement', 'Logementétudiant', 'Penthouse', 
                 'Appartementdeservice', 'Chalet', 'Maison', 'Rez-de-chaussée', 
                 'Maisondemaître', 'Autresbiens', 'Maisondecampagne', 'Loft', 
                 'Maisonbel-étage', 'Pavillon', 'Duplex', 'Triplex', 'Studio', 
                 'Immeublemixte', 'Bienexceptionnel', 'Château', 'Immeuble', 
                 'Manoir', 'Bungalow', 'Villa']

    new_types = ['Farm', 'Apartment', 'Student housing', 'Penthouse',
                 'Service apartment', 'Chalet', 'House', 'Ground floor',
                 'Master house', 'Other goods', 'Country house', 'Loft',
                 'Bel-etage house', 'Pavilion', 'Duplex', 'Triplex', 'Studio',
                 'Mixed building', 'Exceptional property', 'Castle', 'Building',
                 'Manor', 'Bungalow', 'Villa']

    appartments = ['Apartment', 'Student housing', 'Penthouse', 'Service apartment',
                    'Studio', 'Duplex', 'Triplex']

    houses = ['Farm', 'Chalet', 'House', 'Ground floor', 'Master house', 'Other goods',
                'Country house', 'Loft', 'Bel-etage house', 'Pavilion', 'Mixed building',
                'Exceptional property', 'Castle', 'Building', 'Manor', 'Bungalow', 'Villa']

    data.Change_values_of_column("type", old_types, new_types)

    data.new_column_by_separation("type", "Appartment", appartments, houses)

    data.save_data()





if __name__ == "__main__":
    data_assembler()