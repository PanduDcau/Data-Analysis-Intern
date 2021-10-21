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


class Svm:
    def __init__(self, file, non_num):
        self.file = file
        self.non_num = non_num

  
    def createOutliers(self):
        from sklearn.svm import OneClassSVM
        from numpy import quantile, where, random
        anomaly=pd.DataFrame()
        data=pd.DataFrame(self.file)
        non_num=pd.DataFrame(self.non_num)
        # data=data.select_dtypes(include=['float64','int64'])
        data.dropna(axis=0,inplace=True)
        svm = OneClassSVM(kernel='rbf', gamma=0.001,nu=0.03)
        svm.fit(data)
        pred = svm.predict(data)
        anom_index = where(pred==-1)
        anomaly = data.iloc[anom_index]
        anomaly = non_num.join(anomaly, how='inner')
        anomaly.to_csv("outlierss_svm.csv")  
        # SVM Method

  