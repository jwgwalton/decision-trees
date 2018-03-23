from utils import is_numeric


class Question:
    """Question is the mechanism for partioning the dataset,
    Stores the feature that is used to partition the dataset, (the index of the column in the dataset)
    And the value of the feature"""

    def __init__(self, feature, value):
        self.feature = feature
        self.value = value

    def compare(self, example):
        feature_value = example[self.feature]
        if is_numeric(feature_value):
            return feature_value >= self.value
        else:
            return feature_value == self.value  # String comparison

    def __repr__(self):
        """To String for Question"""
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        # TODO: how to get the header value???
        # return f"{header[self.column]} {condition} {str(self.value)}"
        return f"{condition} {str(self.value)}"
