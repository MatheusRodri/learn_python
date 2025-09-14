height = [1.87, 1.82, 1.91, 1.78, 1.85]
print(height)

weight = [81.65, 83.50, 79.20, 75.10, 80.50]
print(weight)

print("")
# weight / height ** 2 # This line will raise an error

import numpy as np
np_height = np.array(height)
print(np_height)
np_weight = np.array(weight)
print(np_weight)

bmi = np_weight / np_height ** 2
print(bmi)
print(bmi[1])
print(bmi > 23)
print(bmi[bmi > 23])

print("")
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)
print(python_list + python_list)
print(numpy_array + numpy_array)