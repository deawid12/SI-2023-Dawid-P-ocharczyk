import numpy as np

# Funkcja aktywacji
def activation(x):
    return 1 if x >= 0 else 0

# Dane wejściowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_AND = np.array([0, 0, 0, 1])
y_NOT = np.array([1, 0, 1, 0])
y_XOR = np.array([0, 1, 1, 0])

# Inicjalizacja wag
w_AND = np.array([0.0, 0.0])
w_NOT = np.array([0.0, 0.0])
w_XOR = np.array([0.0, 0.0])

# Wsp uczenia
learning_rate = 0.1

# Trenowanie AND
for i in range(4):
    x = X[i]
    y = y_AND[i]
    y_pred = activation(np.dot(w_AND, x))
    y_AND_error = y - y_pred
    w_AND += learning_rate * y_AND_error * x.astype(float)

# Trenowanie NOT
for i in range(4):
    x = X[i]
    y = y_NOT[i]
    y_pred = activation(np.dot(w_NOT, x))
    y_NOT_error = y - y_pred
    w_NOT += learning_rate * y_NOT_error * x.astype(float)

# Trenowanie XOR
for i in range(4):
    x = X[i]
    y = y_XOR[i]
    y_pred = activation(np.dot(w_XOR, x))
    y_XOR_error = y - y_pred
    w_XOR += learning_rate * y_XOR_error * x.astype(float)

print("Percprtron AND")
for i in range(4):
    x = X[i]
    y_AND_pred = activation(np.dot(w_AND, x))
    print(f"AND({x[0]}, {x[1]}) = {y_AND_pred}")

print("\nPercprtron NOT")
for i in range(2):
    x = X[i]
    y_NOT_pred = activation(np.dot(w_NOT, x))
    print(f"NOT({x[0]}) = {y_NOT_pred}")

print("\nPercprtron AND-NOT")

for i in range(4):
    x = X[i]
    y_pred = activation(np.dot(w_AND, x) + np.dot(w_NOT, x))
    print(f"x1 AND NOT x2 ({x[0]}, {x[1]}) = {y_pred}")

print("\nPercprtron XOR")
for i in range(4):
    x = X[i]
    y_XOR_pred = activation(np.dot(w_XOR, x))
    print(f"XOR({x[0]}, {x[1]}) = {y_XOR_pred}")