import numpy as np
from numpy import where
from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import IsolationForest
from pyod.models.knn import KNN
import json
from flask import send_from_directory
from flask import current_app

app = Flask(__name__)


class Mcd:
    def __init__(self, file, non_num):
        self.file = file
        self.non_num = non_num

    def createOutliers(self):
        anomaly=pd.DataFrame()
        data=pd.DataFrame(self.file)
        non_num=pd.DataFrame(self.non_num)
        data.dropna(axis=0,inplace=True)
        # data=data.select_dtypes(include=['float64','int64'])
        from sklearn.covariance import EllipticEnvelope
        model  =  EllipticEnvelope(contamination=0.01).fit(data)
        data['anomaly_score'] = model.predict(data)
        anomaly=data[data['anomaly_score']==-1]
        anomaly = non_num.join(anomaly, how='inner')
        anomaly.to_csv("outlierss_mcd.csv")

        # Minimum covariance determinant Method

   