import numpy as np
import mattoimage as mi

array = np.loadtxt("mstexample.csv",delimiter = ',')

print(array)

mi.mattoimage(array)

