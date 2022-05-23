import numpy as np

def randomArray(year, month, day):
    return np.random.rand(year - 1900, abs(month - day))

print(randomArray(1995, 6, 23))

