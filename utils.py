def is_numeric(value):
    return  isinstance(value, int) or isinstance(value, float)


def class_counts(rows):
    """Counts for each labelled class in dataset"""
    counts = {}
    for row in rows:
        label = row[-1] # Label is final column in dictionary
        _add_label_if_missing(label, counts)
        counts[label] += 1
    return counts


def _add_label_if_missing(label, counts):
    if label not in counts:
        counts[label] = 0
