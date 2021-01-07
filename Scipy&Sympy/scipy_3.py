#numerik analiz yöntemiyle kök bulma
import numpy as np
from scipy.optimize import root

def f(x):
    return x ** 5 - x ** 3 - x ** 2

result = root(f, [-10, 10])

print(result)
