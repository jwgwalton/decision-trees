from tree import DecisionTree

training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

decison_tree = DecisionTree()

tree = decison_tree.build_tree(training_data)

decison_tree.print_tree(tree)


def pretty_print_leaf_predictions(counts):
    total = sum(counts.values()) * 1.0
    probabilities = {}
    for label in counts.keys():
        probabilities[label] = str(int(counts[label] / total * 100)) + "%"
    return probabilities


pretty_print_leaf_predictions(decison_tree.classify(training_data[0], tree))

testing_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 4, 'Apple'],
    ['Red', 2, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

for row in testing_data:
    print ("Actual: %s. Predicted: %s" %
           (row[-1], pretty_print_leaf_predictions(decison_tree.classify(row, tree))))