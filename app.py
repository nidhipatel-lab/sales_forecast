from flask import Flask, request, jsonify
import predict, rpredict

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Sales Forecasting!"

@app.route('/sarimax')
def sarimax():
    return predict.product()  # Call the function and return its response


@app.route('/sarimax/predict', methods = ['POST'])
def sarimax_predict():
    return predict.prediction() 


@app.route('/reg')
def reg():
    return rpredict.rproduct() 


@app.route('/reg/predict', methods = ['POST'])
def reg_predict():
    return rpredict.prediction()  



if __name__ == '__main__':
    app.run()