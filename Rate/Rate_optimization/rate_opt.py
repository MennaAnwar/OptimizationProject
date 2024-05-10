import cvxpy as cp
import numpy as np

# Function used in constraint 2
def c2(M: cp.Variable, v) -> cp.Variable:
    M_res = M
    M_res = M_res - cp.diag(cp.diag(M_res)) + cp.diag(v)
    return cp.norm(M_res, axis=1)

# Problem constants
K = 3
L = 9
g = np.random.rand(L, K)
p = np.ones(L) * 10

sigma_max = 10**-3
sigma_n = np.random.rand(K)*sigma_max

# Initial guess for theta
theta = np.ones(K)

# Problem variables
w = cp.Variable((L, K))
u = cp.Variable(K)
v = cp.Variable(K)

# Problem statement
objective = cp.Maximize(cp.sum(0.5*cp.log(1+2*u/(np.pi*np.e))))

# g.T * w will be used a lot in the constraints so it is easier to define it here
M = g.T @ w


constraints = [
    cp.diag(M) >= u/(2*theta) + (0.5 * v**2 * theta),
    c2(M, sigma_n) <= v,
    cp.sum(w, axis=1) <= p
]

problem = cp.Problem(objective, constraints)

problem.solve()

print("u = ", u.value)
print("v = ", v.value)
print("w = ", w.value)