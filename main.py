import cv2 as cv
import numpy as np


def start():
    readImg()


def readImg():

    image = cv.imread('doggo.png')

    status = image.shape

    if len(status) == 3:
        modPx(image)

    else:
        print("Grayscale is not allowed.")


def modPx(image):
    print('\nEnter X and Y values.')
    x = int(input("X Value: "))
    y = int(input("Y Value: "))
    z = int(input("[0] Blue \n[1] Red \n[2] Green \nPlease Choose Color Attributes: "))

    if z >=3:
        print("Invalid Color Scale! Plese choose again...")
        modPx(image)

    else:

        cv.imshow("BEFORE", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

        px = image.item(x, y, z)
        print("Image Value: ", x, y, z)
        print("Pixel Value: ", px)

        image.itemset((x, y, z), 70)
        px = image.item(x, y, z)
        print("Modified Pixel Value: ", px)

    
   
        dimension(image)


def dimension(image):

    size = image.shape

    x = 640
    y = 640

    if size[0] > x and size[1] > y:
        print("Oops! Sorry! Invalid image dimension.")

    else:
        imageType(image)


def imageType(image):
    dtype = image.dtype
    print("The image data type is", dtype)

    imageSize(image)


def imageSize(image):

    requiredSize = 1228800
    size = image.size

    if size <= requiredSize:
        print("Image size is Validated.")
        cv.imshow("AFTER", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("Image size is Invalid.")


start()
