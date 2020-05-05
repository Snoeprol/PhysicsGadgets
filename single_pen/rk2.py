import numpy as np
import matplotlib.pyplot as plt

class ForceGenerators:
    @staticmethod
    def harmonic(x, k):
        return - k[0] * (x ** k[1])

    @staticmethod
    def weird(x, k):
        return np.sin(x)

    @staticmethod
    def pendulum(x,k):
        return - k[0] * np.sin(x)

class RK21D():

    def __init__(self,force_function, constants,steps,dt,initial_position, initial_velocity):
        self.steps = steps
        self.dt = dt
        self.constants = constants
        self.x = initial_position
        self.v = initial_velocity
        self.force_function = getattr(ForceGenerators, force_function)

    def generate(self):

        positions = []
        velocities = []
        for i in range(self.steps):
            # Update velocity
            k1 = self.dt * self.force_function(self.x, self.constants)
            k2 = self.dt * self.force_function(self.x + k1/2, self.constants)
            old_v = self.v
            self.v = self.v + k2

            # Calculate intermediate velocity
            k1 = self.dt/2 * self.force_function(self.x, self.constants)
            k2 = self.dt/2 * self.force_function(self.x + k1/2, self.constants)
            v_assist = old_v + self.dt/2 * k2

            k1 = self.dt * old_v
            k2 = self.dt * v_assist
            self.x = self.x + k2
            positions.append(self.x)
            velocities.append(self.v)

        return positions, velocities

runge = RK21D('pendulum',[100],10000,0.001,1, 0)
plt.plot(runge.generate()[0])
plt.show()
#plt.plot(runge.generate()[1])
#plt.show()