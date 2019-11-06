from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd


app = Flask(__name__)


@app.route('/api', methods=['POST'])
def makecalc():
    data = request.get_json(force=True)
    d={}
    if(data['type']=="IT"):
        d['type']=[0]
    elif(data['type']=="education"):
        d['type']=[0.33]
    elif(data['type']=="recreation"):
        d['type']=[0.66]
    else:
        d['type']=[1]
    if(data['timing']=='A'):
        d['timing']=[0]
    elif(data['timing']=='B'):
        d['timing']=[0.5]
    else:
        d['timing']=[1]
    if(data['weather']=='sunny'):
        d['weather']=[0]
    else:
        d['weather']=[1]
    if(data['holiday type']=='national'):
        d['holiday type']=[0]
    elif(data['holiday type']=='festival'):
        d['holiday type']=[0.33]
    elif(data['holiday type']=='weekends'):
        d['holiday type']=[0.66]
    else:
        d['holiday type']=[1]
    modelfile = 'model/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    prediction=np.array2string(model.predict(pd.DataFrame(d)))    
    return jsonify(prediction)

if __name__ == '__main__':
    app.run()
