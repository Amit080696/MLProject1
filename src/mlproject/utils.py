import os   # to help to get current directory path
import sys  # for custum exception and logging handling 
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
import pymysql
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


import pickle
import numpy as np

from dotenv import load_dotenv
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established", mydb)
        df=pd.read_sql_query("select * from studentsdata", mydb)
        print(df.head())

        return df
    
    except Exception as e:
        raise CustomException(e)

def save_object(filepath, obj):
    try:
        dir_path=os.path.dirname(filepath)

        os.makedirs(dir_path, exist_ok=True)

        with open(filepath, 'wb') as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(sys,e)
    
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)