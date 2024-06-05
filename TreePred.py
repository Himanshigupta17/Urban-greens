import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

def getPred(AQI,LAND,LAT,LONG,TEMP,HUM,POP,PERCP,TRAFFIC):
    data = pd.read_csv('nice.csv')

    # Data preprocessing
    X = data.drop(columns=['CITY/ DISTRICT', 'STATE', 'TREECOVER'])
    y = data['TREECOVER']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=39)

    # Create and train an XGBoost regressor
    model = xgb.XGBRegressor(objective='reg:squarederror', random_state=13)
    model.fit(X_train, y_train)

    # Now, you can use the trained model to make predictions for new input data
    input_data = {
        'AQI': [AQI],
        'LAND': [LAND],
        'LATTITUDE': [LAT],
        'LONGITUDE': [LONG],
        'WEATHER': [TEMP],
        'HUMIDITY': [HUM],
        'POPDENSE': [POP],
        'PERCIPITATION': [PERCP],
        'TRAFFIC': [TRAFFIC]
    }

    # Create a DataFrame from the input data
    input_df = pd.DataFrame(input_data)

    # Use the trained model to make predictions
    predictions = model.predict(input_df)

    # Print the predicted tree cover percentage
    with open("output.txt", "a") as file:
        expected_tree_percentage = round(predictions[0], 2)
        file.write(f"Expected Tree Percentage: " + str(expected_tree_percentage))