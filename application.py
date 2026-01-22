import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

application = Flask(__name__)
app = application


# current path of this script
basedir = os.path.abspath(os.path.dirname(__file__))

# 2. Join the base path with your model paths
ridge_model_path = os.path.join(basedir, 'models', 'ridgecv.pkl')
scaler_path = os.path.join(basedir, 'models', 'scaler.pkl')

## import ridge and standardscaler pickel files
ridge_model = pickle.load(open(ridge_model_path,'rb'))
scaler = pickle.load(open(scaler_path,'rb'))

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        Rh = float(request.form.get('Rh'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_data_scaled = scaler.transform([[Temperature,Rh,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')