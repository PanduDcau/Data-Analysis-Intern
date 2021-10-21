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


class Lof:
    def __init__(self, file, non_num):
        self.file = file
        self.non_num = non_num


    def createOutliers(self):
        from numpy import quantile, where, random
        import pandas as pd
        anomaly = pd.DataFrame()
        df = pd.DataFrame(self.file)
        non_num=pd.DataFrame(self.non_num)
        df.dropna(axis = 0, inplace = True)
        # x = df.select_dtypes(include = ['float64','int64'])
        from sklearn.neighbors import LocalOutlierFactor
        lof = LocalOutlierFactor()
        clusters = lof.fit_predict(df)
        anom_index = where(clusters == -1)
        values = df.iloc[anom_index]
        values = non_num.join(values, how='inner')
        values.to_csv(r'LOF_outliers.csv' ,index=True,header=True)

        # Local Outlier Factor Method

   