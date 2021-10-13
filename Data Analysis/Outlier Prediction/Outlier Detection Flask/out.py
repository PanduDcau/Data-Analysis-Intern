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

# Root URL
@app.route('/')
def index1():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@app.route('/index', methods=['POST'])
def index():
    f = request.files['file']
    if not f:
        return "No file is available.Please enter a valid csv file"
    else:
        int_features = [float(x) for x in request.form.values()]
        if int_features[0]==0:

            def outl(f):
                anomaly = pd.DataFrame()
                df = pd.read_csv(f)
                df.dropna(axis = 1,inplace = True)
                x = df.select_dtypes(include=['float64','int64'])
                Q1 = x.quantile(0.25)
                Q3 = x.quantile(0.75)
                IQR = Q3 - Q1
                IQR_Out = x[((x < (Q1 - 1.5 * IQR)) |(x > (Q3 + 1.5 * IQR))).any(axis=1)]
                IQR_Out.to_csv("Quantile_Outlier.csv")
                # IQR Method

        elif int_features[0]==1:

            def outl(f):
                anomaly = pd.DataFrame()
                df = pd.read_csv(f)
                df.dropna(axis=1,inplace=True)
                x = df.select_dtypes(include=['float64','int64'])
                model  =  IsolationForest(n_estimators=50, max_samples=500, contamination=.01, max_features=2, bootstrap=False, n_jobs=1, random_state=1, verbose=0, warm_start=False).fit(x)
                x['anomaly_score'] = model.predict(x)
                anomaly = x[x['anomaly_score']==-1]
                anomaly.to_csv("IsolationForest_Outlier.csv")
                # Isolation forest Method

        elif int_features[0]==2:

            def outl(f):
                anomaly = pd.DataFrame()
                df = pd.read_csv(f)
                from sklearn.covariance import EllipticEnvelope
                df.dropna(axis = 1,inplace = True)
                x = df.select_dtypes(include=['float64','int64'])
                model2  =  EllipticEnvelope(contamination=0.01).fit(x)
                x['anomaly_score'] = model2.predict(x)
                anomaly = x[x['anomaly_score']==-1]
                anomaly.to_csv("CovarianceDeterminent_Outlier.csv")
                # Minimum covariance determinant Method

        elif int_features[0]==3:

            def outl(f):
                import pandas as pd
                anomaly = pd.DataFrame()
                df = pd.read_csv(f)
                df.dropna(axis = 1, inplace = True)
                x = df.select_dtypes(include = ['float64','int64'])
                from sklearn.neighbors import LocalOutlierFactor
                lof = LocalOutlierFactor()
                clusters = lof.fit_predict(x)
                anom_index = where(clusters == -1)
                values = x.iloc[anom_index]
                values.to_csv("Factor_Outliers.csv")
                # Local Outlier Factor Method

        elif int_features[0]==4:

            def outl(f):
                anomaly = pd.DataFrame()
                df = pd.read_csv(f)
                from sklearn.svm import OneClassSVM
                svm = OneClassSVM(kernel='rbf', gamma=0.001, nu=0.03)
                df.dropna(axis = 1,inplace = True)
                x = df.select_dtypes(include=['float64','int64'])
                svm_1 = svm.fit(x)
                pred = svm_1.predict(x)
                anom_index = where(pred==-1)
                values = x.iloc[anom_index]
                values.to_csv("SVM_Outliers.csv")
                # SVM Method

        elif int_features[0]==5:

            def outl(f):
                anomaly = pd.DataFrame()
                df = pd.read_csv(f)
                df.dropna(axis = 0, inplace = True)
                x = df.select_dtypes(include = ['float64','int64'])
                clf = KNN()
                clf.fit(x)
                outlier = clf.labels_
                anom_index = where(outlier == 1)
                values = x.iloc[anom_index]
                values.to_csv("KNN_Outliers.csv")
                # KNN Method
  
    outl(f)
    return send_from_directory( directory=current_app.root_path,path="outlierss.csv")


if (__name__ == "__main__"):
    app.run(debug=True)