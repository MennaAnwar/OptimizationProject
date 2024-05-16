### Libraries ###

import cvxpy as cp
import numpy as np


### Parameters ###

# number of Transmitters (aka LEDs)
NL = 8

# a known matrix that is independent of p and depends on VLP system parameters 
# size = (3 * NL, 3)
# gamma = np.ones(size) # belongs to R(3NL*3)
gamma = np.random.rand(3 * NL, 3) # belongs to R(3NL*3)

# max tolerable CRLB level (will be specified later)
epsilon = 0.5  

# assumed electrical-to-optical power conversion efficiency
powConvEff = 0.3

# upper and lower bounds for electrical power (W)
elecPow_up = 5
elecPow_low = 1

# upper and lower bounds for optical power (W)
optPow_up = elecPow_up * powConvEff
optPow_low = elecPow_low * powConvEff


### Optimization Problem Variable ###

# transmitters' power
p = cp.Variable(NL, nonneg=True)


### Auxiliary Functions ###

# FIM == J(p) = (I3 (*k*) p)T * Gamma where (*k*) is Kronecker product
def FisherInformationMatrix(p):
    p_matrix = cp.reshape(p, (NL, 1))  # reshape p to a column matrix
    return ( cp.kron(p_matrix, np.eye(3)).T @ gamma )


# Define the objective function (minimize total power)
objective = cp.Minimize(cp.sum(p))

# Define the constraints
constraints = [
    cp.trace(cp.inv_pos(FisherInformationMatrix(p))) <= epsilon,
    p >= 0 
    # p <= optPow_up,
    # p >= optPow_low
]

# Form and solve the problem
problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.SCS)

# Print the results
if problem.status == 'optimal':
    print("Optimal power allocation:", p.value)
    print("Minimum total power:", problem.value)
else:
    print("yo, what the duck?!")