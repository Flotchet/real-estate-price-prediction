import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
#from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error

import pickle

from tqdm import tqdm

from itertools import product

import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from warnings import warn

def region_add(data_dict : dict[str : pd.DataFrame]) -> dict[str : pd.DataFrame]:

    """
    This function add the region to the data
    
    Parameters
    ----------
    data_dict : dict[str : pd.DataFrame]
        The dictionary that contains the data
        
    Returns
    -------
    dict[str : pd.DataFrame]
        The dictionary that contains the data with the region added
        
    Raise
    -----
    TypeError
        If the data_dict is not a dict[str : pd.DataFrame]
        
    Exception
        If the data_dict does not contains the keys
        'Province du Brabant wallon'
        'Province du Brabant flamand'
        'Province d\'Anvers'
        'Province du Brabant flamand 2
        'Province de Limbourg'
        'Province de Liège'
        'Province de Namur'
        'Province du Hainaut 1'
        'Province de Luxembourg'
        'Province du Hainaut 2'
        'Province de Flandre-Occidentale'
        'Province de Flandre-Orientale'
    """
        
        #check if the data_dict is a dict[str : pd.DataFrame]
    if not isinstance(data_dict, dict):
        raise TypeError("The data_dict must be a dict[str : pd.DataFrame]")
        
    #check if the data_dict contains the keys
    if not all(key in data_dict for key in ['Province du Brabant wallon',
                                            'Province du Brabant flamand',
                                            'Province d\'Anvers',
                                            'Province du Brabant flamand 2',
                                            'Province de Limbourg',
                                            'Province de Liège',
                                            'Province de Namur',
                                            'Province du Hainaut 1',
                                            'Province de Luxembourg',
                                            'Province du Hainaut 2',
                                            'Province de Flandre-Occidentale',
                                            'Province de Flandre-Orientale']):
        raise Exception("""The data_dict does not contains the keys 
        'Province du Brabant wallon', 
        'Province du Brabant flamand', 
        'Province d\'Anvers', 
        'Province du Brabant flamand 2, 
        'Province de Limbourg', 
        'Province de Liège', 
        'Province de Namur', 
        'Province du Hainaut 1', 
        'Province de Luxembourg', 
        'Province du Hainaut 2', 
        'Province de Flandre-Occidentale', 
        'Province de Flandre-Orientale'""")
        
    #add the region to the data
    data_dict['Region Wallone'] = data_dict['Province du Brabant wallon']
    data_dict['Region Wallone'] = data_dict['Region Wallone'].append(data_dict['Province de Liège'])
    data_dict['Region Wallone'] = data_dict['Region Wallone'].append(data_dict['Province de Namur'])
    data_dict['Region Wallone'] = data_dict['Region Wallone'].append(data_dict['Province du Hainaut 1'])
    data_dict['Region Wallone'] = data_dict['Region Wallone'].append(data_dict['Province du Hainaut 2'])
    data_dict['Region Wallone'] = data_dict['Region Wallone'].append(data_dict['Province de Luxembourg'])

    data_dict['Region Flamande'] = data_dict['Province du Brabant flamand']
    data_dict['Region Flamande'] = data_dict['Region Flamande'].append(data_dict['Province d\'Anvers'])
    data_dict['Region Flamande'] = data_dict['Region Flamande'].append(data_dict['Province du Brabant flamand 2'])
    data_dict['Region Flamande'] = data_dict['Region Flamande'].append(data_dict['Province de Limbourg'])
    data_dict['Region Flamande'] = data_dict['Region Flamande'].append(data_dict['Province de Flandre-Occidentale'])
    data_dict['Region Flamande'] = data_dict['Region Flamande'].append(data_dict['Province de Flandre-Orientale'])

    return data_dict
    




def split_set(df : pd.DataFrame, min_zip : int, max_zip : int) -> pd.DataFrame:

    """
    This function takes a DataFrame and return a DataFrame with the data split by zipcode
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to split
        
    min_zip : int
        The min zipcode
        
    max_zip : int
        The max zipcode
        
    Returns
    -------   
    pd.DataFrame
        A DataFrame with the data split by zipcode
        
    Raise
    -----
    
    TypeError
        If the DataFrame is not a pd.DataFrame
        
    TypeError
        If the min_zip is not an int
        
    TypeError
        If the max_zip is not an int
        
    Warns
    -----
    UserWarning
        If the DataFrame is empty
    """
    
    #check if the DataFrame is a pd.DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("The DataFrame must be a pd.DataFrame")
    
    #check if the min_zip is an int
    if not isinstance(min_zip, int):
        raise TypeError("The min_zip must be an int")
        
    #check if the max_zip is an int
    if not isinstance(max_zip, int):
        raise TypeError("The max_zip must be an int")
        
    #check if the DataFrame is empty
    if df.empty:
        warn("The DataFrame is empty", UserWarning)
    
    return df[(df['zipcode'] > min_zip) & (df['zipcode'] < max_zip)]


def make_sets(csv : str = "Machine_learning/data_for_regression.csv") -> dict[str : pd.DataFrame]:

    """
    This function takes a csv file and return a dictionary with the data split by province
    
    Parameters
    ----------
    csv : str
        The path to the csv file
        
    Returns
    -------
    dict[str : pd.DataFrame]
        A dictionary with the data split by province
        

    Raise
    -----
    FileNotFoundError
        If the csv file is not found

    TypeError
        If the csv file is not a string

    Exception
        If the file is not a csv

    Warns
    -----
    UserWarning
        If the csv file is empty
    """

    #check if the csv file is a string
    if not isinstance(csv, str):
        raise TypeError("The csv file must be a string")

    #check if the csv file is a csv
    if not csv.endswith(".csv"):
        raise Exception("The file must be a csv")

    #check if the csv file is found
    if not os.path.isfile(csv):
        raise FileNotFoundError("The csv file is not found")

    #check if the csv file is empty
    if os.stat(csv).st_size == 0:
        warn("The csv file is empty", UserWarning)

    #load data
    data : pd.DataFrame = pd.read_csv(csv)
    data                = data[data["To sell"] == True]
    #make a dict with the dataframes
    data_dict : dict[str : pd.DataFrame] = {
                                            'Bruxelles-Capitale': split_set(data, 0 , 1300),
                                            'Province du Brabant wallon': split_set(data, 1299 , 1500),
                                            'Province du Brabant flamand': split_set(data, 1499 , 2000),
                                            'Province d\'Anvers': split_set(data, 1999 , 3000),
                                            'Province du Brabant flamand 2': split_set(data, 2999 , 3500),
                                            'Province de Limbourg': split_set(data, 3499 , 4000),
                                            'Province de Liège': split_set(data, 3999, 5000),
                                            'Province de Namur': split_set(data, 4999, 6000),
                                            'Province du Hainaut 1': split_set(data, 5999, 6600),
                                            'Province de Luxembourg': split_set(data, 6599, 7000),
                                            'Province du Hainaut 2': split_set(data, 6999, 8000),
                                            'Province de Flandre-Occidentale': split_set(data, 7999, 9000),
                                            'Province de Flandre-Orientale': split_set(data, 8999, 10000)
                                           }

    data_dict = region_add(data_dict)

    data_dict['Belgique'] = data

    return data_dict

def data_verification(data_dict : dict[str : pd.DataFrame]) -> dict[str : pd.DataFrame]:
    
    """
    This function takes a dictionary with the data split by province and return 
    a dictionary with the verified data
    
    Parameters
    ----------
    data_dict : dict[str : pd.DataFrame]
        The dictionary with the data split by province
        
    Returns
    -------
    dict[str : pd.DataFrame]
        A dictionary with the data verification
        
    Raise
    -----
    TypeError
        If the data_dict is not a dict
        
    TypeError
        If the data_dict is not a dict[str : pd.DataFrame]
        
    Warns
    -----
    UserWarning
        If the data_dict is empty
    """
    
    #check if the data_dict is a dict
    if not isinstance(data_dict, dict):
        raise TypeError("The data_dict must be a dict")
        
    #check if the data_dict is a dict[str : pd.DataFrame]
    if not all(isinstance(key, str) and isinstance(value, pd.DataFrame) for key, value in data_dict.items()):
        raise TypeError("The data_dict must be a dict[str : pd.DataFrame]")
        
    #check if the data_dict is empty
    if not data_dict:
        warn("The data_dict is empty", UserWarning)

    for key, data in data_dict.items():

        #replace None and NaN by False in Fully equipped kitchen, Furnished, Swimming pool and Open fire
        data['Fully equipped kitchen'] = data['Fully equipped kitchen'].fillna(False)
        data['Furnished'] = data['Furnished'].fillna(False)
        data['Swimming pool'] = data['Swimming pool'].fillna(False)
        data['Open fire'] = data['Open fire'].fillna(False)

        #replace None and NaN by 0 in Number of rooms, Living Area, Area of the terrace, Area of the garden
        data['Number of rooms'] = data['Number of rooms'].fillna(0)
        data['Living Area'] = data['Living Area'].fillna(0)
        data['Area of the terrace'] = data['Area of the terrace'].fillna(0)

        #compute the price by square meter
        data['Price per square meter'] = data['Price'] / data['Living Area']
        #replace the zipcode by the median at the given zipcode
        data['zipcode'] = data.groupby('zipcode')['Price per square meter'].mean()
        #replace the type by the median at the given type
        data['type'] = data.groupby('type')['Price per square meter'].mean()

        #remove price > 500_000
        data = data[data['Price'] < 500_000]
        #remove price < 50_000
        data = data[data['Price'] > 50_000]

        data['Price'] = data['Price per square meter']
        #remove price per square meter
        data = data.drop(['Price per square meter'], axis=1)


        #drop To sell
        data = data.drop(['To sell'], axis=1)
        data = data.drop(['Open fire'], axis=1)
        data = data.drop(['Swimming pool'], axis=1)

        data_dict[key] = data

    return data_dict

    
def get_models() -> dict[str : any]:

    """
    This function returns a dictionary with the models

    Returns
    -------
    dict[str : any]
        A dictionary with the models

    """

    models : dict[str : any] = {
                                'LinearRegression' : LinearRegression(),
                                'Ridge' : Ridge(),
                                'Lasso' : Lasso(),
                                'ElasticNet' : ElasticNet(),
                                'DecisionTreeRegressor' : DecisionTreeRegressor(),
                                'GradientBoostingRegressor' : GradientBoostingRegressor(),
                                'SVR' : SVR(),
                                #'MLPRegressor' : MLPRegressor(hidden_layer_sizes = (100,100,100), max_iter = 500),
                                'XGBoostSE' : xgb.XGBRegressor(objective ='reg:squarederror', 
                                                               learning_rate = 0.045,
                                                               max_depth = 150, 
                                                               alpha = 1, 
                                                               n_estimators = 105),
                                'XGBoostAE' : xgb.XGBRegressor(objective ='reg:absoluteerror', 
                                                               learning_rate = 0.045,
                                                               max_depth = 150, 
                                                               alpha = 1, 
                                                               n_estimators = 105)

                               }


    for m,n in product(range(50,351,25), range(20,301,25)):
        models[f'RandomForestRegressorM{m}N{n}'] = RandomForestRegressor(max_depth = m, n_estimators = n)

    for k in range(5,200):
        models[f'KNeighborsRegressorK{k}'] = KNeighborsRegressor(n_neighbors=k)

    return models


def training():


    #get the data
    data_dict = make_sets()

    #print the size of each element
    for key, data in data_dict.items():
        print(f"{key} : {data.shape}")

    #verify the data
    data_dict = data_verification(data_dict)
    #get the models
    models = get_models()

    #create a list to store the results
    results : list[dict[str : any]] = []

    #go through the models
    for name, model in tqdm(models.items()):

        #go through the data
        for key, data in data_dict.items():

            #pass for memory reason
            if key == 'Belgique' and name.startswith('Random'):
                continue

            if name != 'XGBoostSE':
                #replace nan
                data = data.fillna(0)
                continue

            #get the X and y
            X = data.drop(['Price'], axis=1)
            y = data['Price']

            #split the data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            #fit the model
            model.fit(X_train, y_train)

            #get the predictions
            y_pred = model.predict(X_test)

            #get the metrics
            r2 = r2_score(y_test, y_pred)
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)

            #store the results
            results.append({
                'Province': key,
                'Model': name,
                'R2': r2,
                'MSE': mse,
                'MAE': mae,
                'MAEP': 1 - mae/data['Price'].mean()
            })

            #save the model
            with open(f'{name}{key}.pickle', 'wb') as f:
                pickle.dump(model, f)

        del model

    #create a dataframe with the results
    results = pd.DataFrame(results)

    #save the results
    results.to_csv('results.csv', index=False)

    #print the results
    print(results)

    #get best results by procince
    results = results.groupby('Province').apply(lambda x: x.nlargest(1, 'MAEP'))

    #print the results
    print(results)

    
if __name__ == "__main__":
    training()

