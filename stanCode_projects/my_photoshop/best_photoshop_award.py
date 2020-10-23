"""
File: best_photoshop_award.py
Author: Alan Chen
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
I will stand behind the mountain of the sunrise.
"""


from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THD = 1.3
# Controls the upper bound for black pixel as hair
HAIR = 120


def behind_mt(back, combined):
    """
    The author will stand behind the mountain.
    Because of backlighting, The front scene is black and the sky is blue.
    The front scene will cover the image again to make me look like standing behind mountain.
    :param back: SimpleImage, background, this is a sunrise landscape image on mountain A-li
    :param combined: SimpleImage, the combined images.
    :return: SimpleImage, author standing behind mountain.
    """

    for y in range(back.height):
        for x in range(back.width):
            pixel_me = combined.get_pixel(x, y)
            pixel_bg = back.get_pixel(x, y)
            if max(pixel_bg.green, pixel_bg.blue, pixel_bg.red) < 120:
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return combined


def combine(back, me):
    """
    This function combines the figure image of the author and a background image.
    :param back: SimpleImage, background, this is a sunrise landscape image on mountain A-li
    :param me: SimpleImage, me, author, Alan Chen, in front of a green screen wearing a mask.
    :return: The combined image.
    """
    for y in range(back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            pixel_bg = back.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green) // 3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THD and total > HAIR:
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop a person onto any background.
    It will display the two original image first.
    Afterward, the person will be put behind black background (such as mountain).
    """
    fg = SimpleImage('images/mask.jpg')
    bg = SimpleImage('images/alm.JPG')
    fg.show()
    bg.show()
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()
    behind_mt_img = behind_mt(bg, combined_img)
    behind_mt_img.show()


if __name__ == '__main__':
    main()
