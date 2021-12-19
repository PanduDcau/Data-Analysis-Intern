import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


class Dataclean:
    def cleandata(self):
        # data = pd.read_csv('abalone.csv')

        # Read the configuration file
        import configparser
        config = configparser.ConfigParser()
        config.read(r'config.ini')
        df = config.get('dataset', 'input_path_1')
        response = config.get('response', 'input_path_2')
        data = pd.read_csv(df)
        # dropping all the missing values
        data.dropna(axis=0, inplace=True)
        le = LabelEncoder()
        # Split the data into training and test sets. (0.75, 0.25) split.
        non_num = list(data.select_dtypes(include='object'))
        if len(non_num) == 0:
            data = data
        else:
            data[non_num] = data[non_num].apply(lambda col: le.fit_transform(col))

        X = data.drop(response, axis=1)
        y = data[response]
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=42)
        return data, X_train, X_test, y_train, y_test


# if __name__ == "__main__":
#     Dataclean.cleandata()
