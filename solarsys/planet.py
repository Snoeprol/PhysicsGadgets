import numpy as np
import matplotlib.pyplot as plt
class Planet:
    def __init__(self, x, y, z, vx ,vy, vz,mass):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.mass = mass
    
def update_position(planet):

    norm = np.sqrt(np.dot([planet.x,planet.y,planet.z],[planet.x,planet.y,planet.z]))
    force = generate_force(norm)
    normalized = np.divide([planet.x,planet.y,planet.z],norm)

    x_comp = np.dot([1,0,0],normalized)
    y_comp = np.dot([0,1,0],normalized)
    z_comp = np.dot([0,0,1],normalized)
    planet.vx = planet.vx + dt * force * x_comp
    planet.vy = planet.vy + dt * force * y_comp
    planet.vz = planet.vz + dt * force * z_comp
    planet.x = planet.x + dt * planet.vx
    planet.y = planet.y + dt * planet.vy
    planet.z = planet.z + dt * planet.vz
    
positions = []

def generate_force(r):
    force = 1/np.dot(r,r)
    return - 10 * force

mars = Planet(1,1.5,1.5,0.3,2,0,3)
earth = Planet(1,1,1,0.2,0,1,4)
dt = 0.001
x_earth = []
y_earth = []
mars_pos = [[],[],[]]
steps = 5000
for i in range(steps):
    update_position(earth)
    update_position(mars)
    x_earth.append(earth.x)
    y_earth.append(earth.y)
    mars_pos[0].append(mars.x)
    mars_pos[1].append(mars.y)
    mars_pos[2].append(mars.z)
#plt.plot(x_earth,y_earth)
#plt.plot(mars_pos[0],mars_pos[1])
#plt.plot([0],[0], 'ro')
#plt.show()

from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

def animate(pos):
    
        # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # 40 Scatters with random starting parameters
    data = [np.array(pos)]

    ax.plot([0],[0],[0], markerfacecolor = 'y', marker = 'o', markersize = 6,label = 'Sun') 
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

    # Setting the axes properties
    ax.set_xlim3d([-4, 4])
    ax.set_xlabel('X [fortnite inches]')

    ax.set_ylim3d([-4, 4])
    ax.set_ylabel('Y [fortnite inches]')

    ax.set_zlim3d([-4, 4])
    ax.set_zlabel('Z [fortnite inches]')

    ax.set_title('3D Scatterboys')
    
    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, 25, fargs=(data, lines),
                                    interval=0.01, blit=False)
    plt.legend()
    plt.show()

def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

animate(mars_pos)