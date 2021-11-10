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
conda create --name Anomaly_detect python=3.8
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
1. Install Docker Application in your Pc based on your Os Version
```
Download Link :- https://docs.docker.com/desktop/windows/install/
```

2. After Installing Docker , in your terminal create a New Image
```
docker build -t anomaly .
```
Make sure the image name is in lowercase.

3.  Image is Created and run the image in a New Docker Container
 Caution :- Uncomment the app.run in the app.py which includes the port no.
Also comment the Debug=True app.run

Deploying the Container
```
docker run -p 8080:8080 {image-name}
```
Our {image-name} is anomaly

