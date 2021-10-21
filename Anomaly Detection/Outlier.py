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


class Detect:
    def __init__(self, file, non_num):
        self.file = file
        self.non_num = non_num

    def IQR(self):

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

    def isolation(self):
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

    def mcd(self):
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

    def local(self):
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

    def SVM(self):
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

    def KNN(self):
        import pandas as pd
        from numpy import quantile, where, random
        anomaly = pd.DataFrame()
        df = pd.DataFrame(self.file)
        non_num=pd.DataFrame(self.non_num)
        df.dropna(axis = 0, inplace = True)
        # x = df.select_dtypes(include = ['float64','int64'])
        from pyod.models.knn import KNN
        clf = KNN()
        clf.fit(df)
        outlier = clf.labels_
        anom_index = where(outlier == 1)
        values = df.iloc[anom_index]
        values= non_num.join(values, how='inner')
        values.to_csv(r'KNN_outliers.csv' ,index=True,header=True)
        # KNN Method
