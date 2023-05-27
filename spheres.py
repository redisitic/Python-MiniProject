import numpy as np

#defines the positions, colour and reflectivity of the spheres in the scene
objects = [
    {'center': np.array([0, -0.5, -1]), 'radius': .5, 'diffuse': np.array([1, 1, 1]), 'specular': np.array([0.5, 0.5, 0.5]), 'shininess': 100, 'reflection': 0.75},
    {'center': np.array([0, -9000, 0]), 'radius': 8999, 'diffuse': np.array([0.8, 0.8, 0.8]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 1},
    {'center': np.array([0, 9002, 0]), 'radius': 8999, 'diffuse': np.array([0.8, 0.8, 0.8]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 1},
    {'center': np.array([-9001,0,0]), 'radius': 8999, 'diffuse': np.array([0.8,0.05,0.05]), 'specular': np.array([1,1,1]), 'shininess': 100, 'reflection': 1},
    {'center': np.array([9001,0,0]), 'radius': 8999, 'diffuse': np.array([0.05,0.05,0.8]), 'specular': np.array([1,1,1]), 'shininess': 100, 'reflection': 1},
    {'center': np.array([0,0,-9002]), 'radius': 8999, 'diffuse': np.array([0.05,0.8,0.05]), 'specular': np.array([1,1,1]), 'shininess': 100, 'reflection': 1}
]

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