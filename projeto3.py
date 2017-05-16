from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

g=9.8 #m/s**2
m=0.3 #kg
#consideramos que durante toda a queda, temperatura=10°C ou 283K
p=1.25 #kg*m**-3 #p é a densidade do ar
Cd=0.1 #coeficiente de arrasto; 0.1 antes da aberturaa e  depois da abertura
A= #area do corpo em visão perpendicular ao seu movimento
#estes dois ultimos irão se alterar no momento em que o paraquedas for aberto

def paraquedas(y,t):
	X=y[0]
	Vx=y[1]
	Y=[2]
	Vy=[3]
	dxdt=Vx
	dvxdt=(1/2)*(p*Cd*A*((Vx**2)+(Vy**2))/m)*(Vx/((Vx**2)+(Vy**2))**(1/2))
	dydt=Vy
	dvydt=(1/2)*(p*Cd*A*((Vx**2)+(Vy**2))/m)*(Vy/((Vx**2)+(Vy**2))**(1/2))-g
	return (dxdt,dvxdt,dydt,dvydt)


y0=[0,11000,250,0]
t=np.linspace(0,200, num=2000)
solx=odeint(paraquedas,y0,t)
plt.plot(sol[:,0],sol[:,2])
plt.title("Trajetório do saltador")
plt.xlabel("Distância do salto [metros]")
plt.ylabel("Altura [metros]")
plt.show()


