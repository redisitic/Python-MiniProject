import numpy as np


class Light:
    def __init__(self, position, diffuse, specular, intensity):
        self.position = np.array(position)
        self.diffuse = np.array(diffuse) * intensity
        self.specular = np.array(specular)


class Sphere:
    def __init__(self, center, radius, diffuse, specular, shininess, reflection):
        self.center = np.array(center)
        self.radius: float = radius
        self.diffuse = np.array(diffuse)
        self.specular = np.array(specular)
        self.shininess: float = shininess
        self.reflection: float = reflection


class Camera:
    def __init__(self, position):
        self.position = np.array(position)


class Scene:
    def __init__(self, res: tuple[int, int], max_depth: int, hdr: bool, exposure: float, gamma: float, camera: Camera):
        self.res = res
        self.max_depth = max_depth
        self.hdr = hdr
        self.exposure = exposure
        self.gamma = gamma

        self._spheres: list[Sphere] = []
        self._lights: list[Light] = []
        self._camera = camera

    def add_sphere(self, sphere: Sphere):
        self._spheres.append(sphere)

    def add_light(self, light: Light):
        self._lights.append(light)

    def get_spheres(self) -> list[Sphere]:
        return self._spheres

    def get_lights(self) -> list[Light]:
        return self._lights

    def get_camera(self) -> Camera:
        return self._camera
