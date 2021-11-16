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
matplotlib.use('Agg')  ### To show the plot in frontend via backend
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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


@app.route('/upload', methods=['POST'])   ## Boxplot appears in frontend
def upload():
    f = request.files['file']
    f.save(os.path.join(uploads_dir, 'upload.csv'))
    if not f:
        return"Please upload the csv file"
    else:
        df = pd.read_csv('D:\\Local Disk D\\Anomaly New Detect\\instance\\uploads\\upload.csv')
        num_cols = list(df._get_numeric_data().columns.values.tolist())
        non_num_cols = list(df.select_dtypes(include='object'))
        sns.set()
        color = dict(boxes="#287D8EFF", whiskers="#B43757",medians='DarkBlue', caps='Gray')
        ax = df[num_cols].plot(kind='box',figsize=(16,9),color=color,vert=False,patch_artist=True)
        plt.xticks(rotation = 45)
        plt.ylabel("Variable Names")
        plt.xlabel("Frequency")    
        plt.savefig('D:\\Local Disk D\\Anomaly New Detect\\static\\img\\new_plot.png')
        summary=df.describe()
        shape=df.shape
    return render_template('Check.html', prediction_text2=num_cols ,prediction_text3=non_num_cols, data1 = df.head(20).to_html(),
    data2 = summary.to_html(),name = 'Box Plots of Numeric Variables', url ='/static/img/new_plot.png',shape1=shape)



@app.route('/Check2', methods=['POST'])  ## Section 03
def Check2():

    df=pd.read_csv('D:\\Local Disk D\\Anomaly New Detect\\instance\\uploads\\upload.csv')

    num_cols = list(df._get_numeric_data().columns.values.tolist())
    int_features = [float(x) for x in request.form.get('outlier')]

    columns = request.form.getlist('check01')
    if 'Whole_Data_Set' in columns:
        data = df[num_cols]
    else:
        data = df[columns]

    non_num_columns = list(df.select_dtypes(include='object'))

    selected_non_nom_columns=request.form.getlist('check02')

    if 'Whole_Non_Numeric' in selected_non_nom_columns:
        non_num = df[non_num_columns]
    else:
        non_num = df[selected_non_nom_columns]

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

@app.route('/Check3', methods=['POST'])   ## Section 01
def Check3():

    df=pd.read_csv('D:\\Local Disk D\\Anomaly New Detect\\instance\\uploads\\upload.csv')

    int_features = [float(x) for x in request.form.get('outlier')]

    columns = request.form.getlist('check01')
    if 'Whole_Data_Set' in columns:
        data = df[num_cols]
    else:
        data = df[columns]

    selected_non_nom_columns=request.form.getlist('check02')

    if 'Whole_Non_Numeric' in selected_non_nom_columns:
        non_num = df[non_num_columns]
    else:
        non_num = df[selected_non_nom_columns]


    if int_features[0] == 0:
        # IQR Method
        out = IQR.Iqr(data, non_num)
        out.createOutliers()
        return render_template('photo.html', url_2 ='/static/img/IQR_3D.png' , url_3 ='/static/img/IQR_2D.png')

    elif int_features[0] == 1:
        
        # Isolation forest Method
        out1 = ISOLATION.Isolation(data, non_num)
        out1.createOutliers()
        return render_template('photo.html', url_2 ='/static/img/isolation_3D.png' , url_3 ='/static/img/isolation_2D.png')
    

    elif int_features[0] == 2:
        # Minimum covariance determinant Method
        out2 = MCD.Mcd(data, non_num)
        out2.createOutliers()
        return render_template('photo.html', url_2 ='/static/img/MCD_3D.png' , url_3 ='/static/img/MCD_2D.png')

    elif int_features[0] == 3:
        # Local Outlier Factor Method
        out3 = LOF.Lof(data, non_num)
        out3.createOutliers()
        return render_template('photo.html', url_2 ='/static/img/LOF_3D.png', url_3 ='/static/img/LOF_2D.png' )

    elif int_features[0] == 5:
        # KNN
        out5 = KNN.Knn(data, non_num)
        out5.createOutliers()
        return render_template('photo.html', url_2 ='/static/img/KNN_3D.png' , url_3 ='/static/img/KNN_2D.png')

    elif int_features[0] == 4:
        # SVM
        out4 = SVM.Svm(data, non_num)
        out4.createOutliers()
        return render_template('photo.html', url_2 ='/static/img/SVM_3D.png' , url_3 ='/static/img/SVM_2D.png')
        



@app.route('/Check4', methods=['POST'])     ### Section 02
def Check4():

    df=pd.read_csv('D:\\Local Disk D\\Anomaly New Detect\\instance\\uploads\\upload.csv')

    int_features = [float(x) for x in request.form.get('outlier12')]
    num_columns = request.form.get('check12')
    selected_non_nom_columns_visual=request.form.get('check23')
    
    df1=df[[num_columns,selected_non_nom_columns_visual]]
    df1=pd.DataFrame(df1.groupby(selected_non_nom_columns_visual).sum())
    df1=df1.reset_index()
    data=df1.drop([selected_non_nom_columns_visual],axis=1)

    if int_features[0] == 0:
        # IQR Method
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        df1['IQR'] = data[((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]
        fig = px.scatter(df1, x=selected_non_nom_columns_visual, y=num_columns, color="IQR",title="Anomaly Investigation With IQR" )
        fig.show()
        return render_template('photo.html', url_2 ='/static/img/anomaly.png')


    elif int_features[0] == 1:
        # Isolation forest Method
        model  =  IsolationForest(n_estimators=50, max_samples=500, contamination=.01, bootstrap=False, n_jobs=1, random_state=1, verbose=0, warm_start=False).fit(data)
        df1['anomaly_score'] = model.predict(data)
        fig = px.scatter(df1, x=selected_non_nom_columns_visual, y=num_columns, color="anomaly_score",title="Anomaly Investigation with Isolation Forest" )
        fig.show()
        return render_template('photo.html', url_2 ='/static/img/anomaly.png')

    elif int_features[0] == 2:
        # Minimum covariance determinant Method
        from sklearn.covariance import EllipticEnvelope
        model  =  EllipticEnvelope(contamination=0.01).fit(data)
        df1['anomaly_score'] = model.predict(data)
        fig = px.scatter(df1, x=selected_non_nom_columns_visual, y=num_columns, color="anomaly_score",title="Anomaly Investigation with MCD" )
        fig.show()
        return render_template('photo.html', url_2 ='/static/img/anomaly.png')

    elif int_features[0] == 3:
        # Local Outlier Factor Method
        from sklearn.covariance import EllipticEnvelope
        model  =  EllipticEnvelope(contamination=0.01).fit(data)
        df1['anomaly_score'] = model.predict(data)
        fig = px.scatter(df1, x=selected_non_nom_columns_visual, y=num_columns, color="anomaly_score",title="Anomaly Investigation with LOF" )
        fig.show()
        return render_template('photo.html', url_2 ='/static/img/anomaly.png')


    elif int_features[0] == 5:

        # KNN Method
        from pyod.models.knn import KNN
        clf = KNN()
        clf.fit(data)
        outlier = clf.labels_
        df1['Cluster_index'] = outlier
        fig = px.scatter(df1, x=selected_non_nom_columns_visual, y=num_columns, color="Cluster_index",title="Anomaly Investigation with KNN" )
        fig.show()
        return render_template('photo.html', url_2 ='/static/img/anomaly.png')


    elif int_features[0] == 4:
        # SVM Method
        from sklearn.svm import OneClassSVM
        svm = OneClassSVM(kernel='rbf', gamma=0.001,nu=0.03)
        svm.fit(data)
        pred = svm.predict(data)
        df1['anomaly_score'] = pred
        fig = px.scatter(df1, x=selected_non_nom_columns_visual, y=num_columns, color="anomaly_score",title="Anomaly Investigation with One Class SVM" )
        fig.show()
        return render_template('photo.html', url_2 ='/static/img/anomaly.png')





if (__name__ == "__main__"):
    #app.run(debug=True)
    app.run(host = '0.0.0.0', port = port)
