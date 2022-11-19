# Created the util.py, it contains all the core routines
import json
import pickle
import numpy as np

import pickle
import json
import numpy as np

__locations = None
__data_columns = None # pyhton list
__model = None

# function that will return estimated price, location, sqft, bhk, bathroom
#
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # predict method that will take an input as x and will return an output that is estimated price
    return round(__model.predict([x])[0],2)

# this function returns the location names
def get_location_names():
    pass
    return __locations # function get_location_names returning the locations

# Function will load saved artifiacts in json and home prices and storing in to a global variables
def load_saved_artifacts():
    print('Loading saved artifacts')
    global __data_columns
    global __locations

    global __model
    # opening .json file from artifacts directory
    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns'] # data_columns is key that will return all the data column
        __locations = __data_columns[3:] # get elements from the list starting from # 03

    with open('./artifacts/banglore_home_prices_model.pickle','rb') as f:  # loading a saved pickled models into as __models
        __model = pickle.load(f) # load pickle file
    print('Loading saved artifacts....done')

if __name__ == '__main__':
    load_saved_artifacts() # calling the method
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))