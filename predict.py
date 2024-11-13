from flask import Flask, request, jsonify
import lib  
import pickle
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

app = Flask(__name__)

#@app.route('/')
def product():
    return 'SARIMAX Sales Forecasting!'

with open("./artifacts/forecast_sarimax_result.pkl", "rb") as pickle_in:
    loaded_sarimaxResult = pickle.load(pickle_in)


#@app.route('/predict', methods = ['POST'])
def prediction():
    data = request.get_json(force=True)
    required_columns = ['Holiday', 'IsDiscount', 'IsWeekend', 'Month', 'Number_of_Orders']
    
    if not isinstance(data, dict):
        return {"error": "Data should be a dictionary with dates as keys."}
    
    df = pd.DataFrame.from_dict(data, orient='index')
    
    if not all(col in df.columns for col in required_columns):
        return {"error": "JSON format is incorrect. Required columns are: " + ", ".join(required_columns)}


    scaler = MinMaxScaler()
    exogfeature= df[required_columns]
    scaler.fit(exogfeature)
    exog_forecast = scaler.transform(exogfeature) 
    forecast_steps = len(exog_forecast) 
    forecast = loaded_sarimaxResult.get_forecast(steps=forecast_steps, exog=exog_forecast)
    forecast_ci = forecast.conf_int()
    forecasted_values = forecast.predicted_mean
    forecast_original_scale = np.exp(forecasted_values)
    #print("Forecasted Sales (Original Scale):")
    #print(forecast_original_scale)

    metrics=None
    if 'Sales' in df.columns:
        metrics=lib.performanceMetrics(df['Sales'], forecast_original_scale)

    
    # Response
    response = {
        "data":data.tolist(),
        "forecasted_sales": forecast_original_scale.tolist(),
        "forecast_confidence_interval_lower": forecast_ci.iloc[:, 0].tolist(),
        "forecast_confidence_interval_upper": forecast_ci.iloc[:, 1].tolist(),
        "metrics": metrics
    }
    
    return jsonify(response)


#if __name__ == '__main__':
#    app.run()