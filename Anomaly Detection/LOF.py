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
from sklearn.neighbors import LocalOutlierFactor

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
        x=len(df.columns)
        if x==1:
            # x = df.select_dtypes(include = ['float64','int64'])
            lof = LocalOutlierFactor()
            clusters = lof.fit_predict(df)
            anom_index = where(clusters == -1)
            values = df.iloc[anom_index]
            values = non_num.join(values, how='inner')
            values.to_csv(r'LOF_outliers.csv' ,index=True,header=True)

        else:
            lof = LocalOutlierFactor()
            clusters = lof.fit_predict(df)
            anom_index = where(clusters == -1)
            values = df.iloc[anom_index]
            outlier_index=list(values.index)

            pca = PCA(n_components=2)  # Reduce to k=3 dimensions
            scaler = StandardScaler()
            #normalize the metrics
            X = scaler.fit_transform(df)
            X_reduce = pca.fit_transform(X)

            ## 3D

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.set_zlabel("x_composite_3")
            # Plot the compressed data points
            ax.scatter(X_reduce[:, 0], X_reduce[:, 1], s=4, lw=1, label="inliers",c="green")
            # Plot x's for the ground truth outliers
            ax.scatter(X_reduce[outlier_index,0],X_reduce[outlier_index,1], lw=2, s=60, marker="x", c="red", label="outliers")
            ax.legend()
            plt.show()
            plt.savefig('D:\\Local Disk D\\Anomaly New Detect\\static\\img\\LOF_3D.png')

            ### 2D ####

            fig, ax = plt.subplots(figsize=(16,8))
            ax.scatter(X_reduce[:, 0], X_reduce[:, 1],s=4, lw=1, label="inliers",c="green")
            ax.scatter(X_reduce[outlier_index,0],X_reduce[outlier_index,1],lw=2, s=60, marker="x", c="red", label="outliers")
            ax.legend()
            plt.show()
            plt.savefig('D:\\Local Disk D\\Anomaly New Detect\\static\\img\\LOF_2D.png')


            values = non_num.join(values, how='inner')
            values.to_csv(r'LOF_outliers.csv',index=True,header=True)


        # Local Outlier Factor Method

   