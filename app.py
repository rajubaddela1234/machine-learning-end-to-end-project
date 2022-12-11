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
            Fa=0
        elif(ExterQual=="TA"):
            TA=1
        elif(ExterQual=="Gd"):
            Gd=2
        else:
            EX=3
        
        Neighborhood=request.form["Neighborhood"]
        if(Neighborhood=="MeadowV"):
            MeadowV=0
        elif(Neighborhood=="IDOTRR"):
            IDOTRR=1
        elif(Neighborhood=="BrDale"):
            BrDale=2
        elif(Neighborhood=="BrkSide"):
            BrkSide=3
        elif(Neighborhood=="Edwards"):
            Edwards=4
        elif(Neighborhood=="OldTown"):
            OldTown=5
        elif(Neighborhood=="Sawyer"):
            Sawyer=6
        elif(Neighborhood=="Blueste"):
            Blueste=7
        elif(Neighborhood=="SWISU"):
            SWISU=8
        elif(Neighborhood=="NPkVill"):
            NPkVill=9
        elif(Neighborhood=="NAmes"):
            NAmes=10
        elif(Neighborhood=="Mitchel"):
            Mitchel=11
        elif(Neighborhood=="SawyerW"):
            SawyerW=12
        elif(Neighborhood=="NWAmes"):
            NWAmes=13
        elif(Neighborhood=="Gilbert"):
            Gilbert=14
        elif(Neighborhood=="Blmngtn"):
            Blmngtn=15
        elif(Neighborhood=="CollgCr"):
            CollgCr=16
        elif(Neighborhood=="Crawfor"):
            Crawfor=17
        elif(Neighborhood=="ClearCr"):
            ClearCr=18
        elif(Neighborhood=="Somerst"):
            Somerst=19
        elif(Neighborhood=="Veenker"):
            Veenker=20
        elif(Neighborhood=="Timber"):
            Timber=21
        elif(Neighborhood=="StoneBr"):
            StoneBr=22
        elif(Neighborhood=="NridgHt"):
            NridgHt=23
        else:
            NoRidge=24
        GrLivArea=int(request.form["GrLivArea"])
        KitchenQual=request.form["KitchenQual"]
        if(KitchenQual=="Fa"):
            Fa=0
        elif(KitchenQual=="TA"):
            TA=1
        elif(KitchenQual=="Gd"):
            Gd=2
        else:
            Ex=3
        BsmtQual=request.form["BsmtQual"]
        if(BsmtQual=="Missing"):
            Missing=0
        elif(BsmtQual=="Fa"):
            Fa=1
        elif(BsmtQual=="TA"):
            TA=2
        elif(BsmtQual=="Gd"):
            Gd=3
        else:
            Ex=4
        FullBath=int(request.form["FullBath"])
        stFlrSF=int(request.form["1stFlrSF"])
        TotalBsmtSF=int(request.form["TotalBsmtSF"])

        ndFlrSF=int(request.form['2ndFlrSF'])
        FireplaceQu=request.form["FireplaceQu"]
        if(FireplaceQu=="Po"):
            Po=0
        elif(FireplaceQu=="Missing"):
            Missind=1
        elif(FireplaceQu=="Fa"):
            Fa=2
        elif(FireplaceQu=="TA"):
            TA=3
        elif(FireplaceQu=="Gd"):
            Gd=4
        else:
            Ex=5
        BsmtFinSF1=int(request.form["BsmtFinSF1"])
        YearBuilt=int(request.form["YearBuilt"])
        GarageArea=int(request.form["GarageArea"])
        GarageType=request.form["GarageType"]
        if(GarageType=="Missing"):
            Missing=0
        elif(GarageType=="CarPort"):
            CarPort=1
        elif(GarageType=="Detchd"):
            Detchd=2
        elif(GarageType=="Types"):
            Types=3
        elif(GarageType=="Basment"):
            Basment=4
        elif(GarageType=="Attchd"):
            Attchd=5
        else:
            BuiltIn=6
        Fireplaces=int(request.form["Fireplaces"])
        TotRmsAbvGrd=int(request.form["TotRmsAbvGrd"])
        YearRemodAdd=int(request.form["YearRemodAdd"])
        BedroomAbvGr=int(request.form['BedroomAbvGr'])


        GarageYrBlt=int(request.form["GarageYrBlt"])
        GarageFinish=request.form["GarageFinish"]
        if(GarageFinish=="Missing"):
            Missing=0
        elif(GarageFinish=="Unf"):
            Unf=1
        elif(GarageFinish=="RFn"):
            RFn=2
        else:
            Fin=3
        LotArea=int(request.form["LotArea"])
        CentralAir=request.form["CentralAir"]
        if(CentralAir=="N"):
            N=0
        else:
            Y=1
        BsmtFullBath=int(request.form['BsmtFullBath'])
        MasVnrArea=int(request.form["MasVnrArea"])
        BsmtExposure=request.form["BsmtExposure"]
        if(BsmtExposure=="Missing"):
            Missing=0
        elif(BsmtExposure=="No"):
            No=1
        elif(BsmtExposure=="Mn"):
            Mn=2
        elif(BsmtExposure=="Av"):
            Av=3
        else:
            Gd=4
        OverallCond=int(request.form["OverallCond"])
        WoodDeckSF=int(request.form["WoodDeckSF"])
        MSZoning=request.form["MSZoning"]
        if(MSZoning=="C"):
            C=0
        elif(MSZoning=="RM"):
            RM=1
        elif(MSZoning=="RH"):
            RH=2
        elif(MSZoning=="RL"):
            RL=3
        else:
            FV=4
        
        data=[[OverallQual,GarageCars,ExterQual,Neighborhood,GrLivArea,KitchenQual,BsmtQual,FullBath,stFlrSF,TotalBsmtSF,ndFlrSF,
        FireplaceQu,BsmtFinSF1,YearBuilt,GarageArea,GarageType,Fireplaces,TotRmsAbvGrd,YearRemodAdd,BedroomAbvGr,GarageYrBlt,GarageFinish,
        LotArea,CentralAir,BsmtFullBath,MasVnrArea,BsmtExposure,OverallCond,WoodDeckSF,MSZoning]]

        new_data=scalar.transform(data)
        output=regmodel.predict(new_data)
        print(output[0])

        return render_template('home.html',prediction_text="Your House price is Rs. {}".format(output))
                
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)