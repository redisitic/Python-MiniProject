import numpy as np

# Declaes the lights in the scene.
lights = [ 
            {'position': np.array([1, 3, 3]),'diffuse': np.array([1.5, 1.5, 1.5]), 'specular': np.array([1, 1, 1])}
]

class Light:
    def __init__(self, position, diffuse, specular):
        self.position = np.array(position)
        self.diffuse = np.array(diffuse)
        self.specular = np.array(specular)
        
light1 = Light([1, 3, 3], [1.5, 1.5, 1.5], [1, 1, 1])

def get_lights():
    return [light1]
    