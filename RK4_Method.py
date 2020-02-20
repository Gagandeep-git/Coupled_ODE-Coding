#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


def odeValx(x, y, z): 
    return 10*(y-x)


# In[3]:


def odeValy(x, y,z): 
    return (x*(28-z)-y)


# In[4]:


def odeValz(x, y,z): 
    return (x*y-(8/3)*z)


# In[5]:


# using initial values of x,y,z find values at given time t using RK 4 method
# h is the step size
# t0 is the initial time - taken as zero
def myRungeKutta4Method(x0, y0, z0, t, t0, h, equations): 
    # Count number of iterations in the RK 4 method  
    n = (math.ceil)((t - t0)/h)  
    
    # Initialise x,y, and z
    x=x0;
    y=y0;
    z=z0;
    
    # Iterate for number of iterations
    for i in range(1, n + 1): 
        
        k1x=h*odeValx(x,y,z)
        k1y=h*odeValy(x,y,z)
        k1z=h*odeValz(x,y,z)
            
        k2x =h * odeValx(x+ 0.5*k1x, y + 0.5*k1y, z+0.5*k1z) 
        k2y =h * odeValy(x+ 0.5*k1x, y + 0.5*k1y, z+0.5*k1z)   
        k2z =h * odeValz(x+ 0.5*k1x, y + 0.5*k1y, z+0.5*k1z)    
            
        k3x =h * odeValx(x+ 0.5*k2x, y + 0.5*k2y, z+0.5*k2z) 
        k3y =h * odeValy(x+ 0.5*k2x, y + 0.5*k2y, z+0.5*k2z)
        k3z =h * odeValz(x+ 0.5*k2x, y + 0.5*k2y, z+0.5*k2z)
        
        k4x =h * odeValx(x+ k3x, y + k3y, z+k3z) 
        k4y =h * odeValy(x+ k3x, y + k3y, z+k3z)
        k4z =h * odeValz(x+ k3x, y + k3y, z+k3z)
        
        
        kx=(1.0 / 6.0)*(k1x + 2 * k2x + 2 * k3x + k4x)
        ky=(1.0 / 6.0)*(k1y + 2 * k2y + 2 * k3y + k4y)
        kz=(1.0 / 6.0)*(k1z + 2 * k2z + 2 * k3z + k4z)
        
        x = x + kx  
        y = y + ky
        
        #if func==ode2Val(x,y,z) or func==ode3Val(x,y,z):
        z = z + kz
                
        t0=t0+h
        
        
        print('x:')
        print(x)
        print('y:')
        print(y)
        print('z:')
        print(z)
        
        
        #k11 = h * ode1Val(x, y) 
        #kx1 = h * (lambda x,y: 10*(y-x))(x,y)
        
        #k12 = h * ode1Val(x+ 0.5 * k11, y + 0.5 * k11) 
        #k13 = h * ode1Val(x+ 0.5 * k12, y + 0.5 * k12) 
        #k14 = h * ode1Val(x+ k13, y + k13) 
  
  
    return x,y,z 


# In[7]:


# RK 4
# assume step size 0.1
x0 = 1
y0 = 1
z0 = 1
h = 0.01    # Seems like an ill conditioned system as the coefficients of variables are huge, therefore choose small h
t = 10
t0=0
equations=3         # number of odes
#print("at time=")
#print(t)
print(': the value of x,y,z is:', myRungeKutta4Method(x0, y0, z0, t, t0, h, equations))


# In[ ]:




