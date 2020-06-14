import numpy as np 

# parameters
S0 = 10.0 
K = 10.5 
r = 0.04 
sigma = 0.08 
T = 5.0 
q = 0.0 
dt = 0.1
q_d = 1/2-(r-q-sigma**2/2)*np.sqrt(dt)/(2*sigma) 
u = np.exp(sigma*np.sqrt(dt)) 
d = 1/u 

N = 10000
t = 0 

V = 0
for i in range(N):
    prob = np.random.uniform(size=(int(T/dt),))
    S = S0
    for p in prob:
        if p <= q_d:
            S=S*d
        else:
            S = S*u
        #print(S)
    V = V+np.maximum(0,S-K)

V = (V/N)*np.exp(-r*(T-t)) 

print("The price of the option is {}".format(V))