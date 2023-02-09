import math
import matplotlib.pyplot as plt
import numpy as np


# Define the derivative function using the definition of derivative
def derivative(f, x, h):
    return (f(x + h) - f(x)) / h


# Define the cosine function
def cos_func(x):
    return math.cos(x)


# Part A: Calculate the slope of the cosine function at different points with different step sizes (h)
hs = [0.5, 0.3, 0.2, 0.1, 0.01, 0.001]

for h in hs:
    # Calculate the true error
    true_error = math.fabs(derivative(math.cos, math.pi / 4, h) + 1)

    # Calculate the relative true error
    relative_true_error = true_error / (math.fabs(math.sin(math.pi / 4)) + 1)

    # Calculate the approximate error
    approx_error = h * (math.fabs(math.cos(math.pi / 4 + h)) + 1)
    # Calculate the relative approximate error
    relative_approx_error = approx_error / (math.fabs(math.sin(math.pi / 4)) + 1)

    print("h:", h)
    print("True error:", true_error)
    print("Relative true error:", relative_true_error)
    print("Approximate error:", approx_error)
    print("Relative approximate error:", relative_approx_error)
    print("\n")

# Part B: Calculate the derivatives at different points
points = [0, math.pi / 8, math.pi / 6, math.pi / 4, math.pi / 2, math.pi]
derivatives = [derivative(math.cos, x, 0.001) for x in points]

# Part C: Plot the cosine function and its derivatives
x = np.arange(0, math.pi, 0.01)
y_cos = np.cos(x)
y_sin = -np.sin(x)

plt.plot(x, y_cos, label='cos(x)')
plt.plot(x, y_sin, label='-sin(x)')
plt.scatter([p for p in points], derivatives, label='Derivatives')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('cos(x) and its derivative')
plt.show()