import numpy as np
import matplotlib.pyplot as plt


## Follows up on the course's week1 .md, day2 notes
## In lab 1 dataset

x_train = np.array([1.0, 2.0])
y_train = np.array([300, 500])

m = x_train.shape[0] ##Denotes de number of training examples. We could also use the y_train, since, in SL, each feature connects to a target

i = 1
x_i = x_train[i]
y_i = y_train[i]
ith_example = np.array([x_i, y_i])

##Plotting the data -------------------------------------------------------------

plt.scatter(x_train, y_train, marker='x', c='r') ## X axis, Y axis, shape of the dot, color of the dot
plt.title("Housing Prices")
plt.ylabel("Price")
plt.xlabel("SQF")
##plt.show()


## Linear Regression Predictio --------------------------------------------------

def compute_model_output(x, w, b):
    m = x.shape[0] ##counts the number of elements in the array 
    f_wb = np.zeros(m) ## creates a 1D array filled with 0's where our predictions will lay
    f_wb = w * x + b ## applies the model to our x_train array, when we pass it

    return f_wb

w = 200
b = 100
try_f_wb = compute_model_output(x_train, w, b)

plt.plot(x_train, try_f_wb, c='b', label="Our Prediction")
plt.scatter(x_train, y_train, c='r', label='Actual Values')
plt.title("Data vs Precition Model")
plt.xlabel("Square Feet")
plt.ylabel("Price in Dollars")
plt.legend() ## Adds a small box in the corner
##plt.show()

## We got it, the prediction perfectly models the real data

##Prediction of 1000 SQFT House

prediction = w * 1000 + b
print(f"${prediction:.0f} is the predicted price for a 1000 sqft house")