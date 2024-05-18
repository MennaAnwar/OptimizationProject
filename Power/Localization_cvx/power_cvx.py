### Libraries ###

import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt


### Parameters ###

# number of Transmitters (aka LEDs)
NL = 4

# a known matrix that is independent of p and depends on VLP system parameters 
gamma = np.loadtxt("gamma_sys")

# max tolerable CRLB level (from 0.05 to 0.75)
epsilon = np.arange(0.05, 0.76, 0.05)

# array to store min power values at different CRLB levels
iterations = len(epsilon)
minPowArray = np.empty(iterations)

# empty array to store allocated LED power values at CRLB = 0.25
allocatedPow_CRLB = np.empty(NL)

# upper and lower bounds for electrical power (W)
elecPow_up = 6
elecPow_low = 0.5

# max electric power for all transmitters combined
totalElecPow = 24

# assumed electrical-to-optical power conversion efficiency
powConvEff = 1


### Optimization Problem Variable ###

# transmitters' power
p = cp.Variable(NL, nonneg=True)


### Auxiliary Functions ###

# FIM == J(p) = (I3 (*k*) p)T * Gamma where (*k*) is Kronecker product
def FisherInformationMatrix(p):
    p_matrix = cp.reshape(p, (NL, 1))  # reshape p to a column matrix
    return ( cp.kron(np.eye(3), p_matrix).T @ gamma )


### Optimization Problem and Solution ###

# objective function is to minimize total power (1.T @ P)
objective = cp.Minimize(cp.sum(p))

# loop to calculate min power for different values of CRLB
for i in range(iterations):
    # constraints 
    constraints = [
        cp.trace(cp.inv_pos(FisherInformationMatrix(p))) <= epsilon[i],
        p >= 0,
        cp.sum(p) <= totalElecPow,
        p <= elecPow_up,
        p >= elecPow_low
    ]

    # Form and solve the problem
    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS) # selected SCS as the solver

    # store min power value at this CRLB
    minPowArray[i] = problem.value

    # store allocated power values at epsilon (CRLB) = 0.25
    if epsilon[i] == 0.25:
        allocatedPow_CRLB = p.value

# printing results
if problem.status == 'optimal':
    # print allocated electrical power @CRLB = 0.25
    print("Optimal Electrical Power Allocation:", allocatedPow_CRLB)

    # save power values in a text file to be used for rate optimization
    np.savetxt("kono_pawa_elec_w", allocatedPow_CRLB)

    # save power values in a text file to be used for rate optimization
    np.savetxt("kono_pawa_opt_w", allocatedPow_CRLB * powConvEff)

    # save power values in a text file to be used for rate optimization
    np.savetxt("kono_pawa_opt_dbm", 10 * np.log10(allocatedPow_CRLB * powConvEff * 1000))

    # plotting Min Power vs CRLB
    plt.plot(epsilon,minPowArray)
    plt.xlabel("Max CRLB")
    plt.ylabel("Min Power")
    plt.show()
else:
    print("yo, what the duck?!")
