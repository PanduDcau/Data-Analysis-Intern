import json

import argparse
from pathlib import Path

from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler



##def _logistic_regression(args):


    
    # The excted data type is 'dict', however since the file
    # was loaded as a json object, it is first loaded as a string
    # thus we need to load again from such string in order to get 
    # the dict-type object.




if __name__ == '__main__':

    # Defining and parsing the command-line arguments
    parser = argparse.ArgumentParser(description='My program description')
    # parser.add_argument('--data', type=str)
    # parser.add_argument('--accuracy', type=str)
    #
    # args = parser.parse_args()

    # Creating the directory where the output file will be created (the directory may or may not exist).
    #Path(args.accuracy).parent.mkdir(parents=True, exist_ok=True)
    # Open and reads file "data"
    with open('../download_data/data.json', 'r') as data_file:
        data2 = json.load(data_file)

        # the dict-type object.
        s2 = json.dumps(data2)
        data = json.loads(s2)

        X, y = make_classification(random_state=42)
        x_train = data['x_train']
        y_train = data['y_train']
        x_test = data['x_test']
        y_test = data['y_test']

        # Initialize and train the model
        # model = LogisticRegression()
        # model.fit(x_train, y_train)

        pipe = make_pipeline(StandardScaler(), LogisticRegression())

        # Get predictions
       # y_pred = model.predict(x_test)
        pipe.fit(x_train, y_train)  # apply scaling on training data
        # Get accuracy
        #accuracy = accuracy_score(y_test, y_pred)
        p = pipe.score(x_test, y_test)  # apply scaling on testing data, without leaking training data
        # Save output into file
        with open('logistic_accuracy.json', 'w') as accuracy_file:
            accuracy_file.write(str(p))
    
    #_logistic_regression(args)