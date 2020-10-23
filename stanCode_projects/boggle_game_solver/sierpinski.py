"""
File: sierpinski.py
Name: Alan Chen
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	draw sierpinski_triangle!
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the order of Sierpinski Triangle on each stacks
	:param length: The length of Sierpinski Triangle on each stacks
	:param upper_left_x: The upper left x coordinate of each Triangle
	:param upper_left_y: The upper left y coordinate of each Triangle
	"""
	if order == 0:
		return
	else:
		order -= 1
		a = GLine(upper_left_x, upper_left_y, upper_left_x + 0.5 * length, upper_left_y + 0.866 * length)
		b = GLine(upper_left_x + 0.5 * length, upper_left_y + 0.866 * length, upper_left_x + length, upper_left_y)
		c = GLine(upper_left_x + length, upper_left_y, upper_left_x, upper_left_y)
		sierpinski_triangle(order, length/2, upper_left_x, upper_left_y)
		sierpinski_triangle(order, length/2, upper_left_x + 0.5 * length/2, upper_left_y + 0.866 * length/2)
		sierpinski_triangle(order, length/2, upper_left_x + length/2, upper_left_y)
		window.add(a)
		window.add(b)
		window.add(c)


if __name__ == '__main__':
	main()