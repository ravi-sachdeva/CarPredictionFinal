from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Owner=int(request.form['Owner'])
        Fuel_Type=request.form['Fuel_Type']

        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

        if(Fuel_Type=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0

        elif(Fuel_Type=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1

            
        Year=2020-Year

        Seller_Type = request.form['Seller_Type']
        if(Seller_Type == 'Individual'):
            Seller_Type = 1
        else:
            Seller_Type = 0



        Transmission = request.form['Transmission']
        if(Transmission == 'Manual'):
            Transmission = 1
        else:
            Transmission = 0



        prediction=model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type,Transmission]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="You Can Sell The Car at {} Lakhs".format(output))
    

if __name__=="__main__":
    app.run(debug=True)

