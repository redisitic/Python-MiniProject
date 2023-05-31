import cv2
import os
from functions import path_finder

render = os.path.dirname(os.path.abspath(__file__)) + "/imgs/render.png"
render = path_finder(render)
filename = os.path.dirname(os.path.abspath(
    __file__)) + "/imgs/render_post.png"
filename = path_finder(filename)

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
    #