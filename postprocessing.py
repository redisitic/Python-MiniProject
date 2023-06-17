import cv2


def main():
    image_path = input("Enter a path to the image\n>>> ")

    output_path = f"{image_path[:image_path.rfind('.')]}_post.{image_path[image_path.rfind('.'):]}"

    choice = input("Do you want a blur effect with higher resoultion or downsampling? [b/d]\n>>> ").lower()

    if choice not in ('b', 'd'):
        raise ValueError("invalid choice")

    image = cv2.imread(image_path)

    if choice == 'b':    # Applying a Gaussian blur to the image.
        image = cv2.GaussianBlur(image, (3, 3), 0)
    elif choice == 'd':  # Downsampling the image.
        image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

    cv2.imwrite(output_path, image)


if __name__ == '__main__':
    main()
