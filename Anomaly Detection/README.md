# Anomaly Detection System

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has two major parts :
1. app.py - This contains code fot our Outlier-Detection model to predict Anomalies with Training data in given'.csv' file with Specified Column.
```
Select a .csv file and Specify Column to get the Anamolies
```
### Install Anaconda
configure the Jupyter Notebook to create a Enviornment for the Project

### Install Python Environment
```
conda create --name CarPrice_Predict python=3.8
```

### Install Libraries from requirements.txt
```
requirements.txt
```

### Running the project

1. Run main.py using below command to start Flask API
```
python app.py
```

By default, flask will run on port 5000.

2. Navigate to URL http://localhost:5000


### Dockerizing The Application