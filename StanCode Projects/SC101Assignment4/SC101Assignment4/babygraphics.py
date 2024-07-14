"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = int(GRAPH_MARGIN_SIZE+((width-GRAPH_MARGIN_SIZE)/len(YEARS)*year_index))
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    width = int(CANVAS_WIDTH)
    for vertical_lines in range(len(YEARS)):
        x = get_x_coordinate(width, vertical_lines)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[vertical_lines]),
                           anchor=tkinter.NW)


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

    # ----- Write your code below this line ----- #
    width = int(CANVAS_WIDTH)
    # name=key, year&rank = value
    for i in range(len(lookup_names)):
        # lookup_names' type is list <iterable>
        name = lookup_names[i]
        year_and_rank = name_data[name]
        # year = key, rank = value
        # check if the name exists in top 1000 in 1910, 1920......separately
        for j in range(len(YEARS)):
            year = str(YEARS[j])
            # The first spot only needs the text created. There's no line needs to be drawn.
            if j == 0:
                x = get_x_coordinate(width, j) + TEXT_DX
                # check if the name is in top 1000 in YEARS[j]
                if year in year_and_rank:
                    rank = int(year_and_rank[year])
                    y = int((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000 * rank + GRAPH_MARGIN_SIZE)
                    # check if the name list longer than color list
                    if i <= len(COLORS):
                        canvas.create_text(x+TEXT_DX, y, text=str(name) + ' ' + str(rank), anchor=tkinter.SW, fill=COLORS[i])
                    else:
                        canvas.create_text(x+TEXT_DX, y, text=str(name) + ' ' + str(rank), anchor=tkinter.SW,
                                           fill=COLORS[i-len(COLORS)])
                # the name is not in top 1000 in YEARS[j]
                else:
                    y = int((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE))
                    rank = '*'
                    if i <= len(COLORS):
                        canvas.create_text(x+TEXT_DX, y, text=str(name) + ' ' + str(rank), anchor=tkinter.SW, fill=COLORS[i])
                    else:
                        canvas.create_text(x+TEXT_DX, y, text=str(name) + ' ' + str(rank), anchor=tkinter.SW,
                                           fill=COLORS[i-len(COLORS)])
            if j >= 1:
                # use YEAS[j] to get the position for the certain year in the years list
                last_x = get_x_coordinate(width, j - 1)
                x = get_x_coordinate(width, j)
                last_year = str(YEARS[j - 1])
                # check if the name is in top 1000 in the last year as y will be different
                if last_year in year_and_rank:
                    last_rank = int(year_and_rank[last_year])
                    last_y = int((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2)/1000*last_rank + GRAPH_MARGIN_SIZE)
                else:
                    last_y = int((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE))
                # check if the name is in top 1000 in this year as y will be different
                if year in year_and_rank:
                    rank = int(year_and_rank[year])
                    y = int((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 1000 * rank + GRAPH_MARGIN_SIZE)
                # the name is not in top 1000 in YEARS[j]
                else:
                    y = int((CANVAS_HEIGHT - GRAPH_MARGIN_SIZE))
                    rank = '*'
                # check if the name list longer than color list
                if i <= len(COLORS):
                    canvas.create_line(last_x, last_y, x,
                                       y, fill=COLORS[i], width=LINE_WIDTH)
                    canvas.create_text(x+TEXT_DX, y, text=str(name) + ' ' + str(rank), anchor=tkinter.SW, fill=COLORS[i])
                else:
                    canvas.create_line(last_x, last_y, x, y, fill=COLORS[i-len(COLORS)], width=LINE_WIDTH)
                    canvas.create_text(x+TEXT_DX, y, text=str(name) + ' ' + str(rank), anchor=tkinter.SW,
                                       fill=COLORS[i-len(COLORS)])


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
