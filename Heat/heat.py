import numpy as np
from mayavi import mlab
x , y , z = np . ogrid [-10:10:20j , -10:10:20j , -10:10:20j]
scalar = np . sin ( x * y * z ) / ( x* y * z )
mlab.contour3d(scalar)
mlab.show()