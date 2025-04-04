import pickle
import pandas as np
from sklearn.preprocessing import PowerTransformer
from flask import Flask,request,jsonify,render_template

application=Flask(__name__)
app=application

linreg=pickle.load(open('model/reg.pkl','rb'))
power_transformer=pickle.load(open('model/pt.pkl','rb'))

@app.route('/',methods=['GET','POST'])

def predict_data():
    if request.method=='POST':
        Cement=float(request.form.get('Cement'))
        Blast_Furnace_Slag=float(request.form.get('Blast Furnace Slag'))
        Fly_Ash=float(request.form.get('Fly Ash'))
        Water=float(request.form.get('Water'))
        Superplaticizer=float(request.form.get('Superplasticizer'))
        Coarse_Aggregate=float(request.form.get('Coarse Aggregate'))
        Fine_Aggregate=float(request.form.get('Fine Aggregate'))
        Age=float(request.form.get('Age'))

        new_data_pt=power_transformer.transform([[Cement,Blast_Furnace_Slag,Fly_Ash,Water,Superplaticizer,Coarse_Aggregate,Fine_Aggregate,Age]])
        result=linreg.predict(new_data_pt)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")