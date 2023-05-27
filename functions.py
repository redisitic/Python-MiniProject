# Importing the libraries.
import numpy as np
import matplotlib.pyplot as plt
import os
from spheres import Sphere, get_objects

objects = get_objects()
def normalise(vector):
    return vector / np.linalg.norm(vector)

# Calculates where the ray hits on the sphere


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
    distances = [sphere_intersect(obj.center, obj.radius, ray_origin, ray_direction) for obj in objects]
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

def path_finder(path):
    if os.name == "nt":
        return path.replace("/", "\\") #for windows
    else:
        return path.replace("\\", "/") #for linux