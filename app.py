import json
import pickle
from flask_cors import cross_origin
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
## Load the model
regmodel=pickle.load(open('reg.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
@cross_origin()
def home():
    return render_template('home.html')

@app.route('/predict',methods=["GET",'POST'])
@cross_origin()
def predict():
    if request.method == "POST":
        OverallQual=int(request.form["OverallQual"])
        GarageCars=int(request.form["GarageCars"])

        ExterQual=request.form["ExterQual"]
        if(ExterQual=='Fa'):
            ExterQual=0
        elif(ExterQual=="TA"):
            ExterQual=1
        elif(ExterQual=="Gd"):
            ExterQual=2
        else:
            ExterQual=3
        
        Neighborhood=request.form["Neighborhood"]
        if(Neighborhood=="MeadowV"):
            Neighborhood=0
        elif(Neighborhood=="IDOTRR"):
            Neighborhood=1
        elif(Neighborhood=="BrDale"):
            Neighborhood=2
        elif(Neighborhood=="BrkSide"):
            Neighborhood=3
        elif(Neighborhood=="Edwards"):
            Neighborhood=4
        elif(Neighborhood=="OldTown"):
            Neighborhood=5
        elif(Neighborhood=="Sawyer"):
            Neighborhood=6
        elif(Neighborhood=="Blueste"):
            Neighborhood=7
        elif(Neighborhood=="SWISU"):
            Neighborhood=8
        elif(Neighborhood=="NPkVill"):
            Neighborhood=9
        elif(Neighborhood=="NAmes"):
            Neighborhood=10
        elif(Neighborhood=="Mitchel"):
            Neighborhood=11
        elif(Neighborhood=="SawyerW"):
            Neighborhood=12
        elif(Neighborhood=="NWAmes"):
            Neighborhood=13
        elif(Neighborhood=="Gilbert"):
            Neighborhood=14
        elif(Neighborhood=="Blmngtn"):
            Neighborhood=15
        elif(Neighborhood=="CollgCr"):
            Neighborhood=16
        elif(Neighborhood=="Crawfor"):
            Neighborhood=17
        elif(Neighborhood=="ClearCr"):
            Neighborhood=18
        elif(Neighborhood=="Somerst"):
            Neighborhood=19
        elif(Neighborhood=="Veenker"):
            Neighborhood=20
        elif(Neighborhood=="Timber"):
            Neighborhood=21
        elif(Neighborhood=="StoneBr"):
            Neighborhood=22
        elif(Neighborhood=="NridgHt"):
            Neighborhood=23
        else:
            Neighborhood=24
        GrLivArea=int(request.form["GrLivArea"])
        KitchenQual=request.form["KitchenQual"]
        if(KitchenQual=="Fa"):
            KitchenQual=0
        elif(KitchenQual=="TA"):
            KitchenQual=1
        elif(KitchenQual=="Gd"):
            KitchenQual=2
        else:
            KitchenQual=3
        BsmtQual=request.form["BsmtQual"]
        if(BsmtQual=="Missing"):
            BsmtQual=0
        elif(BsmtQual=="Fa"):
            BsmtQual=1
        elif(BsmtQual=="TA"):
            BsmtQual=2
        elif(BsmtQual=="Gd"):
            BsmtQual=3
        else:
            BsmtQual=4
        FullBath=int(request.form["FullBath"])
        stFlrSF=int(request.form["1stFlrSF"])
        TotalBsmtSF=int(request.form["TotalBsmtSF"])

        ndFlrSF=int(request.form['2ndFlrSF'])
        FireplaceQu=request.form["FireplaceQu"]
        if(FireplaceQu=="Po"):
            FireplaceQu=0
        elif(FireplaceQu=="Missing"):
            FireplaceQu=1
        elif(FireplaceQu=="Fa"):
            FireplaceQu=2
        elif(FireplaceQu=="TA"):
            FireplaceQu=3
        elif(FireplaceQu=="Gd"):
            FireplaceQu=4
        else:
            FireplaceQu=5
        BsmtFinSF1=int(request.form["BsmtFinSF1"])
        YearBuilt=int(request.form["YearBuilt"])
        GarageArea=int(request.form["GarageArea"])
        GarageType=request.form["GarageType"]
        if(GarageType=="Missing"):
            GarageType=0
        elif(GarageType=="CarPort"):
            GarageType=1
        elif(GarageType=="Detchd"):
            GarageType=2
        elif(GarageType=="Types"):
            GarageType=3
        elif(GarageType=="Basment"):
            GarageType=4
        elif(GarageType=="Attchd"):
            GarageType=5
        else:
            GarageType=6
        Fireplaces=int(request.form["Fireplaces"])
        TotRmsAbvGrd=int(request.form["TotRmsAbvGrd"])
        YearRemodAdd=int(request.form["YearRemodAdd"])
        BedroomAbvGr=int(request.form['BedroomAbvGr'])


        GarageYrBlt=int(request.form["GarageYrBlt"])
        GarageFinish=request.form["GarageFinish"]
        if(GarageFinish=="Missing"):
            GarageFinish=0
        elif(GarageFinish=="Unf"):
            GarageFinish=1
        elif(GarageFinish=="RFn"):
            GarageFinish=2
        else:
            GarageFinish=3
        LotArea=int(request.form["LotArea"])
        CentralAir=request.form["CentralAir"]
        if(CentralAir=="N"):
            CentralAir=0
        else:
            CentralAir=1
        BsmtFullBath=int(request.form['BsmtFullBath'])
        MasVnrArea=int(request.form["MasVnrArea"])
        BsmtExposure=request.form["BsmtExposure"]
        if(BsmtExposure=="Missing"):
            BsmtExposure=0
        elif(BsmtExposure=="No"):
            BsmtExposure=1
        elif(BsmtExposure=="Mn"):
            BsmtExposure=2
        elif(BsmtExposure=="Av"):
            BsmtExposure=3
        else:
            BsmtExposure=4
        OverallCond=int(request.form["OverallCond"])
        WoodDeckSF=int(request.form["WoodDeckSF"])
        MSZoning=request.form["MSZoning"]
        if(MSZoning=="C"):
            MSZoning=0
        elif(MSZoning=="RM"):
            MSZoning=1
        elif(MSZoning=="RH"):
            MSZoning=2
        elif(MSZoning=="RL"):
            MSZoning=3
        else:
            MSZoning=4
        
        data=[[OverallQual,GarageCars,ExterQual,Neighborhood,GrLivArea,KitchenQual,BsmtQual,FullBath,stFlrSF,TotalBsmtSF,ndFlrSF,
        FireplaceQu,BsmtFinSF1,YearBuilt,GarageArea,GarageType,Fireplaces,TotRmsAbvGrd,YearRemodAdd,BedroomAbvGr,GarageYrBlt,GarageFinish,
        LotArea,CentralAir,BsmtFullBath,MasVnrArea,BsmtExposure,OverallCond,WoodDeckSF,MSZoning]]

        new_data=scalar.transform(data)
        output=regmodel.predict(new_data)
        print(output[0])

        return render_template('home.html',prediction_text="Your House price is Rs. {}".format(output))
                
    

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)