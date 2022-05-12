import joblib
import matplotlib.pyplot as plt
import pandas
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

'''
atrybuty w pliku csv muszą być integerami, wstępnie ustaliłem:
season = {"wiosna": 1, "lato": 2, "jesien":3, "zima":4}
enough_space_in_trashmaster = { "no": 1, "yes":2}
time_since_flush = [1,2,3,4,5,6,7,8,9,10]
type_of_trash = {"bio":1, "szklo":2, "plastik":3, "papier":4, "mieszane":5}
access_to_bin = { "no":1, "yes":2}
distance = [1,2,3,4,5,6,7,8,9,10]
decision = [0,1] - decyzje zostaną zmienione z tych z wagami na zero jedynkowe ze względu na pewne trudności w dalszej pracy
'''
decisions = ["decision"]
attributes = ["season", "enough_space_in_trashmaster", "time_since_flush", "type_of_trash", "access_to_bin", "distance"]


# return tree made from attributes
def tree():
    dataset = pandas.read_csv('./decision_tree/drzewo_decyzyjne.csv')

    x = dataset[attributes]
    y = dataset[decisions]
    decision_tree = DecisionTreeClassifier()
    decision_tree = decision_tree.fit(x, y)

    return decision_tree


# return decision made from tree and attributes
def decision(decision_tree, season, enough_space_in_trashmaster, time_since_flush, type_of_trash, access_to_bin,
             distance):
    decision = decision_tree.predict(
        [[season, enough_space_in_trashmaster, time_since_flush, type_of_trash, access_to_bin, distance]])

    return decision


'''
we shall save output of our decision tree. It is possible for a few ways:
txt, png or structure
'''


def tree_as_txt(decision_tree):
    with open('./decision_tree/tree_as_txt.txt', "w") as file:
        file.write(export_text(decision_tree))


def tree_to_png(decision_tree):
    plt.figure()
    plot_tree(decision_tree, feature_names=attributes, filled=True)
    plt.title("Decision tree")
    plt.show()


def tree_to_structure(decision_tree):
    joblib.dump(decision_tree, './decision_tree/tree_model')


def tree_from_structure(file):
    return joblib.load(file)

#drzewo = tree()
#tree_as_txt(drzewo)
#tree_to_png(drzewo)
#tree_to_structure(drzewo)
