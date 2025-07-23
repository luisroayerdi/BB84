"""
BB84 protocol with Eveasdropping

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

# ========== PARAMETERS ==========
N_QUBITS = 10  # total qubits sent by Alice
INTERCEPT_RATE = 0.7  # percentage of qubits Eve intercepts (0 to 1)

# ========== FUNCTION DEFINITIONS ==========


def generate_bits(n):
    '''Generate a random bit string of 0s and 1s'''
    return np.random.randint(0, 2, size= n)

def generate_bases(n):
    """Generate a random basis: 0 (Z/rectilinear), 1 (X/diagonal)"""
    return np.random.randint(0, 2, size= n)

def choose_eve_intercepts(n, intercept_rate):
    """Randomly choose which qubits Eve intercepts based on a percentage"""
    n_intercepts = int(intercept_rate * n)
    return np.sort(np.random.choice(n, size=n_intercepts, replace=False))

def measure_qubits(bit_string, sender_basis, reciever_basis, range_intercepted):
    """Logic to measure qubits and deal with different basis"""
    reciever_bits = bit_string.copy()
    for i in range_intercepted:
        if sender_basis[i] == reciever_basis[i]:
            reciever_bits[i] = bit_string[i]
        else:
            reciever_bits[i] = np.random.randint(0,2)
    return reciever_bits

def basis_reconciliation(alice_basis, bob_basis, bits, bob_bits):
    accurate_bits = 0
    compared_bits = 0
    for i in range(len(bits)):
        if alice_basis[i] == bob_basis[i]:
            compared_bits += 1
            if bits[i] == bob_bits[i]:
                accurate_bits += 1
    return accurate_bits, compared_bits

def calculate_qber(compared_bits, accurate_bits):
    '''Calculation of the quantum bit error rate'''
    if compared_bits == 0:
        return 0
    return 1 - (accurate_bits / compared_bits)
        
def print_bb84_state(bits, alice_basis, eve_indexes, eve_basis, eve_bits, bob_basis, bob_bits, accurate_bits, qber):
    print("Original Bits  :", bits)
    print("Alice's Bases  :", alice_basis)
    print("")
    print("Eve's Bases    :", eve_basis)
    print("Eve's Bits     :", eve_bits)
    print("")
    print("Bob's Bases    :", bob_basis)
    print("Bob's Bits     :", bob_bits)
    print("")
    print("Eve Intercepts :", eve_indexes)
    print("Intercepted %  :", len(eve_indexes) / len(bits))
    print("")
    print("Accurate bits  :", accurate_bits)
    print("QBER           :", qber)


# ========== SIMULATION ==========
def simulate_bb84(n_qubits, intercept_rate, verbose=True):
    bits = generate_bits(n_qubits)
    alice_basis = generate_bases(n_qubits)
    eve_indexes = choose_eve_intercepts(n_qubits, intercept_rate)
    
    # Eve's measure and resend qubits
    eve_basis = generate_bases(n_qubits)
    eve_bits = measure_qubits(bits, alice_basis, eve_basis, eve_indexes)

    # Bob's measure and resend qubits
    bob_basis = generate_bases(n_qubits)
    bob_bits = measure_qubits(eve_bits, eve_basis, bob_basis, bits)

    #Basis reconciliation result
    accurate_bits, compared_bits = basis_reconciliation(alice_basis, bob_basis, bits, bob_bits)
    qber = calculate_qber(compared_bits, accurate_bits)

    # Print initial setup
    if verbose:
        print_bb84_state(bits, alice_basis, eve_indexes, eve_basis, eve_bits, bob_basis, bob_bits, accurate_bits, qber)

    
    return bits, alice_basis, bob_basis, eve_basis, eve_indexes

# ========== RUN ==========
if __name__ == "__main__":
    simulate_bb84(N_QUBITS, INTERCEPT_RATE)











