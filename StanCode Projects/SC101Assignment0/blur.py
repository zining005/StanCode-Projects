"""
File: blur.py
Name: Zining Chen
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, original picture
    :return: Blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            total_red = 0
            total_green = 0
            total_blue = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 < pixel_x < img.width:
                        if 0 < pixel_y < img.height:
                            total_red += img.get_pixel(pixel_x, pixel_y).red
                            total_green += img.get_pixel(pixel_x, pixel_y).green
                            total_blue += img.get_pixel(pixel_x, pixel_y).blue
                            count += 1
            new_img.get_pixel(x, y).red = int(total_red/count)
            new_img.get_pixel(x, y).green = int(total_green/count)
            new_img.get_pixel(x, y).blue = int(total_blue/count)
    return new_img


def main():
    """
    Function: Blur the picture in 5 layers.
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
