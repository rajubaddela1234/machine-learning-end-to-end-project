import mlflow
import mlflow.sklearn
from sklearn.metrics import r2_score
import pickle
import numpy as np

# Load the model and scaler
regmodel = pickle.load(open('reg.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Example data for prediction
data = np.array([[7, 2, 2, 5, 1710, 2, 3, 2, 856, 856, 0, 3, 706, 2003, 548, 5, 0, 8, 2003, 3, 2003, 2, 8450, 1, 1, 196, 3, 5, 0, 3]])

# Transform the data
new_data = scalar.transform(data)

# Make a prediction
prediction = regmodel.predict(new_data)

# Example true value for r2_score calculation
true_value = [200000]  # Replace with actual true value

# Calculate r2_score
r2 = r2_score(true_value, prediction)

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5001")
    mlflow.set_experiment("my_experiment")

    with mlflow.start_run():
        mlflow.log_param("OverallQual", 7)
        mlflow.log_param("GarageCars", 2)
        mlflow.log_param("ExterQual", 2)
        mlflow.log_param("Neighborhood", 5)
        mlflow.log_param("GrLivArea", 1710)
        mlflow.log_param("KitchenQual", 2)
        mlflow.log_param("BsmtQual", 3)
        mlflow.log_param("FullBath", 2)
        mlflow.log_param("1stFlrSF", 856)
        mlflow.log_param("TotalBsmtSF", 856)
        mlflow.log_param("2ndFlrSF", 0)
        mlflow.log_param("FireplaceQu", 3)
        mlflow.log_param("BsmtFinSF1", 706)
        mlflow.log_param("YearBuilt", 2003)
        mlflow.log_param("GarageArea", 548)
        mlflow.log_param("GarageType", 5)
        mlflow.log_param("Fireplaces", 0)
        mlflow.log_param("TotRmsAbvGrd", 8)
        mlflow.log_param("YearRemodAdd", 2003)
        mlflow.log_param("BedroomAbvGr", 3)
        mlflow.log_param("GarageYrBlt", 2003)
        mlflow.log_param("GarageFinish", 2)
        mlflow.log_param("LotArea", 8450)
        mlflow.log_param("CentralAir", 1)
        mlflow.log_param("BsmtFullBath", 1)
        mlflow.log_param("MasVnrArea", 196)
        mlflow.log_param("BsmtExposure", 3)
        mlflow.log_param("OverallCond", 5)
        mlflow.log_param("WoodDeckSF", 0)
        mlflow.log_param("MSZoning", 3)

        mlflow.log_metric("r2_score", r2)
        mlflow.sklearn.log_model(regmodel, "model")

    print("MLflow setup completed.")