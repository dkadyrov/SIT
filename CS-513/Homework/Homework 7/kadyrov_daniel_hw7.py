# Course: CS 513B
# First Name: Daniel
# Last Name: Kadyrov
# ID: 10455680
# Purpose: Homework #7 RF

#%%
import pandas as pd

data = pd.read_csv("wisc_bc_ContinuousVar.csv", na_values="?")
data = data.dropna()

#%%

data["diagnosis norm"] = data["diagnosis"].factorize()[0] #data["Class"].apply(lambda x: )
x = data.iloc[:,2:-1]
y = data["diagnosis norm"]
# %%
input_dim = 2
ouput_dim = 2 
hidden_layers = 5
epsilon = 0.01 # learning rate for gradient descent
reg_lambda = 0.01 # regularization strength
passes = 20000
#%%
import numpy as np

num = len(x)
np.random.seed(0)

W1 = np.random.randn(input_dim, hidden_layers) / np.sqrt(input_dim)
b1 = np.zeros((1, hidden_layers))
W2 = np.random.randn(hidden_layers, ouput_dim) / np.sqrt(hidden_layers)
b2 = np.zeros((1, ouput_dim))

model = {}

for i in range(0, passes):
    z1 = x.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    delta3 = probs
    delta3[range(num), y] -= 1
    dW2 = (a1.T).dot(delta3)
    db2 = np.sum(delta3, axis=0, keepdims=True)
    delta2 = delta3.dot(W2.T) * (1-np.power(a1, 2))
    dW1 = np.dot(X.T, delta2)
    db1 = np.sum(delta2, axis=0)

    dW2 += reg_lambda * W2
    dW1 += reg_lambda * W1 

    W1 += -epsilon * dW1
    b1 += -epsilon * db1
    W2 += -epsilon * dW2
    b2 += -epsilon * db2

    model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}


# %%
