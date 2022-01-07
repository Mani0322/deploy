from flask import Flask,render_template,request
import pickle 
import numpy as np

model = pickle.load(open("model.pkl","rb"))
app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_carprice():
    Present_price = float(request.form.get("Present Price"))
    Kms_Driven = int(request.form.get("Kms Driven"))
    Fuel_Type = int(request.form.get("Fuel Type"))
    Seller_Type = int(request.form.get("Seller Type"))
    Transmission = int(request.form.get("Transmission"))
    Owner = int(request.form.get("Owner"))

    result = model.predict(np.array([Present_price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]).reshape(1,6))
    

    return {"selling price":float(result.round(2))}
    
    
    
    
    




if __name__ == "__main__":
    app.run(debug=True)
