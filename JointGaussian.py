#!/usr/bin/env python
# coding: utf-8

# In[10]:


import math
import random


# In[7]:


pdf=(1/pow((2*math.pi),3/2))*math.exp(-0.5*((x-1)^2+(y-1)^2+(z-1)^2))


# In[56]:


# sample pdf by integrating pdf to get CDF using Monte Carlo Integration
CDF=0
errorterm=0
n=10000
sample=[]
for i in range(2, n+2):
    x=random.random()
    y=random.random()
    z=random.random()
    
    pdf=(1/pow((2*math.pi),3/2))
    xxx=math.exp(-0.5*((pow((x-1),2)+(pow((y-1),2)+(pow((z-1),2))))))
    CDF=CDF+pdf
    errorterm=pow(pdf,2)+errorterm
    CDF=CDF/n
    error=pow(errorterm/n-pow(CDF,2),0.5)/pow(n,2)
    
    #print(error)
    if error<1/n:
        sample.append({x,y,z})
    
    else:
        n=n-1

    
    


# In[61]:


print(error)


# In[ ]:





# In[ ]:





# In[ ]:




