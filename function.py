import numpy as np
import matplotlib.pyplot as plt

def P(x):
    return -2*x+100*x-800

z=range(1,8)
y=[-10*n**2+60*n+200 for n in z]
total=sum(y)

day=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

plt.pie(y,labels=day,autopct=lambda y:'{:.0f}'.format(y*total/100))
plt.show()