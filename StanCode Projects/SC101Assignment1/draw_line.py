"""
File: draw_line.py
Name: Zining Chen
-------------------------
This file shows how to use event-driven program "onmouseclicked(function)" to trigger the hole and line take turns
appearing separately.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 30
window = GWindow()
is_oval = False
hole = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """

    onmouseclicked(create_hole_and_line)


def create_hole_and_line(mouse):
    global is_oval, hole
    if not is_oval:
        hole = GOval(SIZE, SIZE)
        hole.filled = False
        hole.color = 'black'
        window.add(hole, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        is_oval = True
    else:
        window.remove(hole)
        line = GLine(hole.x-SIZE/2, hole.y-SIZE/2, mouse.x, mouse.y)
        line.filled = True
        window.add(line)
        is_oval = False


if __name__ == "__main__":
    main()
