import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

# Function used in constraint 2
def c2(M: cp.Variable, v) -> cp.Variable:
    M_res = M
    M_res = (M_res - cp.diag(cp.diag(M_res))) + cp.diag(v)
    return cp.norm(M_res, axis=1)

# Problem constants
K = 3 # Number of users
L = 9 # Number of lamps
g = np.random.rayleigh(1, (L, K)) # Describe the channel
p = np.ones(L) * 10 # Max power for each lamp

sigma_max = 10**-10
sigma_n = np.random.rand(K)*sigma_max

# Initial guess for theta
theta = np.ones(K)
iterations = 500
opt_rate = np.zeros(iterations) - 1

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
        cp.diag(M) >= u/(2*theta) + (0.5 * cp.multiply(v**2, theta)),
        c2(M, sigma_n) <= v,
        cp.sum(w, axis=1) <= p
    ]

    problem = cp.Problem(objective, constraints)
    try:
        problem.solve(solver=cp.SCS) #SCS
        # update value of theta
        uj = u.value
        vj = v.value
        theta = np.sqrt(uj)/vj

        # add this rate to opt_rate
        opt_rate[j] = problem.value
    except:
        break
# End of loop

# Algorithm output
print("u = ", u.value)
print("v = ", v.value)
print("w = ", w.value)
print("optimal rate = ", problem.value)

# Plot output
res = opt_rate[opt_rate != -1]
n = np.arange(1, len(res)+1)
plt.plot(n,res)
plt.xlabel("Iteration number")
plt.ylabel("Optimal rate")
plt.show()
