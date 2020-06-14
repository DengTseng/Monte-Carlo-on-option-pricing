import numpy as np 
import scipy.stats as st 
import matplotlib.pyplot as plt 

# parameters
S0 = 10.0 
K = 10.5 
r = 0.04 
sigma = 0.08 
T = 5.0 
q = 0 

t = 0 

# Black Scholes
d1 = (np.log(S0/K)+(r-q+sigma**2/2)*(T-t))/(sigma*np.sqrt(T-t)) 
d2 = d1 - sigma*np.sqrt(T-t) 

V_BS = S0*np.exp(-q*(T-t))*st.norm.cdf(d1) - K*np.exp(-r*(T-t))*st.norm.cdf(d2) 

# Monte Carlo BS
N = [10,100,1000,10000,100000] 
error1 = np.zeros((5,1))
for i in range(5):
    V =np.maximum(0,S0*np.exp((r-q-sigma**2/2)*(T-t)+sigma*np.sqrt(T-t)*np.random.randn(N[i]))-K)
    V_MC = (sum(V)/N[i])*np.exp(-r*(T-t)) 
    #print(V_MC)
    error1[i] = np.abs(V_MC-V_BS) 

# Monte Carlo Bio-tree
dt = 0.1
q_d = 1/2-(r-q-sigma**2/2)*np.sqrt(dt)/(2*sigma) 
u = np.exp(sigma*np.sqrt(dt)) 
d = 1/u 
error2 = np.zeros((5,1))
for j in range(5):
    V_BT = 0
    for i in range(N[j]):
        prob = np.random.uniform(size=(int(T/dt),))
        S = S0
        for p in prob:
            if p <= q_d:
                S=S*d
            else:
                S = S*u
            #print(S)
        V_BT = V_BT+np.maximum(0,S-K)
    V_BT = (V_BT/N[j])*np.exp(-r*(T-t)) 
    error2[j] = np.abs(V_BT-V_BS) 

plt.figure()
plt.plot(error1,label = "MC on Black-Scholes") 
plt.plot(error2,label = "MC on Bio-Tree") 
plt.xticks(np.linspace(0,4,5),["10","100","1000","10000","100000"])
plt.legend()
plt.ylabel("error")
plt.xlabel("Times")
plt.show()