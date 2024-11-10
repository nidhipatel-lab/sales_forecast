import pandas as pd
import numpy as np
from sklearn.metrics import (
    mean_squared_error as mse,
    mean_absolute_error as mae,
    mean_absolute_percentage_error as mape

)

def dataProcessing(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['IsWeekend'] = df['Date'].dt.weekday >= 5  # True if Saturday or Sunday
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df["IsDiscount"] = np.where(df["Discount"] == "Yes", 1, 0)

    return df

def aggData(df):
    sdf = df.groupby('Date').agg(
    Day=('Day', 'first'),
    Month=('Month', 'first'),
    Year=('Year', 'first'),
    DayOfWeek=('DayOfWeek', 'first'),
    IsWeekend=('IsWeekend', 'first'),
    Holiday =('Holiday','sum'),
    IsDiscount=('IsDiscount', 'sum'),
    Number_of_Orders=('ID','count'),
    ).reset_index().copy()
    
    sdf['Date'] = pd.to_datetime(sdf['Date'])
    sdf.set_index('Date', inplace=True)
    return sdf

def performanceMetrics(actual, predicted):
    #print('MAE :', round(mae(actual, predicted), 3))
    #print('RMSE :', round(mse(actual, predicted)**0.5, 3))
    #print('MAPE:', round(mape(actual, predicted), 3))
    metrics = {
        "MAE": round(mae(actual, predicted), 3),
        "RMSE": round(mse(actual, predicted)**0.5, 3),
        "MAPE": round(mape(actual, predicted), 3)
    }
    return metrics

