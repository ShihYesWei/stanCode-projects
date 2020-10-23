"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program draws line graphs with tkinter based on data organized from babynames.
X-axis is years and Y-axis is the ranking of the name.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    n = width - GRAPH_MARGIN_SIZE*2    # the usable range
    n /= len(YEARS)                    # divide the usable range into number of years
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * n
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    width = CANVAS_WIDTH
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)   # most left line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)   # most top line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)  #most bottom line
    for i in range(len(YEARS)):  # draw the vertical lines based on each decades
        year_index = i
        canvas.create_line(get_x_coordinate(width, year_index), 0, get_x_coordinate(width, year_index), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(width, year_index),CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    width = CANVAS_WIDTH
    height = CANVAS_HEIGHT
    for n in range(len(lookup_names)):
        name = lookup_names[n]  # get each name from lookup_names
        for i in range(len(YEARS)):
            year_index = i  # get the year index
            year = YEARS[i]  # get each year from YEARS
            x_year = get_x_coordinate(width, year_index)  # the x-position of this year
            if str(year) in name_data[name]:  # if rank <= 1000
                rank = name_data[name][str(year)]
            else:  # if rank > 1000
                rank = '*'  # unranked is shown as *
            y_year = get_y_coordinate(height, rank) # the y-position of this name in this year
            canvas.create_text(x_year + TEXT_DX, y_year, text= str(name)+' '+str(rank), anchor=tkinter.SW, fill=COLORS[n%len(COLORS)])
            if i != 0:
                canvas.create_line(pre_x_year, pre_y_year, x_year, y_year, width=LINE_WIDTH ,fill=COLORS[n%4])
            pre_x_year = x_year  # the x-position from previous decade
            pre_y_year = y_year  # the y-position from previous decade


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the correspond rank of name
    , returns the y coordinate based on the ranking.

    Input:
        height (int): The height of the canvas
        rank (str): The rank of the name in the current year, the type will be switched from str into int
    Returns:
        y_coordinate (int): The y coordinate of the name based on the rank.
    """
    if rank == '*':
        rank = 1000  # if the name is unranked, the y-position is set same as rank 1000
    else:
        rank = int(rank)
    y_coordinate = height - 2*GRAPH_MARGIN_SIZE  #the usable range
    y_coordinate /= 1000
    y_coordinate *= rank
    y_coordinate += GRAPH_MARGIN_SIZE
    return y_coordinate





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
