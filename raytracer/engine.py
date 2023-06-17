import numpy as np

from .scene import Scene, Sphere


def _normalise(vector):
    return vector / np.linalg.norm(vector)


def _sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None


def _nearest_intersected_object(objects, ray_origin, ray_direction):
    distances = [_sphere_intersect(obj.center, obj.radius, ray_origin, ray_direction) for obj in objects]
    nearest_object = None
    min_distance = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distance
            nearest_object = objects[index]
    return nearest_object, min_distance


def _reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis


def render(scene: Scene, quite: bool = False):
    ratio = scene.res[0] / scene.res[1]
    screen = (-1, 1/ratio, 1, -1/ratio)

    image = np.zeros((scene.res[1], scene.res[0], 3))
    for i, y in enumerate(np.linspace(screen[1], screen[3], scene.res[1])):
        for j, x in enumerate(np.linspace(screen[0], screen[2], scene.res[0])):
            pixel = np.array([x, y, 0])
            origin = scene.get_camera().position
            direction = _normalise(pixel - origin)
            color = np.zeros(3)
            reflection = 1
            for k in range(scene.max_depth):
                nearest_object: Sphere
                nearest_object, min_distance = _nearest_intersected_object(scene.get_spheres(), origin, direction)
                if nearest_object is None:
                    break
                intersection = origin + min_distance * direction
                normal_to_surface = _normalise(intersection - nearest_object.center)
                shifted_point = intersection + 1e-5 * normal_to_surface
                illumination = np.zeros(3)
                shadowed_illumination = np.zeros(3)
                for light in scene.get_lights():
                    intersection_to_light = _normalise(light.position - shifted_point)
                    _, min_distance = _nearest_intersected_object(scene.get_spheres(), shifted_point, intersection_to_light)
                    intersection_to_light_distance = np.linalg.norm(light.position - intersection)
                    is_shadowed = min_distance < intersection_to_light_distance
                    if is_shadowed:
                        reflection *= 0.25 * (nearest_object.diffuse * nearest_object.reflection) * (light.diffuse * (1 - 0.63661977236759*np.arccos(np.dot(intersection_to_light, normal_to_surface))) / intersection_to_light_distance ** 2)
                        shadowed_illumination += reflection
                    illumination += nearest_object.diffuse * light.diffuse * (1 - 0.63661977236759*np.arccos(np.dot(intersection_to_light, normal_to_surface))) / intersection_to_light_distance ** 2
                    intersection_to_camera = _normalise(scene.get_camera().position - intersection)
                    illumination += nearest_object.specular * light.specular * np.dot(normal_to_surface, _normalise(intersection_to_light + intersection_to_camera)) ** (nearest_object.shininess / 4)
                color += (reflection * illumination) + shadowed_illumination
                reflection *= nearest_object.reflection * nearest_object.diffuse * illumination
                origin = shifted_point
                direction = _reflected(direction, normal_to_surface)

            color = color * scene.exposure - scene.gamma + 2.2
            if scene.hdr:
                color = color**0.6
            image[i, j] = np.clip(color, 0, 1)

        if not quite:
            print(f"{i+1} / {scene.res[1]}, {(i+1)/scene.res[1]:.2%}", end="\r")

    if not quite:
        print("\n")

    return image
