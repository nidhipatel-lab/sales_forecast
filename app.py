# app.py
from predict import predict_app
from rpredict import rpredict_app
from flask import Flask

app = Flask(__name__)

# Register both Flask apps (predict and rpredict)
app.register_blueprint(predict_app, url_prefix='/predict')
app.register_blueprint(rpredict_app, url_prefix='/rpredict')

if __name__ == '__main__':
    app.run(debug=True)
