import numpy as np
from numpy import where
from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import IsolationForest
from pyod.models.knn import KNN
import json
from flask import send_from_directory
from flask import current_app
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
from sklearn.covariance import EllipticEnvelope

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
        x=len(data.columns)
        if x==1:
            # data_n=data_n.select_dtypes(include=['float64','int64'])
            
            model  =  EllipticEnvelope(contamination=0.01).fit(data)
            data['anomaly_score'] = model.predict(data)
            anomaly=data[data['anomaly_score']==-1]
            outlier_index=list(anomaly.index)
            anomaly = non_num.join(anomaly, how='inner')
            anomaly.to_csv("outlierss_mcd.csv")
                
            
        #### Plot the outliers

        
        else:
            model  =  EllipticEnvelope(contamination=0.01).fit(data)
            data['anomaly_score'] = model.predict(data)
            anomaly=data[data['anomaly_score']==-1]
            outlier_index=list(anomaly.index)
            pca = PCA(n_components=3)  # Reduce to k=3 dimensions
            scaler = StandardScaler()
            #normalize the metrics
            X = scaler.fit_transform(data)
            X_reduce = pca.fit_transform(X)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.set_zlabel("x_composite_3")
            # Plot the compressed data points
            ax.scatter(X_reduce[:, 0], X_reduce[:, 1], zs=X_reduce[:, 2], s=4, lw=1, label="inliers",c="green")
            # Plot x's for the ground truth outliers
            ax.scatter(X_reduce[outlier_index,0],X_reduce[outlier_index,1], X_reduce[outlier_index,2],lw=2, s=60, marker="x", c="red", label="outliers")
            ax.legend()
            plt.show()
            plt.savefig('D:\\Local Disk D\\Anomaly New Detect\\static\\img\\MCD_3D.png')

            fig, ax = plt.subplots(figsize=(16,8))
            ax.scatter(X_reduce[:, 0], X_reduce[:, 1],s=4, lw=1, label="inliers",c="green")
            ax.scatter(X_reduce[outlier_index,0],X_reduce[outlier_index,1],lw=2, s=60, marker="x", c="red", label="outliers")
            ax.legend()
            plt.show()
            plt.savefig('D:\\Local Disk D\\Anomaly New Detect\\static\\img\\MCD_2D.png')

            anomaly = non_num.join(anomaly, how='inner')
            anomaly.to_csv("outlierss_isolation.csv")
        
        # Minimum Covariance Determinant Method
