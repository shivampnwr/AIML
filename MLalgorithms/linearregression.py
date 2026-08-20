import numpy as np
import copy
import  matplotlib as plt

X_train = np.array([[100,3,4,2],[150,5,5,1],[200,8,2,2]])
Y_train = np.array([10000000,1500000,20000000])

b_init = 785.1811367994083
w_init = np.array([ 0.39133535, 18.75376741, -53.36032453, -26.42131618])


def compute_cost(X,y,w,b):
    m = X.shape[0]
    cost=0
    for i in range(m):
        f_wb = np.dot(X[i],w)+ b
        cost  += (f_wb - y[i])**2    
    cost =  cost/(2*m)
    return cost
cost = compute_cost(X_train,Y_train,w_init,b_init)
print(f"cost with the initial value,of w,b {cost}")


def compute_gradient(X,y,w,b):
    m,n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0
    for i in range(m):
        err = ((np.dot(X[i],w) + b ) - y[i])
        for j in range(n):
            dj_dw += err * X[i,j]
            dj_db += err
        dj_dw = dj_dw/m
        dj_db = dj_db/m
    return dj_dw, dj_db
dj_dw,dj_db = compute_gradient(X_train,Y_train,w_init,b_init)
print(f"gradient, w.r.t w with inital value of w: {dj_dw}")
print(f"gradient, w.r.t b with inital value of b: {dj_db}")

def gradient_descent(X,y,w_init,b_init,compute_gradient,num_iters,alpha):
    w = copy.deepcopy(w_init)  #avoid modifying global w within function
    b = b_init
    
    for i in range(num_iters):

        dj_db,dj_dw = compute_gradient(X, y, w, b)  

        # Update Parameters using w, b, alpha and gradient
        w = w - alpha * dj_dw               
        b = b - alpha * dj_db   

    return w, b
w = np.zeros_like(w_init)
b = 0
alpha = 0.002
num_iters = 10000
w_final,b_final = gradient_descent(X_train,Y_train,w,b,compute_gradient,num_iters,alpha)
print(w_final)
print("{b_final:0.2f}")




