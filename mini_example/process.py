import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import csv
import random
from math import trunc
import matplotlib.pyplot as plt

output_conversion_dict = {
    1: "too hot",
    2: "just right",
    3: "too cold"
}

def convert(row):
    if row["response"] == "too hot": return [1, int(row["temp"])]
    if row["response"] == "just right": return [2, int(row["temp"])]
    if row["response"] == "too cold": return [3, int(row["temp"])]

def convert_response_to_int():
    with open("raw_data.csv", "r") as f:
        reader = csv.DictReader(f)
        converted = [convert(row) for row in reader]
    return converted


def get_train_test_split(samples):
    random.shuffle(samples)
    num_samples = len(samples)
    cutoff_index = trunc(.8 * num_samples)
    train_samples = samples[:cutoff_index]
    test_samples = samples[cutoff_index:]
    return train_samples, test_samples    

def get_samples(train_samples, test_samples):
    train_X = [[s[1]] for s in train_samples]
    train_Y = [s[0] for s in train_samples]
    test_x = [[s[1]] for s in test_samples]
    test_y = [s[0] for s in test_samples]
    return train_X, train_Y, test_x, test_y

prepared_data = convert_response_to_int()

train_samples, test_samples = get_train_test_split(prepared_data)

train_X, train_Y, test_x, test_y = get_samples(train_samples, test_samples)

model = DecisionTreeClassifier()
model.fit(train_X, train_Y)
score = model.score(test_x, test_y)
print(score)
tree.plot_tree(model)
plt.show()
