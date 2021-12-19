# Kubeflow for ML Scipts

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) , Tensorflow (Deep Learning) & xgboost installed.

### Project Structure
This project has five major parts :

1. DataCleaning.py - This contains code for our Machine Learning model to apply mlfows for the Selected "csv file" in Config file.
```
config.ini file - two Types 
1) Classification
2) Regression
```
#### Changing the type in config.ini needed for run Regression and Classifcation .py files seperately. 
2. ElasticNet regression.py - This contains code for Regression analysis for the Selected data Set.

3. GB_Regression/Classifiaction.py - This contains code for Regression & Classification analysis for the Selected data Set and create Mlflow Models.

4. Tensorflow LTSM.py - This contains code for Deep Learning analysis for the Selected data Set and create Mlflow Models.

5. XG Boost Regression/Classification - This code contains Regression & Classification analysis of data using XGboost .

### Install Anaconda
configure the Jupyter Notebook to create a Enviornment for the Project

### Install Python Environment
```
conda create --name mlflow python=3.8 64bits
```

### Install Libraries from requirements.txt
```
requirements.txt
```

### Running the project
##### Make sure config.ini file configured for relevent type.

1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python GB Regression.py
```
2. Run mlflow ui for evaluate model
```
mlflow ui
```

By default, mlflow will run on port 5000.

3. Navigate to URL http://localhost:5000




