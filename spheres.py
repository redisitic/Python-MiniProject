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