import numpy as np 

# parameters
S0 = 10.0 
K = 10.5 
r = 0.04 
sigma = 0.08 
T = 5.0 
q = 0.0 

N = 10000
t = 0 

# produce random numbers 
V =np.maximum(0,S0*np.exp((r-q-sigma**2/2)*(T-t)+sigma*np.sqrt(T-t)*np.random.randn(N))-K)
V = (sum(V)/N)*np.exp(-r*(T-t))

print("The price of the option is {}".format(V))