import json
import os

from matplotlib import pyplot as plt

from .scene import Scene, Light, Sphere, Camera
from . import engine


class Project:
    def __init__(self, name: str, desc: str,
                 res: tuple[int, int],
                 max_depth: int, hdr: bool, exposure: float, gamma: float,
                 lights: tuple[Light] | list[Light], spheres: tuple[Sphere] | list[Sphere],
                 camera: Camera):
        # assigning metadata
        self.name = name
        self.desc = desc

        # creating scene
        self._scene = Scene(res, max_depth, hdr, exposure, gamma, camera)
        for light in lights:
            self._scene.add_light(light)
        for sphere in spheres:
            self._scene.add_sphere(sphere)

    def render(self, export_path: str):
        os.makedirs(export_path[:export_path.rfind(os.path.sep)],
                    exist_ok=True)

        image = engine.render(self._scene)
        plt.imsave(export_path, image)

    @staticmethod
    def load(path: str):
        with open(path) as f:
            project = json.load(f)

        # constructing objects
        lights = [Light(light['position'], light['diffuse'], light['specular'], light['intensity'])
                  for light in project['objects']['lights']]

        spheres = [Sphere(sphere['center'], sphere['radius'], sphere['diffuse'], sphere['specular'], sphere['shininess'], sphere['reflection'])
                   for sphere in project['objects']['spheres']]

        camera = Camera(project['objects']['camera']['position'])

        return Project(
            project['meta']['name'], project['meta']['description'],
            (project['settings']['resolution']['width'], project['settings']['resolution']['height']),
            project['settings']['rendering']['max_depth'], project['settings']['rendering']['hdr'],
            project['settings']['rendering']['exposure'], project['settings']['rendering']['gamma'],
            lights, spheres, camera
        )
