import pickle
from sklearn.naive_bayes import GaussianNB
from random import shuffle
from math import trunc
import numpy as np

def get_train_test_split(samples):
    shuffle(samples)
    num_samples = len(samples)
    cutoff_index = trunc(.8 * num_samples)
    train_samples = samples[:cutoff_index]
    test_samples = samples[cutoff_index:]
    return train_samples, test_samples

def save_model(model):
    pickle.dump(model, open("current_model.pickle", "wb"))

def get_samples(train_samples, test_samples):
    X = [s["processed"] for s in train_samples]
    Y = [s["category"] for s in train_samples]
    test_x = [s["processed"] for s in test_samples]
    test_y = [s["category"] for s in test_samples]
    return X, Y, test_x, test_y

def fit_model(X, Y):
    clf = GaussianNB()
    clf.fit(X, Y)
    return clf


def train(samples):
    train_samples, test_samples = get_train_test_split(samples)
    X, Y, test_x, test_y = get_samples(train_samples, test_samples)
    model = fit_model(X, Y)
    score = model.score(test_x, test_y)
    save_model(model)
    return score
