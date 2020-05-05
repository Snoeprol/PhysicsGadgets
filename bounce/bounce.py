class Ball:

    def __init__(self, x, y, z, vx, vy, vz, m):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.m = m
    
class Engine():
    def __init__(self, dt):
        
        self.dt = dt
        self.time = 0

    def update_time(self):

        time = time + dt
