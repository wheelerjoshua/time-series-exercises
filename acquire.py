import pandas as pd
import numpy as np
import requests
import os

base_url = 'https://python.zgulde.net'

def get_items():
    '''This function reads items.csv into a dataframe.
    If none is found, creates csv.'''
    if os.path.isfile('items.csv'):
        df = pd.read_csv('items.csv')
    else:
        response = requests.get('https://python.zgulde.net/api/v1/items')
        data = response.json()
        max_page = data['payload']['max_page']
        current_page = 0
        df = pd.DataFrame()

        while current_page != (max_page - 1):
            response = requests.get(base_url + data['payload']['next_page'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['payload']['items'])])
            current_page += 1
            if current_page > max_page:
                break
        df.to_csv('items.csv')
    return df        

def get_stores():
    '''This function reads stores.csv into a dataframe.
    If none is found, creates csv.'''
    if os.path.isfile('stores.csv'):
        df = pd.read_csv('stores.csv')
    else:
        response = requests.get('https://python.zgulde.net/api/v1/stores')
        data = response.json()
        df = pd.DataFrame(data['payload']['stores'])
        df.to_csv('stores.csv')
    return df


def get_sales():
    '''This function reads sales.csv into a dataframe.
    If none is found, creates csv.'''
    if os.path.isfile('sales.csv'):
        df = pd.read_csv('sales.csv')
    else:
        response = requests.get('https://python.zgulde.net/api/v1/sales')
        data = response.json()
        df = pd.DataFrame(data['payload']['sales'])
        while data['payload']['next_page']:
            response = requests.get(base_url + data['payload']['next_page'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['payload']['sales'])])
        df.to_csv('sales.csv')
    return df

def get_commerce():
    '''This funciton merges stores and items dataframes onto sales dataframe.'''
    sales = get_sales()
    items = get_items()
    stores = get_stores()
    sales.rename(columns = {'store':'store_id', 'item':'item_id'},inplace = True)
    df = pd.merge(sales, stores, on = 'store_id', how = 'left')
    df = pd.merge(df, items, on = 'item_id', how = 'left')
    return df

def get_opsd_germany():
    '''This function reads opsd_germany.csv into a dataframe.
    If none is found, creates csv.'''
    if os.path.isfile('opsd_germany.csv'):
        df = read_csv('opsd_germany.csv')
    else:
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        df.to_csv('opsd_german.csv')
    return df