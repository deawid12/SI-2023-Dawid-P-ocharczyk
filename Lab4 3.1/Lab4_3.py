import numpy as np

def entropy(labels):
    unique_labels, counts = np.unique(labels, return_counts=True)
    probabilities = counts / len(labels)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

def information_gain(data, labels, attribute):
    attribute_values = np.unique(data[:, attribute])
    total_entropy = entropy(labels)
    weighted_entropy = 0
    for value in attribute_values:
        value_indices = np.where(data[:, attribute] == value)[0]
        subset_labels = labels[value_indices]
        subset_entropy = entropy(subset_labels)
        subset_weight = len(value_indices) / len(data)
        weighted_entropy += subset_weight * subset_entropy
    information_gain = total_entropy - weighted_entropy
    return information_gain

def decision_tree_learning(data, labels, attributes):
    if len(np.unique(labels)) == 1:
        # All examples have the same label
        return labels[0]
    if len(attributes) == 0:
        # No more attributes to split on
        label_counts = np.bincount(labels)
        most_common_label = np.argmax(label_counts)
        return most_common_label
    best_attribute = None
    best_information_gain = -1
    for attribute in attributes:
        gain = information_gain(data, labels, attribute)
        if gain > best_information_gain:
            best_attribute = attribute
            best_information_gain = gain
    tree = {best_attribute: {}}
    attribute_values = np.unique(data[:, best_attribute])
    for value in attribute_values:
        value_indices = np.where(data[:, best_attribute] == value)[0]
        subset_data = data[value_indices]
        subset_labels = labels[value_indices]
        subset_attributes = attributes.copy()
        subset_attributes.remove(best_attribute)
        tree[best_attribute][value] = decision_tree_learning(subset_data, subset_labels, subset_attributes)
    return tree

# Dane
OB = np.array([
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 1]
])

labels = np.array([0, 0, 0, 1, 1])

attributes = [0, 1, 2]

decision_tree = decision_tree_learning(OB, labels, attributes)

print(decision_tree)
