import json
import os

import argparse
from pathlib import Path

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

##def _decision_tree(args):

    # Open and reads file "data"
    # with open(args.data) as data_file:
    #     data = json.load(data_file)

    # The excted data type is 'dict', however since the file
    # was loaded as a json object, it is first loaded as a string
    # thus we need to load again from such string in order to get 




if __name__ == '__main__':

    # Defining and parsing the command-line arguments
    parser = argparse.ArgumentParser(description='My program description')
    # parser.add_argument('--data', type=str)
    # parser.add_argument('--accuracy', type=str)

    #args = parser.parse_args()

    # Creating the directory where the output file will be created (the directory may or may not exist).
    # Path(args.accuracy).parent.mkdir(parents=True, exist_ok=True)
    #os.makedirs("D:\\Local Disk D\\Kubeflow_Pipeline\\decision_tree", exist_ok=True)

    # Open and reads file "data"
    with open('../download_data/data.json', 'r') as data_file:
        data2 = json.load(data_file)
       # print(data)

        # the dict-type object.
        s1 = json.dumps(data2)
        data = json.loads(s1)

        x_train = data['x_train']
        y_train = data['y_train']
        x_test = data['x_test']
        y_test = data['y_test']

        # Initialize and train the model
        model = DecisionTreeClassifier(max_depth=3)
        model.fit(x_train, y_train)

        # Get predictions
        y_pred = model.predict(x_test)

        # Get accuracy
        accuracy = accuracy_score(y_test, y_pred)

        # Save output into file
        with open('accuracy.json', 'w') as accuracy_file:
            accuracy_file.write(str(accuracy))
    #_decision_tree(args);
