import numpy as np
import random

print("Alice, enter your bit string")
Alice_bits = input()

def Basis(bits):
    return ''.join(random.choice(['x', '+']) for _ in bits)

def Polarization(bits_string, basis_string):
    polarized_string = []
    for char1, char2 in zip(bits_string, basis_string):
        if char1 == '0' and char2 == '+':
            polarized_string.append('↑')  
        elif char1 == '1' and char2 == '+':
            polarized_string.append('→')  
        elif char1 == '0' and char2 == 'x':
            polarized_string.append('↗')  
        elif char1 == '1' and char2 == 'x':
            polarized_string.append('↖')
    return ''.join(polarized_string)

def Measurement(polarized_string, basis_string):
    measurement_string = []
    for char1, char2 in zip(polarized_string, basis_string):
        if char1 == '↑' and char2 == '+':
            measurement_string.append('↑')  
        elif char1 == '↑' and char2 == 'x':
            measurement_string.append(random.choice(["↖", "↗"]))  
        elif char1 == '↖' and char2 == '+':
            measurement_string.append(random.choice(["→", "↑"]))  
        elif char1 == '↖' and char2 == 'x':
            measurement_string.append('↖')

        elif char1 == '→' and char2 == '+':
            measurement_string.append('→')  
        elif char1 == '→' and char2 == 'x':
            measurement_string.append(random.choice(["↖", "↗"]))  
        elif char1 == '↗' and char2 == '+':
            measurement_string.append(random.choice(["→", "↑"]))  
        elif char1 == '↗' and char2 == 'x':
            measurement_string.append('↗')
    return ''.join(measurement_string)

Alice_basis = Basis(Alice_bits)
Alice_polarized_bits = Polarization(Alice_bits, Alice_basis)

Eve_basis = Basis(Alice_bits)
Eve_polarized_bits = Measurement(Alice_polarized_bits, Eve_basis)

Bob_basis = Basis(Alice_bits)

#Eveasdropping attempt
print("Eve, do you want to measure Alices bits using your state basis. (Y/N)?")
attack = input()

Bob_polarized_bits = Alice_polarized_bits
if attack in ['y', 'yes']:
    Bob_polarized_bits = Measurement(Eve_polarized_bits, Bob_basis)
elif attack in ['n', 'no']:
    Bob_polarized_bits = Measurement(Alice_polarized_bits, Bob_basis)   


#Checking for Eveasdropper
def check_eveasdropper(transmiting_basis, transmiting_bits, recieving_basis, recieving_bits):
    if not (len(transmiting_basis) == len(transmiting_bits) == len(recieving_basis) == len(recieving_bits)):
        raise ValueError("Input lists must be of the same length.")
    
    for i in range(len(transmiting_basis)):
        if transmiting_basis[i] == recieving_basis[i]:
            if transmiting_bits[i] != recieving_bits[i]:
                print("Eve attack")
                return "Eve attack"
    
    print("No attack")
    return "No attack"

print('Alice basis:          ', Alice_basis)
print("Alice Polarized bits: ", Alice_polarized_bits)
print("Eve_basis             ", Eve_basis)
print("Eve_polarized_bits:   ", Eve_polarized_bits)
print('Bob basis:            ', Bob_basis)
print("Bob_polarized_bits:   ", Bob_polarized_bits)