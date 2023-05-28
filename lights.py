import numpy as np
class Light:
    def __init__(self, position, diffuse, specular, intensity):
        self.position = np.array(position)
        self.diffuse = np.array(diffuse)*intensity
        self.specular = np.array(specular)
        
def get_lights():
    light1 = Light([1, 3, 0], [1, 1, 1], [1, 1, 1], 10)
    return [light1]
    