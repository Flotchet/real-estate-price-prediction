import json
import os
import numpy as np
import pandas as pd
import pickle
import warnings



def save_data(data : any ,
              path : str ,
              name : str , 
              format : str , 
              error : bool = False , 
              warns : bool = True
                                    ) -> int:

    """
    Save data to file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :param format: format of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, (dict, list, np.ndarray, pd.DataFrame)):

        if warns:
            warnings.warn("data must be a dict, list, numpy array or pandas DataFrame")
        if error:
            raise TypeError("data must be a dict, list, numpy array or pandas DataFrame")
        else:
            return 3

    if not isinstance(path, str):

        if warns:
            warnings.warn("path must be a string")
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    if not isinstance(format, str):

        if warns:
            warnings.warn("format must be a string")
        if error:
            raise TypeError("format must be a string")
        else:
            return 4

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .json
    if not name.endswith('.' + format):
        name = name + '.' + format

    # Save data to json file
    if format == 'json':
        with open(path + name, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    # Save data to csv file
    elif format == 'csv':
        if isinstance(data, pd.DataFrame):
            data.to_csv(path + name, index=False)
        else:
            pd.DataFrame(data).to_csv(path + name, index=False)

    # Save data to txt file
    elif format == 'txt':
        if isinstance(data, pd.DataFrame):
            data.to_csv(path + name, index=False)
        else:
            pd.DataFrame(data).to_csv(path + name, index=False)

    else:
        if warns:
            warnings.warn("format must be 'json', 'csv' or 'txt'")
        if error:
            raise ValueError("format must be 'json', 'csv' or 'txt'")
        else:
            return 5

    return 0



def save_data_to_json(data : dict[any:any] , 
                      path : str , 
                      name : str , 
                      error : bool = False , 
                      warns : bool = True
                                            ) -> int :

    """
    Save data to json file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, dict):

        if warns:
            warnings.warn("data must be a dict")
        if error:
            raise TypeError("data must be a dict")
        else:
            return 3

    if not isinstance(path, str):   

        if warns:
            warnings.warn("path must be a string")      
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Check if the name ends with .json
    if not name.endswith('.json'):
        name = name + '.json'

    # Save data to json file
    with open(path + name, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    return 0



def save_data_to_csv(data : any , 
                     path : str , 
                     name : str , 
                     error : bool = False , 
                     warns : bool = True
                                            ) -> int:
                                            
    """
    Save data to csv file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, (dict, list, np.ndarray, pd.DataFrame)):

        if warns:
            warnings.warn("data must be a dict, list, numpy array or pandas DataFrame")
        if error:
            raise TypeError("data must be a dict, list, numpy array or pandas DataFrame")
        else:
            return 3

    if not isinstance(path, str):     

        if warns:
            warnings.warn("path must be a string")   
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .csv
    if not name.endswith('.csv'):
        name = name + '.csv'

    # Save data to csv file
    if isinstance(data, pd.DataFrame):
        data.to_csv(path + name, index=False)
    else:
        pd.DataFrame(data).to_csv(path + name, index=False)

    return 0



def save_data_to_txt(data : any , 
                     path : str , 
                     name : str , 
                     error : bool = False ,  
                     warns : bool = True
                                            ) -> int:

    """
    Save data to txt file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(data, (str, int, float, dict, list, np.ndarray, pd.DataFrame)):

        if warns:
            warnings.warn("data must be a str, int, float, dict, list, np.ndarray, pd.DataFrame")
        if error:
            raise TypeError("data must be a str, int, float, dict, list, np.ndarray, pd.DataFrame")
        else:
            return 3

    if not isinstance(path, str):      

        if warns:
            warnings.warn("path must be a string")  
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .txt 
    if not name.endswith('.txt'):
        name = name + '.txt'
    
    # Save data to txt file
    if isinstance(data, pd.DataFrame):
        data.to_csv(path + name, index=False)

    elif isinstance(data, np.ndarray):
        np.savetxt(path + name, data, delimiter=",")

    elif isinstance(data, str):
        with open(path + name, 'w') as outfile:
            outfile.write(data)

    elif isinstance(data, list):
        with open(path + name, 'w') as outfile:
            outfile.write(' '.join(data))
    else:
        with open(path + name, 'w') as outfile:
            outfile.write(str(data))

    return 0



def save_data_to_pickle(data : any , 
                        path : str , 
                        name : str , 
                        error : bool = False , 
                        warns : bool = True
                                                ) -> int:

    """
    Save data to pickle file
    :param data: data to save
    :param path: path to save
    :param name: name of file
    :return: None
    """

    # check if the types of the variables are the good ones:
    if not isinstance(path, str):  

        if warns:
            warnings.warn("path must be a string")       
        if error:
            raise TypeError("path must be a string")
        else:
            return 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return 1

    # Check if path exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # Check if the name ends with .pickle
    if not name.endswith('.pickle'):
        name = name + '.pickle'

    # try to save data to pickle file
    with open(path + name, 'wb') as outfile:
        pickle.dump(data, outfile)

    return 0



def load_json(path : str , 
              name : str , 
              error : bool = False,
              warns : bool = True
                                    ) -> tuple[dict:int]:

    """
    Load data from a json file into a dictionary
    :param path: path to save
    :param name: name of file
    :return: dictionary containing the json data and an code of execution
    """

    # check if the types of the variables are the good ones:
    if not isinstance(path, str): 

        if warns:
            warnings.warn("path must be a string")      
        if error:
            raise TypeError("path must be a string")
        else:
            return {}, 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return {}, 1

    # Check if path exist and if not create it
    if not os.path.exists(path):

        if warns:
            warnings.warn("The path does not exist")
        if error:
            raise FileNotFoundError("The path does not exist")
        else:
            return {}, 3

    # Check if the name ends with .json
    if not name.endswith('.json'):
        name = name + '.json'

    # Check if the file exist
    if not os.path.exists(path + name):

        if warns:
            warnings.warn("The file does not exist")
        if error:
            raise FileNotFoundError("The file does not exist")
        else:
            return {}, 4

    # Load data from json file
    with open(path + name, 'r') as infile:
        data = json.load(infile)

    return data, 0



def load_csv(path : str , 
             name : str , 
             error : bool = False ,
             warns : bool = True
                                    ) -> tuple[any:int]:

    """
    Load data from a csv file into a dictionary
    :param path: path to save
    :param name: name of file
    :return: dictionary containing the json data and an code of execution
    """

    # check if the types of the variables are the good ones:
    if not isinstance(path, str):

        if warns:
            warnings.warn("path must be a string")
        if error:
            raise TypeError("path must be a string")
        else:
            return {}, 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return {}, 1

    # Check if path exist and if not create it
    if not os.path.exists(path):

        if warns:
            warnings.warn("The path does not exist")
        if error:
            raise FileNotFoundError("The path does not exist")
        else:
            return {}, 3

    # Check if the name ends with .csv
    if not name.endswith('.csv'):
        name = name + '.csv'

    # Check if the file exist
    if not os.path.exists(path + name):

        if warns:
            warnings.warn("The file does not exist")
        if error:
            raise FileNotFoundError("The file does not exist")
        else:
            return {}, 4

    # Load data from csv file
    data = pd.read_csv(path + name)

    return data, 0



def load_txt(path : str , 
             name : str , 
             error : bool = False , 
             warns : bool = True
                                    ) -> tuple[str, int]:
    
        """
        Load data from a txt file into a dictionary
        :param path: path to save
        :param name: name of file
        :return: dictionary containing the json data and an code of execution
        """
    
        # check if the types of the variables are the good ones:
        if not isinstance(path, str):       

            if warns:
                warnings.warn("path must be a string") 
            if error:
                raise TypeError("path must be a string")
            else:
                return {}, 2
        
        if not isinstance(name, str):

            if warns:
                warnings.warn("name must be a string")
            if error:
                raise TypeError("name must be a string")
            else:
                return {}, 1
    
        # Check if path exist and if not create it
        if not os.path.exists(path):

            if warns:
                warnings.warn("The path does not exist")
            if error:
                raise FileNotFoundError("The path does not exist")
            else:
                return {}, 3
    
        # Check if the name ends with .txt
        if not name.endswith('.txt'):
            name = name + '.txt'
    
        # Check if the file exist
        if not os.path.exists(path + name):

            if warns:
                warnings.warn("The file does not exist")
            if error:
                raise FileNotFoundError("The file does not exist")
            else:
                return {}, 4
    
        # Load data from txt file as str
        with open(path + name, 'r') as infile:
            data = infile.read()
    
        return data, 0



def load_pickle(path : str , 
                name : str , 
                error : bool = False , 
                warns : bool = True
                                        ) -> tuple[any, int]:

    """
    Load data from a pickle file into a dictionary
    :param path: path to save
    :param name: name of file
    :return: dictionary containing the json data and an code of execution
    """

    # check if the types of the variables are the good ones:
    if not isinstance(path, str):   

        if warns:
            warnings.warn("path must be a string")     
        if error:
            raise TypeError("path must be a string")
        else:
            return {}, 2
    
    if not isinstance(name, str):

        if warns:
            warnings.warn("name must be a string")
        if error:
            raise TypeError("name must be a string")
        else:
            return {}, 1

    # Check if path exist and if not create it
    if not os.path.exists(path):

        if warns:
            warnings.warn("The path does not exist")
        if error:
            raise FileNotFoundError("The path does not exist")
        else:
            return {}, 3

    # Check if the name ends with .pickle
    if not name.endswith('.pickle'):
        name = name + '.pickle'

    # Check if the file exist
    if not os.path.exists(path + name):

        if warns:
            warnings.warn("The file does not exist")
        if error:
            raise FileNotFoundError("The file does not exist")
        else:
            return {}, 4

    # Load data from pickle file
    with open(path + name, 'rb') as infile:
        data = pickle.load(infile)

    return data, 0


def main():

    # Create a dictionary
    data = {'a': 1, 'b': 2, 'c': 3}
    directory_target = ""
    error = False

    # Save the dictionary to a json file
    save_data_to_json(directory_target, "test", data, error)
    
    # Load the dictionary from the json file
    data, code = load_json(directory_target, "test.json", error)
    print(data, code)

    # Save the dictionary to a csv file
    save_data_to_csv(directory_target, "test", data, error)

    # Load the dictionary from the csv file
    data, code = load_csv(directory_target, "test.csv", error)
    print(data, code)

    # Save the dictionary to a txt file
    save_data_to_txt(directory_target, "test", data, error)

    # Load the dictionary from the txt file
    data, code = load_txt(directory_target, "test.txt", error)
    print(data, code)

    # Save the dictionary to a pickle file
    save_data_to_pickle(directory_target, "test", data, error)

    # Load the dictionary from the pickle file
    data, code = load_pickle(directory_target, "test.pickle", error)
    print(data, code)

if __name__ == '__main__':
    main()
