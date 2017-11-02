import numpy as np 
import matplotlib.pyplot as plt
import math 
import sys 
from pylab import figure

h = .01
t_final = 10000
#new comment to test git

if(len(sys.argv) != 1):
  #if there are command line arguments, then check to see if one of them is help
  for i in range (len(sys.argv)):
      if(sys.argv[i] == "help"): 
  
        print("Command Line arguments are: ")
        print("1 - Compare numerical and analytic") #plot numeric vs. analytic
        print("2 - Error vs. time for the explicit method" ) 
        #plot the error on the explicit euler method
        print("3 - Explicit Euler: x, v vs. t ")   
        print("4 - Implicit Euler: x, v vs. t" )
        print("5 - Explicit Euler in phase space")      
        print("6 - Implicit Euler in phase space")      
        print("7 - Symplectic Euler in phase space")      
        print("8 - Symplectic, Implicit, and Explicit Euler methods in phase space")      
        print("9 - Error Convergence Plot")      
        print("10 - Error on Explicit Euler method vs. Time") 
        exit()
        #exit program after printing help 



def explicit_euler(x_0, v_0, h_1, t_f): 
  x = [x_0]
  v = [v_0]
  t = [0]
  for i in range (0, t_f): 
    x.append(x[i] + h_1*v[i])
    v.append(v[i] - h_1*x[i])
    t.append(t[i] + h_1)
  return x, v, t 
  #explicit euler formula 
  
  
def e_error(x, v, t_f, h_1):
  v_error = []
  x_error = []
  for i in range(0, t_f ):
    t = i*h_1
    x_error.append(abs(np.cos(t)- x[i]))
    v_error.append(abs(-np.sin(t) - v[i])) 
  return x_error, v_error
  #find the error between analytic solution and the numerical method
  
  
def compute_energy(x, v):
  if (len(x) != len(v)):
    print ('x and v are not the same length')
    return 0
  E = []
  for i in range (len(x)):
    E.append(x[i]**(2) + v[i]**(2))
  return E
  #compute energy for each time step


def implicit_euler(x_0, v_0, h_1): 
  x = [x_0]
  v = [v_0]
  t = [0]
  for i in range (0, t_final):
    v.append(1.0/float((h_1)**2 + 1)*float(v[i] - h_1*x[i]))
    x.append(x[i] + h_1*v[i])
    t.append(t[i] + h_1)
  return x, v, t
  
def symp_euler(x_0, v_0, h_1):
  x = [x_0]
  v = [v_0]
  t = [0] 
  for i in (range (0, t_final)): 
    x.append(x[i] + h_1*v[i])
    v.append(v[i] - h_1*x[i+1])
    t.append(t[i] + h_1)
  return x, v, t
  
 

x_ex, v_ex, t_ex = explicit_euler(1, 0, h, t_final)
x_im, v_im, t_im = implicit_euler(1, 0, h)
x_sym, v_sym, t_sym = symp_euler(1,0,h)



E_ex = compute_energy(x_ex, v_ex)
E_sym = compute_energy(x_sym, v_sym)
E_im = compute_energy(x_im, v_im)

k= [h/2.0, h/3.0 ,h/4.0, h/16.0, h/20.0, h/32.0, h/64.0, h/100.0]
data = []

time = 10
for i in range(len(k)):
  # run for a fixed time, not a fixed number of time steps. 
  t_steps = int(time/(k[i]))
  x_3, v_3, t_3 = explicit_euler(1, 0, k[i], t_steps)
  x_error2, v_error2 = e_error(x_3, v_3, (t_steps +1 ), k[i])
  data.append(max(x_error2))



x_errorEx, v_errorEx = e_error(x_ex, v_ex, (t_final + 1), h)
x_errorIm, v_errorIm = e_error(x_im, v_im, (t_final + 1), h)


if (len(sys.argv) == 1):
  exit()
  #quit before printing images if there are no command line arguments

for i in range (1, len(sys.argv)): 
  
  if( int(sys.argv[i]) == 1):
    plt.plot(x_ex)
    plt.plot(np.cos(t_ex))
    plt.savefig("x_compare.png")
    
    #plot numeric vs. analytic

  if ( int(sys.argv[i]) == 2): 
    plt.plot(t_ex, x_errorEx) 
    plt.savefig("error_explicit.png")
    #plot the error on the explicit euler method
    
  if ( int(sys.argv[i]) == 3): 
    plt.plot(t_ex, x_ex)
    plt.plot(t_ex, v_ex)
    plt.savefig("xv_ex.png")
    #plot the time and velocity for the explicit plot

  if (int(sys.argv[i]) == 4):
    plt.plot(t_im, x_im)
    plt.plot(t_im, v_im)
    plt.savefig("xv_im.png")
    #plot the time vs. velocity for the implicit plot
  
  if (int(sys.argv[i]) == 5):
    plt.plot(x_ex, v_ex)
    plt.savefig("phase_ex.png") 
    #plot the explicit Euler in phase space
    
  if (int(sys.argv[i]) == 6):
    plt.plot(x_im, v_im)
    plt.savefig("phase_im.png") 
    #plot the implicit Euler in phase space
   
  if (int(sys.argv[i]) == 7):
    plt.plot(x_sym, v_sym)
    plt.savefig("phase_sym.png")
    #plot symplectic Euler in phase space
  
  if (int(sys.argv[i]) == 8):
    plt.plot(x_sym, v_sym)
    plt.plot(x_im, v_im)
    plt.plot(x_ex, v_ex)
    plt.savefig("phase_all.png")
    #plot symplectic, explicit, and implicit in phase space
    
  if(int(sys.argv[i]) == 9):
    plt.loglog(k, data)
    plt.savefig("error_convergence.png")
    
  if(int(sys.argv[i]) == 10):
    plt.loglog(k, data)
    plt.savefig("error_ex.png")

#some functions to plot things










