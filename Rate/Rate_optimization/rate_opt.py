import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

# Function used in constraint 2
def c2(M: cp.Variable, v) -> cp.Variable:
    M_res = M
    M_res = (M_res - cp.diag(cp.diag(M_res)))/np.sqrt(3) + cp.diag(v)
    return cp.norm(M_res, axis=1)

# Function to calculate a weighted moving average
def calculate_ema(values, alpha):
    ema = values[0]  # start with the first value

    for value in values[1:]:
        ema = alpha * value + (1 - alpha) * ema
    
    return ema


# Problem constants
K = 3 # Number of users
L = 9 # Number of lamps
g = np.loadtxt("my_grindset") # Describe the channel
p = np.array([7.74903481e-07, 1.44155904e+01, 6.11280099e+00, 3.00493992e+00, 1.81572075e-06, 6.07339084e+00, 1.07330140e-06, 1.63758571e+01, 5.73877204e+00])

# sigma_max = 10**-7
sigma_n = np.ones(K)*10**-11

# Initial guess for theta
theta = np.ones(K)
iterations = 500
opt_rate = []

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
        opt_rate.append(problem.value)
    except:
        break
# End of loop

# Algorithm output
print("final optimal rate = ", opt_rate[-1])
# Plot output
n = np.arange(1, len(opt_rate)+1)
if len(n) > 20:
    np.savetxt("my_grindset", g)


plt.plot(n,opt_rate)
plt.xlabel("Iteration number")
plt.ylabel("Optimal rate")
plt.show()

# Take EMA and graph it with alpha
ema_values = []
alpha_values = np.arange(0, 1.1, 0.1)

for alpha in alpha_values:
    ema_values.append(calculate_ema(opt_rate, alpha))

plt.plot(alpha_values, ema_values)
plt.xlabel("Alpha")
plt.ylabel("EMA Rate")
plt.show()

