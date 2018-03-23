from utils import class_counts


class Leaf:
    """ Terminal node of a decision tree.
    contains a dictionary of the number of times each label reaches this leaf,
    if perfectly split will just have one label """

    def __init__(self, rows):
        self.predictions = class_counts(rows)
