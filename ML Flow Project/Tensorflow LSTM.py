"""Trains and evaluate a simple MLP
on the Reuters newswire topic classification task.
"""
import numpy as np
import tensorflow
from tensorflow import keras
from tensorflow.keras.datasets import reuters
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.wrappers.scikit_learn import KerasClassifier

# The following import and function call are the only additions to code required
# to automatically log metrics and parameters to MLflow.

import mlflow.keras
import DataCleaning

mlflow.keras.autolog()


def create_model(dense_l1, dense_l2, meta):
    n_features_in_ = meta["n_features_in_"]
    X_shape_ = meta["X_shape_"]
    n_classes_ = meta["n_classes_"]

    model = Sequential()
    model.add(Dense(n_features_in_, input_shape=X_shape_[1:], activation="relu"))
    model.add(Dense(dense_l1, activation="relu"))
    model.add(Dense(dense_l2, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))

    return model


if __name__ == "__main__":
    max_words = 1000
    batch_size = 32
    epochs = 100

    print("Loading data...")
    le = LabelEncoder()
    # Split the data into training and test sets. (0.75, 0.25) split.
    out = DataCleaning.Dataclean()
    data, X_train, X_test, y_train, y_test = out.cleandata()

    print(len(X_train), "train sequences")
    print(len(X_test), "test sequences")

    num_classes = int(np.max(y_train)) + 1
    print(num_classes, "classes")

    print("Vectorizing sequence data...")
    tokenizer = Tokenizer(num_words=max_words)
    # x_train = tokenizer.sequences_to_matrix(x_train)
    # x_test = tokenizer.sequences_to_matrix(x_test)
    print("x_train shape:", X_train.shape)
    print("x_test shape:", X_test.shape)

    print("Convert class vector to binary class matrix " "(for use with categorical_crossentropy)")
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    print("y_train shape:", y_train.shape)
    print("y_test shape:", y_test.shape)

    print("Building model...")
    model = Sequential()
    model.add(Dense(units=4, input_dim=X_train.shape[1]))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation("softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    history = model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)
    score = model.evaluate(X_test, y_test, batch_size=batch_size, verbose=1)
    print("Test score:", score[0])
    print("Test accuracy:", score[1])

from sklearn.pipeline import Pipeline
