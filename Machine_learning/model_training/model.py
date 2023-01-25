#use xgboost as regression to make the estimation
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def split_set(df)

def make_sets(csv : str = "Machine_learning/data_for_regression.csv") -> dict[str : pd.DataFrame]:
    #load data
    data : pd.DataFrame = pd.read_csv(csv)
    data                = data[data["To sell"] == True]

    #exclude the data from brussels region Bruxelles-Capitale
    data_bx : pd.DataFrame = data[data['zipcode'] < 1300]

    #only take the data where 1299 < zipcode < 1500 Province du Brabant wallon
    data_bw : pd.DataFrame = data[data['zipcode'] > 1299]
    data_bw                = data_bw[data_bw['zipcode'] < 1500]

    #only take the data where 1499 < zipcode < 2000 Province du Brabant flamand 
    data_bf : pd.DataFrame = data[data['zipcode'] > 1499]
    data_bf                = data_bf[data_bf['zipcode'] < 2000]

    #only take the data where 1999 < zipcode < 3000 Province d'Anvers
    data_an : pd.DataFrame = data[data['zipcode'] > 1999]
    data_an                = data_an[data_an['zipcode'] < 3000]

    #only take the data where 2999 < zipcode < 3500 Province du Brabant flamand 2
    data_bf2 : pd.DataFrame = data[data['zipcode'] > 2999]
    data_bf2                = data_bf2[data_bf2['zipcode'] < 3500]

        #only take the data where 3499 < zipcode < 4000 Province de Limbourg
    data_li : pd.DataFrame = data[data['zipcode'] > 3499]
    data_li                = data_li[data_li['zipcode'] < 4000]

    #only take the data where 3999 < zipcode < 5000 Province de Liège
    data_lg : pd.DataFrame = data[data['zipcode'] > 3999] 
    data_lg                = data_lg[data_lg['zipcode'] < 5000]

    #only take the data where 4999 < zipcode < 6000 Province de Namur
    data_na : pd.DataFrame = data[data['zipcode'] > 4999]
    data_na                = data_na[data_na['zipcode'] < 6000]

    #only take the data where 5999 < zipcode < 6600 Province du Hainaut 1
    data_ha1 : pd.DataFrame = data[data['zipcode'] > 5999]
    data_ha1                = data_ha1[data_ha1['zipcode'] < 6600]

    #only take the data where 6599 < zipcode < 7000 Province de Luxembourg
    data_lu : pd.DataFrame = data[data['zipcode'] > 6599]
    data_lu                = data_lu[data_lu['zipcode'] < 7000]

    #only take the data where 6999 < zipcode < 8000 Province du Hainaut 2
    data_ha2 : pd.DataFrame = data[data['zipcode'] > 6999]
    data_ha2                = data_ha2[data_ha2['zipcode'] < 8000]

    #only take the data where 7999 < zipcode < 9000 Province de Flandre-Occidentale
    data_foc : pd.DataFrame = data[data['zipcode'] > 7999]
    data_foc                = data_foc[data_foc['zipcode'] < 9000]

    #only take the data where 8999 < zipcode < 10000 Province de Flandre-Orientale
    data_for : pd.DataFrame = data[data['zipcode'] > 8999]
    data_for                = data_for[data_for['zipcode'] < 10000]


    #make a dict with the dataframes
    data_dict : dict[str : pd.DataFrame] = {
                                            'Bruxelles-Capitale': data_bx, 
                                            'Province du Brabant wallon': data_bw, 
                                            'Province du Brabant flamand': data_bf, 
                                            'Province d\'Anvers': data_an, 
                                            'Province du Brabant flamand 2': data_bf2, 
                                            'Province de Limbourg': data_li, 
                                            'Province de Liège': data_lg, 
                                            'Province de Namur': data_na, 
                                            'Province du Hainaut 1': data_ha1, 
                                            'Province de Luxembourg': data_lu, 
                                            'Province du Hainaut 2': data_ha2, 
                                            'Province de Flandre-Occidentale': data_foc, 
                                            'Province de Flandre-Orientale': data_for
                                           }

    return data_dict

def adapt_data
s=0
#go trougth items 
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

    #split data
    X = data.drop(['Price'], axis=1)
    y = data['Price']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=123)

    # Create a XGBoost regressor
    xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = .75, learning_rate = 0.045,
                              max_depth = 150, alpha = 1, n_estimators = 105)

    # Fit the regressor to the training data
    xg_reg.fit(X_train, y_train)

    # Predict on the test set
    y_pred = xg_reg.predict(X_test)

    # Calculate the R-squared score
    r2 = r2_score(y_test, y_pred)

    print(key)

    print(r2)

    # Calculate the rsquared error
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    print(rmse)

    # compute the absolute error
    errors = abs(y_pred - y_test).mean()
    print(errors)
    print(100 - errors / data['Price'].mean() * 100)

    s += 100 - errors / data['Price'].mean() * 100

print(s/13)