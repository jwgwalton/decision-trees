from question import Question
from utils import class_counts


def gini_impurity(rows):
    counts = class_counts(rows)
    impurity = 1
    for label in counts:
        prob_of_label = counts[label] / float(len(rows))
        impurity -= prob_of_label**2
    return impurity


def information_gain(left_child, right_child, current_uncertainty):
    weight = float(len(left_child)/ len(left_child) + len(right_child))
    return current_uncertainty - weight * gini_impurity(left_child) - (1 - weight) * gini_impurity(right_child)


def partition(rows, question):
    """ partition a dataset into matching and non matching rows based off question"""
    true_rows, false_rows = [], []
    for row in rows:
        if question.compare(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def find_optimal_split(rows):
    """Iterate over features and values to find optimal question to partition the data"""
    best_gain = 0
    best_question = None
    current_uncertainty = gini_impurity(rows)
    n_features = len(rows[0]) - 1 # number of columns - the label column

    for column in range(n_features):
        unique_values = _unique_values_in_column(rows, column)

        # iterate through possible questions to find best split
        for value in unique_values:
            question = Question(column, value)

            true_rows, false_rows = partition(rows, question)

            if _data_not_split(true_rows, false_rows):
                continue # Question doesn't divide so move onto next possible

            gain = information_gain(true_rows, false_rows, current_uncertainty)

            if gain > best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


def _data_not_split(true_rows, false_rows):
    return len(true_rows) == 0 or len(false_rows) == 0


def _unique_values_in_column(rows, column):
    return set([row[column] for row in rows])





