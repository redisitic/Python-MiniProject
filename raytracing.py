# Importing the libraries.
import numpy as np
import matplotlib.pyplot as plt
import os

# Global variables.

max_depth = 4
width = 800
height = 600
exposure = 1
gamma = 2.2

# Function to normalise a vector.


def normalise(vector):
    return vector / np.linalg.norm(vector)

# Calculates the sign disatance function of a sphere for ray intersection.


def sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None

# Goes through all the spheres in the scene to find the nearest one to the ray.


def nearest_intersected_object(objects, ray_origin, ray_direction):
    distances = [sphere_intersect(
        obj['center'], obj['radius'], ray_origin, ray_direction) for obj in objects]
    nearest_object = None
    min_distance = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distance
            nearest_object = objects[index]
    return nearest_object, min_distance

# Reflects the ray based on the normal of the sphere.


def reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis

# Defining camera and screen.


camera = np.array([0, 0, 1])
ratio = float(width/height)
screen = (-1, 1/ratio, 1, -1/ratio)  # Sccreen perfectly fits the camera.

# Declares Scene Objects.

objects = [
    {'center': np.array([-1, -0.5, -1]), 'radius': .5, 'ambient': np.array([0, 0, 0]), 'diffuse': np.array(
        [0.8, 0.7, 0.075]), 'specular': np.array([0.5, 0.5, 0.5]), 'shininess': 100, 'reflection': 0.75},
    {'center': np.array([1, -0.5, -1]), 'radius': .5, 'ambient': np.array([0, 0, 0]), 'diffuse': np.array(
        [0.075, 0.7, 0.8]), 'specular': np.array([0.5, 0.5, 0.5]), 'shininess': 100, 'reflection': 0.75},
    {'center': np.array([0, -9000, 0]), 'radius': 8999, 'ambient': np.array([0, 0, 0]), 'diffuse': np.array(
        [0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 5}
]
# Declaes the lights in the scene.
lights = [  # { 'position': np.array([10.125,16,5.5]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0.25, 0.25, 0.25]), 'specular': np.array([0.125, 0.125, 0.125]) },
            # { 'position': np.array([10.25,16,5.625]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0.25, 0.25, 0.25]), 'specular': np.array([0.125, 0.125, 0.125]) },
            # { 'position': np.array([10.375,16,5.75]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0.25, 0.25, 0.25]), 'specular': np.array([0.125, 0.125, 0.125]) },
            # { 'position': np.array([10.5,16,5.875]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0.25, 0.25, 0.25]), 'specular': np.array([0.125, 0.125, 0.125]) },
            {'position': np.array([10, 16, 6]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([2, 0, 0]), 'specular': np.array([1, 1, 1])},
            { 'position': np.array([-10,16,6]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0, 0, 2]), 'specular': np.array([0.125, 0.125, 0.125]) },
            # { 'position': np.array([9.75,16,6.25]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0.25, 0.25, 0.25]), 'specular': np.array([0.125, 0.125, 0.125]) },
            # { 'position': np.array([9.625,16,6.375]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0.25, 0.25, 0.25]), 'specular': np.array([0.125, 0.125, 0.125]) },
            # { 'position': np.array([9.5,16,6.5]), 'ambient': np.array([0.125, 0.125, 0.125]), 'diffuse': np.array([0.25, 0.25, 0.25]), 'specular': np.array([0.125, 0.125, 0.125]) }



]
# Main RayTracing loop.
image = np.zeros((height, width, 3))
for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
    for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
        pixel = np.array([x, y, 0])
        origin = camera
        direction = normalise(pixel - origin)
        color = np.zeros((3))
        reflection = 1
        for k in range(max_depth):
            nearest_object, min_distance = nearest_intersected_object(
                objects, origin, direction)
            if nearest_object is None:
                break
            intersection = origin + min_distance * direction
            normal_to_surface = normalise(
                intersection - nearest_object['center'])
            shifted_point = intersection + 1e-5 * normal_to_surface
            illumination = np.zeros((3))
            for light in lights:
                intersection_to_light = normalise(
                    light['position'] - shifted_point)
                _, min_distance = nearest_intersected_object(
                    objects, shifted_point, intersection_to_light)
                intersection_to_light_distance = np.linalg.norm(
                    light['position'] - intersection)
                is_shadowed = min_distance < intersection_to_light_distance
                if is_shadowed:
                    continue
                illumination += nearest_object['diffuse'] * light['diffuse'] * (
                    1 - 0.63661977236759*np.arccos(np.dot(intersection_to_light, normal_to_surface)))
                intersection_to_camera = normalise(camera - intersection)
                H = normalise(intersection_to_light + intersection_to_camera)
                illumination += nearest_object['specular'] * light['specular'] * np.dot(
                    normal_to_surface, H) ** (nearest_object['shininess'] / 4)
            color += reflection * illumination
            reflection *= nearest_object['reflection'] * \
                nearest_object['diffuse']*illumination
            origin = shifted_point
            direction = reflected(direction, normal_to_surface)
        color = color * exposure + ((gamma*-1)+2.2)
        image[i, j] = np.clip(color, 0, 1)
    print(" %d / %d " % (i + 1, height))


def path_finder(path):
    if os.name == "nt":
        return path.replace("/", "\\")
    else:
        return path.replace("\\", "/")


# Path to the original render.
render = os.path.dirname(os.path.abspath(
    __file__)) + "/imgs/render.png"
# Making sure the path is correct for the OS.
render = path_finder(render)

plt.imsave(render, image)  # Saves the final render.
