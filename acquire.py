''''''''''''''''''''
'                  '
'    IMPORTS       '
'                  '
''''''''''''''''''''
import pandas as pd
import requests
import os



''''''''''''''''''''
'                  '
'   ACQUIRE        '
'                  '
''''''''''''''''''''

def csv_to_dataframe(url, page_name, key1, key2= None, key3= None):
    ''' 
    Takes in a csv and return that dataframe.
    csv_to_dataframe(
    url: csv url,
    key1: key from dataframe,
    key2= None
    )
    '''
    items_list = []
    
    # Let's take an example url and make a get request
    response = requests.get(url)
    #create dictionary object
    data= response.json()
    
    n = data[key1][key2]
    
    if (key2 != None) & (key3 != None):
        #Adding 1 here so the last digit is not cut off (not inclusive)
        for i in range(1,n+1):
            url = f'https://python.zach.lol/api/v1/{page_name}?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data[key1][key3]
            items_list += page_items
    else:
        for i in range(1,n+1):
            url = f'https://python.zach.lol/api/v1/{page_name}?page='+str(i)
            response = requests.get(url)
            data = response.json()
            page_items = data[key1]
            items_list += page_items
    
    df= pd.DataFrame(items_list)
    return df




def get_data(csv, url, page_name, key1, key2= None, key3= None, cached=False):
    '''
    This function reads in items df and writes data to
    a csv file if cached == False or if cached == True reads in sales df from
    a csv file, returns df.
    '''
    if cached == False or os.path.isfile(csv) == False:
        
        #Read fresh data from db into a DataFrame.
        df= csv_to_dataframe(url, page_name, key1, key2, key3)
        
        # Write DataFrame to a csv file.
        df.to_csv(csv)
        
    else:
        
        # If csv file exists or cached == True, read in data from csv.
        df = pd.read_csv(csv, index_col=0)
        
    return df





