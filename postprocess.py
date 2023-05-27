import cv2
import os
# Using OpenCV to anti-alias the render from raytracing.py.
# I should implement samples in the main loop instead.


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

# Path to the post processed render.
filename = os.path.dirname(os.path.abspath(
    __file__)) + "/imgs/render_post.png"
# Making sure the path is correct for the OS.
filename = path_finder(filename)

# Asking the user if they want to use a blur effect or downsampling.
n = input("Do you want a blur effect with higher resoultion or downsampling? (b / d)")

if n.lower() == 'b':
    image = cv2.imread(render)
    # Applying a Gaussian blur to the image.
    Gaussian = cv2.GaussianBlur(image, (3, 3), 0)
    cv2.imwrite(filename, Gaussian)
    
elif n.lower() == 'd':
    image = cv2.imread(render)
    # Downsampling the image.
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    cv2.imwrite(filename, image)
    
else:
    print("Invalid Choice. Using no Post process.")
