import pandas as pd
import numpy as np
from datetime import timedelta, datetime

def prep_sales(df):
    '''
    This function prepares sales dataframe.
    '''
    df.sale_date = pd.to_datetime(df.sale_date)
    df = df.set_index('sale_date').sort_index()
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    return df

def prep_opsd_germany(df):
    '''
    This function prepares the German energy production
    '''
    df.rename(columns = {'Date':'date','Consumption':'consumption','Wind':'wind','Solar':'solar','Wind+Solar':'wind_and_solar'},inplace = True)
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date').sort_index()
    df['month'] = df.index.month
    df['year'] = df.index.year
    df.fillna(0, inplace = True)
    return df
    