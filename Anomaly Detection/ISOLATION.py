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


class Isolation:
    def __init__(self, file, non_num):
        self.file = file
        self.non_num = non_num

    def createOutliers(self):
        anomaly=pd.DataFrame()
        data_n=pd.DataFrame(self.file)
        non_num=pd.DataFrame(self.non_num)
        data_n.dropna(axis=0,inplace=True)
        # data_n=data_n.select_dtypes(include=['float64','int64'])
        model  =  IsolationForest(n_estimators=50, max_samples=500, contamination=.01, bootstrap=False, n_jobs=1, random_state=1, verbose=0, warm_start=False).fit(data_n)
        data_n['anomaly_score'] = model.predict(data_n)
        anomaly=data_n[data_n['anomaly_score']==-1]
        anomaly = non_num.join(anomaly, how='inner')
        anomaly.to_csv("outlierss_isolation.csv")
				
        # Isolation forest Method

   