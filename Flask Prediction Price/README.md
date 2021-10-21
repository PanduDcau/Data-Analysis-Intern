# Car-Price-Prediction

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has two major parts :
1. app.py - This contains code fot our Machine Learning model to predict Car_Auctioning Prices with Training data in 'car_data.csv' file.
```
Download it from Kaggle.com
```
### Install Anaconda
configure the Jupyter Notebook to create a Enviornment for the Project

### Install Python Environment
```
conda create --name CarPrice_Predict python=3.6
```

### Install Libraries from requirements.txt
```
requirements.txt
```
### Run the Jupyter File and Create a Pickle FIle
```
jupyter notebook > Car.ipynb
```

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python main.py
```
2. Run main.py using below command to start Flask API
```
python app.py
```

By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000




