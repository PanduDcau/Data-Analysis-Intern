import numpy as np
from flask import Flask, request, jsonify, render_template, redirect
import pandas as pd
from sklearn.ensemble import IsolationForest
import json
from flask import send_from_directory
from flask import current_app
from flask import flash
import IQR
import ISOLATION
import SVM
import MCD
import LOF
import KNN
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

import os

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir,exist_ok=True)

@app.route('/')
def upload1():
    return render_template('upload.html')


@app.route('/Check')
def Check():
    return render_template('Check.html')


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save(os.path.join(uploads_dir, 'upload.csv'))
    if not f:
        return"Please upload the csv file"
    else:
        df = pd.read_csv('D:\\Local Disk D\\Anomaly New Detect\\upload.csv')
        num_cols = list(df._get_numeric_data().columns.values.tolist())
        sns.set()
        color = dict(boxes="#287D8EFF", whiskers="#B43757",medians='DarkBlue', caps='Gray')
        ax = df[num_cols].plot(kind='box',figsize=(16,9),color=color,vert=False,patch_artist=True)
        plt.xticks(rotation = 45)
        plt.title("Box Plots of Numeric Columns")
        plt.ylabel("Variable Names")
        plt.xlabel("Frequency")    
           
        plt.savefig('D:\\Local Disk D\\Anomaly New Detect\\static\\img\\new_plot.png')
            
        summary=df.describe()
        
    return render_template('Check.html', prediction_text2=num_cols , data1 = df.head(20).to_html(),data2 = summary.to_html(),name = 'Box Plots of Numeric Variables', url ='/static/img/new_plot.png')


@app.route('/Check2', methods=['POST'])
def Check2():
    #import findspark
    #findspark.init()
    #import pyspark
    #from pyspark.sql import SparkSession
    #spark = SparkSession.builder.appName("Practise").getOrCreate()
    #df = spark.read.csv('C:\\Users\\Acer\\Outlier app\\instance\\uploads\\upload.csv',header = True, inferSchema=True)
    #df=df.toPandas()

    df=pd.read_csv('D:\\Local Disk D\\Anomaly New Detect\\instance\\uploads\\upload.csv')
    num_cols = list(df._get_numeric_data().columns.values.tolist())

    int_features = [float(x) for x in request.form.get('outlier')]

    columns = request.form.getlist('check01')
    if 'Whole_Data_Set' in columns:
        data = df[num_cols]
    else:
        data = df[columns]

    non_num = df.select_dtypes(include='object')

    if int_features[0] == 0:
        # IQR Method
        out = IQR.Iqr(data, non_num)
        out.createOutliers()
        return send_from_directory(directory=current_app.root_path, path="IQR_Outlier.csv")

    elif int_features[0] == 1:
        # Isolation forest Method
        out1 = ISOLATION.Isolation(data, non_num)
        out1.createOutliers()
        return send_from_directory(directory=current_app.root_path, path="outlierss_isolation.csv")

    elif int_features[0] == 4:
        # SVM Method
        out4 = SVM.Svm(data, non_num)
        out4.createOutliers()
        return send_from_directory(directory=current_app.root_path, path="outlierss_svm.csv")

    elif int_features[0] == 2:
        # Minimum covariance determinant Method
        out2 = MCD.Mcd(data, non_num)
        out2.createOutliers()
        return send_from_directory(directory=current_app.root_path, path="outlierss_mcd.csv")

    elif int_features[0] == 3:
        # Local Outlier Factor Method
        out3 = LOF.Lof(data, non_num)
        out3.createOutliers()
        return send_from_directory(directory=current_app.root_path, path="LOF_outliers.csv")

    elif int_features[0] == 5:

        # KNN Method
        out5 = KNN.Knn(data, non_num)
        out5.createOutliers()
        return send_from_directory(directory=current_app.root_path, path="KNN_outliers.csv")


if (__name__ == "__main__"):
    app.run(debug=True)
