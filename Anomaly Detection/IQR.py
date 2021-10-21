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


class Iqr:
    def __init__(self, file, non_num):
        self.file = file
        self.non_num = non_num

    def createOutliers(self):

        # anomaly=pd.DataFrame()
        data = pd.DataFrame(self.file)
        non_num=pd.DataFrame(self.non_num)
        data.dropna(axis=0,inplace=True)
        # data=data.select_dtypes(include=['float64','int64'])
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        IQR_Out = data[((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]
        IQR_Out = non_num.join(IQR_Out, how='inner')
        IQR_Out.to_csv(r'IQR_Outlier.csv')
        # IQR Method

    