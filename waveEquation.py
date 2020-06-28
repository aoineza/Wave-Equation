import  numpy as np

def waveEquation(l,T,alpha,m,N,f,g):
    h = l/m
    k = T/N
    lamb = k*alpha/h
    W = np.zeros((N+1,m+1))
    T = np.zeros((N+1,m+1))
    X = np.zeros((N+1,m+1))
    for j in range(1,N+1):
        W[j][0] = 0
        W[j][m] = 0
    W[0][0] = f(0)
    W[m][0] = f(l)
    for i in range(1,m):
        W[0][i] = f(i*h)
        W[1][i] = (1-lamb**2)*f(i*h)+(lamb**2)/2*(f((i+1)*h)+f((i-1)*h))+k*g(i*h)
    for j in range(1,N):
        for i in range(1,m):
            W[j+1][i] = 2*(1-lamb**2)*W[j][i]+(lamb**2)*(W[j][i+1]+W[j][i-1])-W[j-1][i]
    for j in range(0,N+1):
        for i in range(0,m+1):
            X[j][i] = i*h
            T[j][i] = j*k
    return [W,T,X]

    
        
    
    
