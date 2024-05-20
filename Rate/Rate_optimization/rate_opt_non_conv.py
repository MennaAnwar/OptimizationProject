import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

# Function used in objective function denominator
def obj_den(M: cp.Variable, v) -> cp.Variable:
    M_res = M
    M_res = (M_res - cp.diag(cp.diag(M_res)))/np.sqrt(3) + cp.diag(v)
    return cp.norm(M_res, axis=1)


# Problem constants
K = 3 # Number of users
L = 4 # Number of lamps
G = np.loadtxt("G") # Describe the channel
p = np.loadtxt("../../Power/Localization_cvx/kono_pawa_opt_w")

# sigma_max = 10**-7
sigma_n = np.ones(K)*10**-11

# Problem variables
w = cp.Variable((L, K))

# g.T * w will be used a lot in the constraints so it is easier to define it here
M = G.T @ w

# Problem statement
objective = cp.Maximize(cp.sum(0.5*cp.log(1+2* cp.abs(cp.diag(M))**2 / (obj_den(M, sigma_n) *np.pi*np.e))))



constraints = [
    cp.sum(w, axis=1) <= p
]

problem = cp.Problem(objective, constraints)
problem.solve(solver=cp.ECOS) #SCS
print("Optimal value for w is")
print(w.value)
print("Optimal rate is")
print(problem.value)

