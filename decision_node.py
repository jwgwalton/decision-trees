class DecisionNode:
    """A Decision Node asks a question.

    This holds a reference to the question, and to the two child nodes
    resulting from a matching or non matching answer to the question.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch