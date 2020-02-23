# Coupled_ODE-Coding

Monte Carlo Simulation

Consider the set of coupled ODEs:
𝑑𝑥 = 10(𝑦 − 𝑥) 𝑑𝑡
𝑑𝑦 = 𝑥(28 − 𝑧) − 𝑦 𝑑𝑡
𝑑𝑧 = 𝑥𝑦 − 8 𝑧 𝑑𝑡 3
𝑥(0) = 𝑦(0) = 𝑧(0) = 1
    
    Write an explicit RK-4 scheme to solve the above coupled system.
Now consider that the initial condition is not exactly known – it is only known that the initial value of (x,y,z) is a joint Gaussian with mean (1,1,1) and covariance of identity matrix. Sample 10,000 elements from this joint PDF and simulate the above coupled ODEs with each of those initial conditions.
