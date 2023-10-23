
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IPython import get_ipython

def string_to_function2D(expression):

            def function(x,y):

                return eval(expression)
            
            return function

def string_to_function3D(expression):

            def function(x,y,z):

                return eval(expression)
            
            return function

class DS:


    def __init__(self, x, y, z = None):
        # x, y and z are strings, the differential equtions describing the dynamics


        self.diff_eq = [x,y]

        if z != None:
            self.diff_eq.append(z)


    def plot(self, O, N):

        dt = 0.01
        
        if len(self.diff_eq) == 3:
              
            dx = string_to_function3D(self.diff_eq[0])
            dy = string_to_function3D(self.diff_eq[1])
            dz = string_to_function3D(self.diff_eq[2])

            # evolution functions
            def x_dot(x,y,z):
        
                return x + dt * dx(x,y,z)

            def y_dot(x,y,z):
        
                return y + dt * dy(x,y,z)

            
            def z_dot(x,y,z):
        
                return z + dt * dz(x,y,z)     
               
        else:

            dx = string_to_function2D(self.diff_eq[0])
            dy = string_to_function2D(self.diff_eq[1])

            def x_dot(x,y):
        
                return x + dt * dx(x,y)

            def y_dot(x,y,z):
        
                return y + dt * dy(x,y)   
        



        # initial condition
        x = [O[0]]
        y = [O[1]]

        if len(self.diff_eq) == 3:
            z = [O[2]]


        if len(self.diff_eq) == 3:

            for i in range(int(N)):
        
                x0 = x[-1]
                y0 = y[-1]
                z0 = z[-1]
                
                x.append(x_dot(x0, y0, z0))
                y.append(y_dot(x0, y0, z0))
                z.append(z_dot(x0, y0, z0))
        
            self.xline = np.array(x)
            self.yline = np.array(y)
            self.zline = np.array(z)
        
        else:

            for i in range(int(N)):
        
                x0 = x[-1]
                y0 = y[-1]
                
                
                x.append(x_dot(x0, y0))
                y.append(y_dot(x0, y0))

            self.xline = np.array(x)
            self.yline = np.array(y)

        # plot the (projected) flow


        plt.figure(dpi=1500)
        
        ax1 = plt.axes()
        ax1.plot(self.xline, self.yline, linewidth = 0.5)
        plt.axis('off')

        # xmax = abs(max(self.xline))+0.1
        # ymax = abs(max(self.yline))+0.1
        # xmin = abs(min(self.xline))-0.1
        # ymin = abs(min(self.yline))-0.1
        
        # plt.xlim(xmin, xmax)
        # plt.ylim(ymin, ymax)

            

    def plot3D(self, O, N):
         
        dt = 0.01
        
        if len(self.diff_eq) == 3:
              
            dx = string_to_function3D(self.diff_eq[0])
            dy = string_to_function3D(self.diff_eq[1])
            dz = string_to_function3D(self.diff_eq[2])

            # evolution functions
            def x_dot(x,y,z):
        
                return x + dt * dx(x,y,z)

            def y_dot(x,y,z):
        
                return y + dt * dy(x,y,z)

            
            def z_dot(x,y,z):
        
                return z + dt * dz(x,y,z)

        # initial condition
        x = [O[0]]
        y = [O[1]]
        z = [O[2]]

        
        if len(self.diff_eq) == 3:

            for i in range(int(N)):
        
                x0 = x[-1]
                y0 = y[-1]
                z0 = z[-1]
                
                x.append(x_dot(x0, y0, z0))
                y.append(y_dot(x0, y0, z0))
                z.append(z_dot(x0, y0, z0))
        
            self.xline = np.array(x)
            self.yline = np.array(y)
            self.zline = np.array(z)
        

        
        plt.figure(dpi=3500)

        get_ipython().run_line_magic('matplotlib', 'widget')
        ax = plt.axes(projection='3d') 
       
        ax.plot3D(self.xline, self.yline, self.zline, 'black', linewidth = 0.1)
        plt.axis("off")
        plt.ion()
        
        