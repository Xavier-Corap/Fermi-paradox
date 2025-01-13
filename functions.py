import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches


Rp=10 ##en année
fp=0.5
ne=2
fl=1
fi=0.01
fc=0.01
Rg=15 ##en kpc
h=1 ##en kpc
annee=31536000 ##seconde par an
c=300000*annee/3.09e16 ##vitesse de la lumière en kilo parsec par année
Rastro=Rp*fp*ne
fbiot=fl*fi*fc
N=10
##coordonnées du soleil 
soleil=[0,8.5,0]
Rastro=1

Vg=np.pi*Rg**2*h


def N(L,Rastro=Rastro,fbiot=fbiot):
    return Rastro*fbiot*L

def D1(L,Rastro=Rastro,fbiot=fbiot,h=h,Rg=Rg):
    return 2*(3*h*Rg**2/(4*Rastro*fbiot*L))**(1/3)

def D2(L,Rastro=Rastro,fbiot=fbiot,h=h,Rg=Rg):
    return 2*Rg/np.sqrt(Rastro*fbiot*L)





def arm(r,k,r0,theta0):
    return -1*r*np.sin(k*np.log(r/r0)+theta0),r*np.cos(k*np.log(r/r0)+theta0)


def te(r,k,r0,theta0):
    return k*np.log(r/r0)+theta0


def erand(k,r0,theta0,n):
    t0=[]
    R0=[]
    t1=[]
    R1=[]
    t2=[]
    R2=[]
    t3=[]
    R3=[]
    for i in range(0,n):
        b=int(np.random.uniform(0,4))
        r=np.random.exponential(3)
        theta=te(r,k[b],r0[b],theta0[b])
        theta=theta+np.random.uniform(0,2*np.pi)*np.exp(-r*0.35)
        r=r+np.random.normal(0,0.07*r)
        t0.append(theta)
        R0.append(r)
            
    return R0,R1,R2,R3,t0,t1,t2,t3
        
def xy(r,t):
    x=[]
    y=[]
    for i in range (0,len(t)):
        x.append(r[i]*np.cos(t[i]))
        y.append(r[i]*np.sin(t[i]))
    return x,y
        
def zal(z):
    for i in range (0,len(z)):
        z[i]=np.random.choice([-1,1])*z[i]
    return z


def Vmoy1(L,v=0.001*c,Vg=Vg):
    return 1/3*np.pi*v**3*L**3

def Vmoy2(L,v=0.001*c,Vg=Vg,h=h):
    return 1/3*np.pi*v**2*L**2/h

def contact(L,N,p,pm,Vmoy,v=0.001*c,Vg=Vg):
    L2=[]
    N2=[]
    for i in range(0,len(N)):
        for j in range(0,len(L)):
            p0=Vmoy(L[j])/Vg*N[i]
            if p0>=p and p0<=pm:
                L2.append(L[j])
                N2.append(N[i])
    return L2,N2