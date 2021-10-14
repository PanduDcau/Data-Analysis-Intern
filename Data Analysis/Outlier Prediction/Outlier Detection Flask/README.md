## ML-Model-Flask-Deployment
This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API

### Prerequisites
You must have Scikit Learn, Pandas, Flask,Pyod (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has one major part :
1. out.py - This contains code fot our Machine Learning model to predict the Outliers of a Given csv Files.

Use the requirements.txt file to download relevant Packages

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python out.py
```

By default, flask will run on port 5000.

2. Navigate to URL http://localhost:5000

3. Then Provide the Relevant Csv file to FInd the Outliers.

4. After Selecting a Particular Method for Outlying Detection , output file given with Anamolies as an Output.
