from flask import *
from sklearn.externals import joblib
import pandas as pd
import numpy as np
app=Flask(__name__)
regression=joblib.load(open("multiple_linear_model.pkl",'rb'))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
        RnD_Spend=float(request.form['RnD_Spend'])
        Admin_Spend=float(request.form['Admin_Spend'])
        Market_Spend=float(request.form['Market_Spend'])
        NewYork=float(request.form['NewYork'])
        Califonia=float(request.form['Califonia'])
        Florida=float(request.form['Florida'])
        
        result=regression.predict([[RnD_Spend,Admin_Spend,Market_Spend,NewYork,Califonia,Florida]])[0]
        
        return render_template('predict.html',prediction=result)
if __name__=="__main__":
    app.run(debug=True)