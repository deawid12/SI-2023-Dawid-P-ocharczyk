import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class NeuralNetwork:
    def __init__(self):
        # Inicjalizacja wag
        self.wg1 = np.array([[-0.5], [0.3]])
        self.wg2 = np.array([[0.7]])

        # Inicjalizacja biasów
        self.bs1 = np.array([[-0.1]])
        self.bs2 = np.array([[0.5]])

    def forward(self, x):
        # Propagacja w przód
        self.lay1 = sigmoid(np.dot(x, self.wg1) + self.bs1)
        self.wy = sigmoid(np.dot(self.lay1, self.wg2) + self.bs2)
        return self.wy

    def backward(self, x, y, wy):
        # Propagacja wsteczna
        error = y - wy
        wyjsc = error * wy * (1 - wy)

        BD = wyjsc * self.wg2.T
        hi = BD * self.lay1 * (1 - self.lay1)

        # Aktualizacja wag i biasów
        self.wg2 += self.lay1.T.dot(wyjsc) * 0.1
        self.bs2 += np.sum(wyjsc, axis=0, keepdims=True) * 0.1
        self.wg1 += x.T.dot(hi) * 0.1
        self.bs1 += np.sum(hi, axis=0, keepdims=True) * 0.1

network = NeuralNetwork()
x = np.array([[0.6, 0.1]]) # Pierwszy przykład treningowy
y = np.array([[1]]) # Oczekiwany wynik

wy = network.forward(x)
print("Przed treningiem:")
print(wy)

network.backward(x, y, wy)
print("Po treningu:")
print(network.forward(x))
