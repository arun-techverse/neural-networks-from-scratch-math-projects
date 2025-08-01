import numpy as np
#activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(sig_x):
    return sig_x * (1 - sig_x)

#Input/Output
x = np.array([[0.5, 0.8]])  
y_true = np.array([[1]]) 

#initianlize
np.random.seed(0)
W1 = np.random.randn(2, 2) 
b1 = np.random.randn(1, 2)
W2 = np.random.randn(2, 1) 
b2 = np.random.randn(1, 1)

#forward
z1 = np.dot(x, W1) + b1
a1 = sigmoid(z1)

z2 = np.dot(a1, W2) + b2
a2 = sigmoid(z2)
loss = 0.5 * (y_true - a2)**2 

print("==== FORWARD PASS ====")
print("z1 (input → hidden):", z1)
print("a1 (activation):", a1)
print("z2 (hidden → output):", z2)
print("a2 (final prediction):", a2)
print("Loss:", loss)

#output
dL_da2 = -(y_true - a2)
da2_dz2 = sigmoid_derivative(a2)
dz2_dW2 = a1

dL_dz2 = dL_da2 * da2_dz2
dL_dW2 = np.dot(dz2_dW2.T, dL_dz2) 
dL_db2 = dL_dz2 

#hidden
dz2_da1 = W2
dL_da1 = np.dot(dL_dz2, dz2_da1.T)
da1_dz1 = sigmoid_derivative(a1)
dz1_dW1 = x

dL_dz1 = dL_da1 * da1_dz1
dL_dW1 = np.dot(dz1_dW1.T, dL_dz1)  # shape (2,2)
dL_db1 = dL_dz1

print("\n==== BACKWARD PASS ====")
print("Gradient dL/dW2:", dL_dW2)
print("Gradient dL/db2:", dL_db2)
print("Gradient dL/dW1:", dL_dW1)
print("Gradient dL/db1:", dL_db1)