"""
Create the BB84 protocol with and without Eve

Additional statistical features: 

1. Counting of bits that dont match between Alice and Bob (QBER)
2. Create a variable the % of bits intercepted by Eve (Allow Random too)
4. Create a variable taht determines the % percentage of realistic errors

Role	| Task
Alice	| Sends randomly encoded qubits (bit + basis)
Bob	    | Randomly chooses measurement basis
Eve	    | Intercepts a % of qubits, measures and resends
You	    | Count mismatches between Alice and Bob when their bases match


"""

import numpy as np
from numpy import random

n = 10

#original string of information
bits = np.random.randint(0, 2, size= n)


#Alice basis (0 for orthogonal basis 1 for diagonal basis)
Alice_basis = np.random.randint(0, 2, size= n)

#Bob basis (0 for orthogonal basis 1 for diagonal basis)
Bob_basis = np.random.randint(0, 2, size= n)



# eve interception random percentage

evesdropping = []

for i in range(n):
    x = np.random.randint(2)
    if x == 1:
        print(x)
        evesdropping.append(i)

Eve_indexes = np.array(evesdropping)

print(bits)
print(Eve_indexes)

percentage_intercepted = len(Eve_indexes)/len(bits)

print(percentage_intercepted)








