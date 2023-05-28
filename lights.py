import numpy as np
class Light:
    def __init__(self, position, diffuse, specular):
        self.position = np.array(position)
        self.diffuse = np.array(diffuse)
        self.specular = np.array(specular)
        
light1 = Light([1, 3, 3], [1.5, 1.5, 1.5], [1, 1, 1])

def get_lights():
    return [light1]
    