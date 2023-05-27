# Importing the libraries.
import numpy as np
import matplotlib.pyplot as plt
import os
import functions as f
from spheres import objects
from lights import lights

# Global variables.

max_depth = 4
width = 150
height = 100
exposure = 1
gamma = 2.2

# Defining camera and screen.

camera = np.array([0, 0, 1])
ratio = float(width/height)
screen = (-1, 1/ratio, 1, -1/ratio)  # Screen perfectly fits the camera.

# Main RayTracing loop.
image = np.zeros((height, width, 3))
for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
        pixel = np.array([x, y, 0])
        origin = camera
        direction = f.normalise(pixel - origin)
        color = np.zeros((3))
        reflection = 1
        for k in range(max_depth):
            nearest_object, min_distance = f.nearest_intersected_object(objects, origin, direction)
            if nearest_object is None:
                break
            intersection = origin + min_distance * direction
            normal_to_surface = f.normalise(intersection - nearest_object['center'])
            shifted_point = intersection + 1e-5 * normal_to_surface
            illumination = np.zeros((3))
            for light in lights:
                intersection_to_light = f.normalise(light['position'] - shifted_point)
                _, min_distance = f.nearest_intersected_object(objects, shifted_point, intersection_to_light)
                intersection_to_light_distance = np.linalg.norm(light['position'] - intersection)
                is_shadowed = min_distance < intersection_to_light_distance
                if is_shadowed:
                    continue
                illumination += nearest_object['diffuse'] * light['diffuse'] * (1 - 0.63661977236759*np.arccos(np.dot(intersection_to_light, normal_to_surface)))
                intersection_to_camera = f.normalise(camera - intersection)
                H = f.normalise(intersection_to_light + intersection_to_camera)
                illumination += nearest_object['specular'] * light['specular'] * np.dot(normal_to_surface, H) ** (nearest_object['shininess'] / 4)
            color += reflection * illumination
            reflection *= nearest_object['reflection'] * \
                nearest_object['diffuse']*illumination
            origin = shifted_point
            direction = f.reflected(direction, normal_to_surface)
        color = color * exposure + ((gamma*-1)+2.2)
        image[i, j] = np.clip(color, 0, 1)
    print(" %d / %d " % (i + 1, height))

# Path to the original render.
render = os.path.dirname(os.path.abspath(
    __file__)) + "/imgs/render.png"
# Making sure the path is correct for the OS.
render = f.path_finder(render)

plt.imsave(render, image)  # Saves the final render.