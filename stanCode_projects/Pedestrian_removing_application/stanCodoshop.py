"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
-----------------------------------------------
This application will ask users to input more than three photos from the same background.
In brief, the algorithm calculates the color distance between each pixel and the mean RGB value
and display the best pixel over the images.
With its algorithm, this application can remove the passersby.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values
    """
    rdsq = (red - pixel.red)**2  # red squared
    gdsq = (green - pixel.green)**2  # green squared
    bdsq = (blue - pixel.blue)**2  # blue squared
    dist = (rdsq +gdsq + bdsq)**0.5  # sum and square root
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]
    """
    pixel_n = len(pixels)
    red = 0
    green = 0
    blue = 0
    rgb = [red, green, blue]
    for i in range(len(pixels)):
        pix = pixels[i]
        red += pix.red
        green += pix.green
        blue += pix.blue
    rgb[0] = int(red/pixel_n)
    rgb[1] = int(green/pixel_n)
    rgb[2] = int(blue/pixel_n)
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages
    """
    avg = get_average(pixels)
    red_avg = avg.pop(0)
    green_avg = avg.pop(0)
    blue_avg = avg.pop(0)
    best = pixels[0]
    best_dist = get_pixel_dist(pixels[0], red_avg, green_avg, blue_avg)
    for i in range(len(pixels)):
        pix = pixels[i]
        if get_pixel_dist(pix, red_avg, green_avg, blue_avg) < best_dist:
            best = pix
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed

    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for j in range(result.height):
        for i in range(result.width):
            result_pix = result.get_pixel(i, j)
            n = []
            for k in range(len(images)):
                n.append(images[k].get_pixel(i, j))
            best = get_best_pixel(n)
            result_pix.red = best.red
            result_pix.green = best.green
            result_pix.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
