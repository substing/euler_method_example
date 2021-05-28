#import libraries needed
import numpy as np
import matplotlib.pyplot as plt


h = 0.1 #step size
t = np.arange(0, h+1, h) #establish domain on which to analyze function
s0 = 1 #initial value


s = np.zeros(len(t)) #initially fill s array with zeros and make it size of t
s[0] = s0 #set initial condition

#Define mathematical function to be approximated
#In this instance, we are using an example from https://tutorial.math.lamar.edu/Classes/DE/UndeterminedCoefficients.aspx
#Of course, before writing the equation in code, we first isolated the value of y'
#Our equation was initially y' + 2y = 2 - e^(-4t) with y(0) = 1
#This becomes y' = 2 - e^(-4t) - 2y
def f(tp, sp): #tp and sp refering to this function calculating at a particular point, in contrast to general s and t used for iteration
	return 2 - np.exp(-4*tp) -2*sp

def exact_soln(t):
	return 1 + 0.5*np.exp(-4*t) - 0.5*np.exp(-2*t)

for i in range(0, len(t)-1): #iterate and calculate an entry of s for every step value of t
	s[i+1] = s[i] + h*f(t[i], s[i])

plt.plot(t, s, linestyle = 'dotted')# approximate solutuion
plt.plot(t, exact_soln(t))# "exact" solution

#things to make the graph pretty
for i in range(0, len(t)-1):
	plt.text(t[i], s[i], round(s[i], 4))



plt.title("Euler method approximation")
plt.grid()
plt.xlabel('t')
plt.ylabel('y')
plt.show()