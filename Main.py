import numpy as np
import pandas as pd

rho = 1.22
g = 9.81
Area = 2.3
Mass = 1000
trails = 6

# Enter your own Spreadsheet name
velocity = pd.read_csv("Untitled 1.csv") 
velocity_matrix = velocity.iloc[:,1:]
time_matrix = velocity.iloc[:,0]

#Finding average
velocity_avg = np.nanmean(velocity_matrix, axis=1)

#converting km/h to m/s
velocity_act = velocity_avg/3.6

time_diff = np.empty((np.size(time_matrix),))
for i in range(len(time_matrix)):
    if i == 0:
        time_diff[i] = 0
    else:
        time_diff[i] = time_matrix[i] - time_matrix[i-1]
        
   
def predict_velocity(vel_start, size, weights, t_diff):
    temp_ = np.empty((size*2,))
    velocity_ = np.empty((size,))
    for i in range(size*2):
        if i==0:
            temp_[0] = vel_start
        else:
            acc = -(Area*0.5*rho*weights[0]/Mass)*(temp_[i-1]**2) - weights[1]*g
            fin_vel = temp_[i-1] + acc*t_diff
            temp_[i] = fin_vel
    
    key=0
    for j in range(0,size*2,2):
        velocity_[key] = temp_[j]
        key = key + 1
    return(velocity_)

def gradient_descent(vel_cal, initial_weights, lrn_rate, conv_fac):
    converged = False
    weights = np.array(initial_weights)
    Epoch = 0
    while(not converged):
        grad_sum_squares = 0
        Epoch = Epoch + 1
        for i in range(len(weights)):
    
            v_pred = predict_velocity(vel_cal[0],np.size(vel_cal),weights,time_diff[1]/2)
        
            errors = v_pred - vel_cal
            if i ==0:
                temp = -(Area*0.5*rho/Mass)*(time_diff[1]/2)
                print(temp)
                print(v_pred)
                print(errors)
                derivative = np.dot(2*errors, temp*(v_pred**2))
                print(derivative)
            elif i == 1:
                derivative = np.sum(2*errors*(-g*time_diff[1]/2))
                print(derivative)
            weights[i] = weights[i] - (lrn_rate * derivative)
            grad_sum_squares = grad_sum_squares + derivative**2
           
        grad_mag = np.sqrt(grad_sum_squares)
        print("---------------------------------------------------------------")
        print("Epoch = " + str(Epoch))
        print("Weights = "+ str(weights))
        print("Error = " + str(grad_mag))
        if(grad_mag < conv_fac):
            converged = True
    return weights, grad_mag
