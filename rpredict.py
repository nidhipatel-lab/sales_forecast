from flask import Flask, request, jsonify
import lib  
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

app = Flask(__name__)

model_filename="./artifacts/Regressor.pkl"
scaler_filename="./artifacts/Regressor_scaler.pkl"
def load_model_and_scaler(model_filename, scaler_filename):
    try:
        with open(model_filename, 'rb') as model_file:
            model = pickle.load(model_file)
        
        with open(scaler_filename, 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)

        return model, scaler
    except Exception as e:
        raise Exception(f"Error loading model or scaler: {str(e)}")


@app.route('/rpredict', methods=['POST'])
def rpredict():
    try:
        model, scaler = load_model_and_scaler(model_filename, scaler_filename)

        data = request.get_json(force=True) 
        if not isinstance(data, dict):
            return {"error": "Data should be a dictionary with dates as keys."}
        
        required_keys = ['Holiday', 'IsDiscount', 'Day', 'Month', 'Year', 'DayOfWeek', 'IsWeekend', 'Number_of_Orders']
        
        for date, day_data in data.items():
            if not all(key in day_data for key in required_keys):
                return jsonify({"error": f"Missing required fields for date {date}"}), 400
            

        df = pd.DataFrame.from_dict(data, orient='index')

        if df.empty:
            return jsonify({"error": "Dataframe is empty, check the input data."}),400
        
        scaled_features = scaler.transform(df)

        predictions = model.predict(scaled_features)
        
        response = {
            "predictions": predictions.tolist()
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)