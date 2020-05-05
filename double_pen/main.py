import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class DoublePendulum:
    """ Double pendulum using lagrangian differential equation solving it using euler or RK4"""
    def __init__(self, l1 = 1, l2 = 1, m1 = 1, m2 = 1, a1 = np.pi /2, a2 = np.pi /4 , g = 1, o1 = 0, o2 = 0, dt = 0.01, steps = 10000):
        
        self.l1 = l1
        self.l2 = l2
        self.a1 = a1
        self.a2 = a2
        self.m1 = m1
        self.m2 = m2
        self.g = g
        self.dt = dt
        self.o1 = o1
        self.o2 = o2
        self.steps = steps

    def _d_o2(self,dt):
        
        t1 = self._do2_assist(0)
        t2 = self._do2_assist(t1 * dt/2)
        t3 = self._do2_assist(t2 * dt/2)
        t4 = self._do2_assist(t3 * dt)
        
        return (dt / 6) * (t1 + 2 * t2 + 2 * t3 + t4)

    def _do2_assist(self, prop_o):
        
        o2 = self.o2 + prop_o

        t5 = 2 * np.sin(self.a1 - self.a2)
        t6 = self.o1 ** 2 * self.l1 * (self.m1 + self.m2)
        t7 = self.g * (self.m1 + self.m2) * np.cos(self.a1)
        t8 = o2 ** 2 * self.l2 * self.m2 * np.cos(self.a1 - self.a2)
        t9 = self.l2 * (2 * self.m1 + self.m2 - self.m2 * np.cos(2 * self.a1 - 2 * self.a2))

        return t5 * (t6 + t7 + t8)/ t9   

    def _d_o1(self,dt):
        
        t1 = self._do1_assist(0)
        t2 = self._do1_assist(t1 * dt/2)
        t3 = self._do1_assist(t2 * dt/2)
        t4 = self._do1_assist(t3 * dt)
    
        return (dt / 6) * (t1 + 2 * t2 + 2 * t3 + t4)

    def _do1_assist(self, prop_o):

        o1 = self.o1 + prop_o

        t1 = -self.g * (2 * self.m1 + self.m2) * np.sin(self.a1)
        t2 = -self.m2 * self.g * np.sin(self.a1 - 2 * self.a2)
        t3 = -2 * np.sin(self.a1 - self.a2) * self.m2 * (self.o2**2 * self.l2 + o1 **2 * self.l1 * np.cos(self.a1-self.a2))
        t4 = self.l1 * (2 * self.m1 + self.m2 - self.m2 * np.cos(2 * self.a1 - 2 * self.a2))

        return (t1 + t2 + t3)/ t4
    
    def _euler(self):
        do1 = self._do1_assist(0) * self.dt
        do2 = self._do2_assist(0) * self.dt
        self.o1 += do1
        self.o2 += do2
        self.a1 += self.o1 * self.dt
        self.a2 += self.o2 * self.dt
        return (self.a1, self.a2)

    def _runge_kutta(self):
        o1_cur = self.o1
        o2_cur = self.o2
        do1_half = self._d_o1(self.dt/2)
        do2_half = self._d_o2(self.dt/2)
        o1_ass = o1_cur + do1_half
        o2_ass = o2_cur + do2_half
        do1 = self._d_o1(self.dt)
        do2 = self._d_o2(self.dt)
        self.o1 += do1
        self.o2 += do2
        self.a1 += self.dt/6 * (o1_cur + 4 * o1_ass + self.o1)
        self.a2 += self.dt/6 * (o2_cur + 4 * o2_ass + self.o2)
        return (self.a1, self.a2)
    
    def _generate_angles(self):
        a1 = [] 
        a2 = []
        for i in range(self.steps):
            angles = self._runge_kutta()
            a1.append(angles[0])
            a2.append(angles[1])
        return (a1, a2)
    
    def generate_positions(self):
        (angle_1, angle_2) = self._generate_angles()
        x_1s = []
        y_1s = []
        x_2s = []
        y_2s = []

        for i in range(self.steps):
            x_1 = self.l1 * np.sin(angle_1[i])
            y_1 = - self.l1 * np.cos(angle_1[i])

            x_2 = x_1 + self.l2 * np.sin(angle_2[i])
            y_2 = y_1 - self.l2 * np.cos(angle_2[i])
            
            x_1s.append(x_1)
            y_1s.append(y_1)
            x_2s.append(x_2)
            y_2s.append(y_2)
        return (x_1s, y_1s, x_2s, y_2s)

    def plot_angles(self):
        (angle_1, angle_2) = self._generate_angles()
        plt.plot(angle_1)
        plt.plot(angle_2)
        plt.show()

    def plot_angles_2(self):
        (angle_1, angle_2) = self._generate_angles()
        plt.plot(angle_1,angle_2)
        plt.show()

class Animator:
    
    def __init__(self, pendulum):
        self.pendulum = pendulum
        self.animate()

    def animate(self):

        self.positions = self.pendulum.generate_positions()
        self.x1 = self.positions[0]
        self.y1 = self.positions[1]
        self.x2 = self.positions[2]
        self.y2 = self.positions[3]

        fig = plt.figure()
        if self.pendulum.generate_positions():
            ax_size = self.pendulum.l1 + self.pendulum.l2
        else:
            ax_size = self.pendulum.l
        ax = fig.add_subplot(111, autoscale_on=False, xlim=(-ax_size, ax_size), ylim=(-ax_size, ax_size))
        ax.set_aspect('equal')
        ax.get_frame_on()

        ax.set_facecolor('black')
        ax.grid()
        self.line, = ax.plot([], [], 'o-', lw=2)
        self.time_template = 'time = %.1fs'
        self.time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

        
        ani = animation.FuncAnimation(fig, self.frame, range(1, len(self.x1)),
                                    interval=self.pendulum.dt/10, blit=True, init_func=self.init)
        #Writer = animation.writers['ffmpeg']
        #writer = Writer(fps=4, metadata=dict(artist='Me'), bitrate=100)
        #ani.save('Pend.mp4', writer = writer)
        plt.show()

    def init(self):
        self.line.set_data([], [])
        self.time_text.set_text('')
        return self.line, self.time_text


    def frame(self,i):
        thisx = [0, self.x1[i], self.x2[i]]
        thisy = [0, self.y1[i], self.y2[i]]

        self.line.set_data(thisx, thisy)
        #self.time_text.set_text(self.time_template % (i*self.pendulum.dt))
        return self.line, self.time_text

if __name__ == "__main__":
    double_pendulum = DoublePendulum(1,100,1,1,np.pi/2- 0.1,np.pi/3,1,0,0,0.1,10000)
    double_pendulum.plot_angles_2()
    animator = Animator(double_pendulum)