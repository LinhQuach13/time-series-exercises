# tabular data manipulation
import numpy as np
import pandas as pd
# datetime utilities
from datetime import timedelta, datetime
import datetime
# visualization
import matplotlib.pyplot as plt

# no yelling in the library
import warnings
warnings.filterwarnings("ignore")




def drop_cols(df):
    ''' 
    Takes in df and drops unnecessary indexed columns
    '''
    df= df.drop(columns= ['Unnamed: 0_x', 'Unnamed: 0_y', 'Unnamed: 0'])
    return df




def datatype_datatime64(df):
    ''' 
    Takes in df and converts sale data column to datatime64 datatype
    '''
    #Changing sale date datatype to datatime64 object
    df.sale_date= pd.to_datetime(df.sale_date)
    return df




def plot_sale_amount(df):
    ''' 
    Takes in df and plots the distribution of sale_amount column
    '''
    # Plot the distribution of sale_amount
    plt.figure()
    df.sale_amount.hist(label= "Sale Amount")
    plt.title('Plot of Sale Amount')
    plt.legend()
    plt.show()
    
    
    
    
def plot_item_price(df):
    ''' 
    Takes in df and plots the distribution item_price column
    '''
    plt.figure()
    df.item_price.hist(label= "Item Price")
    plt.title('Plot of Item Price')
    plt.legend()
    plt.show()

    
    
    
def set_store_index(df):
    ''' 
    Takes in df, sets sale_date as index and sorts by index
    '''
    # Set the index to be the datetime variable.
    df= df.set_index('sale_date').sort_index()
    return df




def month_day_and_sales_col(df):
    ''' 
    Takes in df and creates columns 
    (month column, day column, and sales_total column)
    '''
    # Creating day column
    df['month'] = df.index.month
    # Creating day column
    df['day'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    return df




def prepare_germany_data(df):
    ''' 
    Prepare Germany Data
    '''
    #Changing date datatype to datatime64 object
    df.Date= pd.to_datetime(df.Date)
    # Plot of consumption
    plt.figure()
    df.Consumption.hist(label= "Consumption")
    plt.title('Distribution of Consumption')
    plt.legend()
    plt.show()
    # Plot of Wind
    plt.figure()
    df.Wind.hist(label= "Wind")
    plt.title('Distribution of Wind')
    plt.legend()
    plt.show()
    # Plot of Solar
    plt.figure()
    df.Solar.hist(label= "Solar")
    plt.title('Distribution of Solar')
    plt.legend()
    plt.show()
    # Plot of Wind+Solar
    plt.figure()
    df['Wind+Solar'].hist(label= "Wind and Solar")
    plt.title('Distribution of Wind + Solar')
    plt.legend()
    plt.show()
    #Set the index to be the datetime variable.
    df= df.set_index('Date').sort_index()
    #Adding month column
    df['month'] = df.index.month
    #Creating year column
    df['year'] = df.index.year
    #Fill any missing values
    df = df.fillna(value=0)
    return df