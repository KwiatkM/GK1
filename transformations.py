import numpy as np
from math import tan

def perspectiveProjectionMatrix(w,h,fov,n,f):
    # w = width of the camera (screen)
    # h = height of the camera (screen)
    # fov = field of view (in radians)
    # n = distance to near plane
    # f = distance to far plane
    return np.array([[(1/((w/h) * tan(fov/2))), 0, 0, 0],
                     [0, (1/tan(fov/2)), 0, 0],
                     [0, 0, f/(f-n), ((-f) * n)/(f-n)],
                     [0, 0, 1, 0]])