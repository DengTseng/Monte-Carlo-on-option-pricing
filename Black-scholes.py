import numpy as np 
import scipy.stats as st 

# parameters
S0 = 10.0 
K = 10.5 
r = 0.04 
sigma = 0.08 
T = 5.0 
q = 0 

t = 0 

# Calculate 
d1 = (np.log(S0/K)+(r-q+sigma**2/2)*(T-t))/(sigma*np.sqrt(T-t)) 
d2 = d1 - sigma*np.sqrt(T-t) 

V = S0*np.exp(-q*(T-t))*st.norm.cdf(d1) - K*np.exp(-r*(T-t))*st.norm.cdf(d2) 

print("The price of the option is {}".format(V))