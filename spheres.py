import numpy as np
class Sphere:
    def __init__(self, center, radius, diffuse, specular, shininess, reflection):
        self.center = np.array(center)
        self.radius = float(radius)
        self.diffuse = np.array(diffuse)
        self.specular = np.array(specular)
        self.shininess = float(shininess)
        self.reflection = float(reflection)

def get_objects():
    sphere1 = Sphere([0, -0.5, -1], .5, [1, 1, 1], [0.5, 0.5, 0.5], 100, 0.75)
    sphere2 = Sphere([0, -9000, 0], 8999, [0.8, 0.8, 0.8], [1, 1, 1], 100, 1)
    sphere3 = Sphere([0, 9002, 0], 8999, [0.8, 0.8, 0.8], [1, 1, 1], 100, 1)
    sphere4 = Sphere([-9001,0,0], 8999, [0.8,0.05,0.05], [1,1,1], 100, 1)
    sphere5 = Sphere([9001,0,0], 8999, [0.05,0.05,0.8], [1,1,1], 100, 1)
    sphere6 = Sphere([0,0,-9002], 8999, [0.05,0.8,0.05], [1,1,1], 100, 1)
    return [sphere1, sphere2, sphere3, sphere4, sphere5, sphere6]