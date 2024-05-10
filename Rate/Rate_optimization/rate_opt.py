import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

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
iterations = 10
opt_rate = np.zeros(iterations)

# Iterate over the problem
for j in range(iterations):
    print(j)
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
    # update value of theta
    uj = u.value
    vj = v.value
    theta = np.sqrt(uj)/vj

    # add this rate to opt_rate
    opt_rate[j] = problem.value

# Algorithm output
print("u = ", u.value)
print("v = ", v.value)
print("w = ", w.value)
print("optimal rate = ", problem.value)

# Plot output
n = np.arange(1, iterations+1)
plt.plot(n, opt_rate)
plt.xlabel("Iteration number")
plt.ylabel("Optimal rate")
plt.show()
