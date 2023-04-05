
import numpy as np
import matplotlib.pyplot as plt
n = 1.57
alpha = 60

def beta2(n, beta1):
    return np.degrees(np.arcsin((np.sin(np.radians(beta1)))/n))

def gamma2(n,beta1):
    return alpha - beta2(n,beta1)

def gamma1(n, beta1):
    gamma2_ = gamma2(n,beta1)
    return np.degrees(np.arcsin(n*np.sin(np.radians(gamma2_))))

def delta(n,beta1):
    return beta1 + gamma1(n,beta1) - alpha

#theta_ = np.linspace(33.3,90)
#plt.plot(theta_,delta(n,theta_),'go')
theta_ = np.linspace(33.3,90,300)
#plt.plot(theta_,delta(n,theta_),'b-')
#plt.xlabel("theta")
#plt.ylabel("delta")
#plt.show()

A1 = 1.522
A2 = 4590
nRed = A1 + A2/(680**2)
nOrange = A1 + A2/(600**2)
nYellow = A1 + A2/(580**2)
nGreen = A1 + A2/(540**2)
nBlue = A1 + A2/(470**2)
nPurple = A1 + A2/(405**2)

plt.plot(theta_,delta(nRed,theta_),color='red')
plt.plot(theta_,delta(nOrange,theta_),color='orange')
plt.plot(theta_,delta(nYellow,theta_),color='yellow')
plt.plot(theta_,delta(nGreen,theta_),color='green')
plt.plot(theta_,delta(nBlue,theta_),color='blue')
plt.plot(theta_,delta(nPurple,theta_),color='purple')
plt.xlabel="theta"
plt.ylabel="delta"
plt.show()

###################### plots
input = [90, 76, 70, 64, 58, 53, 47]
output = [75, 65, 58, 55, 54, 56, 63]

for i in range(len(input)):
    plt.plot(input[i],np.degrees(np.arctan(output[i]/46)),'o', color=(0,0,0))

plt.show()

plt.plot(theta_,delta(nRed,theta_),color='red')
plt.plot(theta_,delta(nOrange,theta_),color='orange')
plt.plot(theta_,delta(nYellow,theta_),color='yellow')
plt.plot(theta_,delta(nGreen,theta_),color='green')
plt.plot(theta_,delta(nBlue,theta_),color='blue')
plt.plot(theta_,delta(nPurple,theta_),color='purple')
plt.xlabel="theta"
plt.ylabel="delta"

for i in range(len(input)):
    plt.plot(input[i],np.degrees(np.arctan(output[i]/46)),'o', color=(0,0,0))

plt.show()