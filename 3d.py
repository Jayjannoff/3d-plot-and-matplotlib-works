#!/usr/bin/env python
# coding: utf-8

# In[41]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[42]:


fig,ax = plt.subplots()
x=np.linspace(0,3*np.pi,1000)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x,y,lw=3,label='sine')
plt.plot(x,y1,lw=3,label='cosine')
ax.grid(True)
ax.legend(frameon=False)
ax.axis('equal')
ax.set_xlim(0,3*np.pi)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi/2))
ax.yaxis.set_major_locator(plt.MultipleLocator(np.pi/4))
plt.show()


# In[43]:


from mpl_toolkits import mplot3d
fig = plt.figure()
ax = plt.axes(projection='3d')
plt.show()


# In[44]:


ax = plt.axes(projection='3d')
zline = np.linspace(0,15,1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline,yline,zline,color='gray')


zdata = 15*np.random.random(100)
xdata = np.sin(zdata)+0.1*np.random.randn(100)
ydata = np.cos(zdata)+0.1*np.random.randn(100)
ax.scatter3D(xdata,ydata,zdata,c=zdata,cmap='Greens')
plt.show()


# In[45]:


ax = plt.axes(projection='3d')
zline = np.linspace(0,20,10000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline,yline,zline,color='gray')

zdata = 20*np.random.random(150)
xdata = np.sin(zdata)+0.1*np.random.randn(150)
ydata = np.cos(zdata)+0.1*np.random.randn(150)
ax.scatter3D(xdata,ydata,zdata,c=zdata,cmap='Reds')
plt.show()


# In[46]:


#So as to use the upcoming cell you are demanded to install (sklearn) and also oliwiette mat file i will share with you.


# In[47]:


fig , axi = plt.subplots(5,5,figsize=(6,6))
fig.subplots_adjust(wspace=0,hspace=0)
#you can find installetion guide from pypi.com and you can search as sklearn the web will show you how to install
from sklearn.datasets import fetch_olivetti_faces
data = fetch_olivietti_faces().images

for i in range(5):
    for j in range(5):
        ax[i,j].xaxis.set_major_locator(plt.NullLocator)
        ax[i,j].yaxis.set_major_locator(plt.NullLocator)
        ax.imshow(data[10*i+j],cmap='bone')
plt.show


# In[48]:


rng = np.random.RandomState(0)
x = np.linspace(0,10,500)
y = np.cumsum(rng.randn(500,6),0)
plt.plot(x,y)
plt.legend('ABCDEF',ncol=2,loc='upper left')
plt.show()


# In[51]:


import seaborn as sns
sns.set()
plt.plot(x,y)
plt.legend('ABCDEF',ncol=2,loc='upper left')


# In[55]:


iris = sns.load_dataset('iris')
iris.head()


# In[57]:


sns.pairplot(iris,hue='species',height=2.5)


# In[ ]:




