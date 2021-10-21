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

app = Flask(__name__)


@app.route('/')
def upload1():
    return render_template('upload.html')


@app.route('/Check')
def Check():
    return render_template('Check.html')


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    if not f:
        return"Please upload the csv file"
    else:
        df = pd.read_csv(f)
        num_cols = list(df._get_numeric_data().columns.values.tolist())
        length = len(num_cols)
    return render_template('Check.html', prediction_text2=num_cols, prediction_text3=length)


@app.route('/Check2', methods=['POST'])
def Check2():
    f = request.files['file']
    if not f:
        return "No file is available.Please enter a valid csv file"
    else:
        df = pd.read_csv(f)
        num_cols = list(df._get_numeric_data().columns.values.tolist())

        int_features = [float(x) for x in request.form.get('outlier')]

        columns = request.form.getlist('vehicle1')
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

        elif int_features[0] == 2:
            # SVM Method
            out4 = SVM.Svm(data, non_num)
            out4.createOutliers()
            return send_from_directory(directory=current_app.root_path, path="outlierss_svm.csv")

        elif int_features[0] == 3:
            # Minimum covariance determinant Method
            out2 = MCD.Mcd(data, non_num)
            out2.createOutliers()
            return send_from_directory(directory=current_app.root_path, path="outlierss_mcd.csv")

        elif int_features[0] == 4:
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
