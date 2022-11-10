# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas)
    draw_ground(canvas)
    draw_cloud(canvas)
    draw_fence(canvas)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.


def draw_sky(canvas):
    draw_rectangle(canvas, 0, 0, 800, 500, fill = "skyblue")

def draw_ground(canvas):
    draw_rectangle(canvas, 0, 0, 800, 100, fill = "green", outline = "green")
def draw_cloud(canvas):
    draw_oval(canvas, 100, 400, 200, 300, fill = "white", outline = "white")
    draw_oval(canvas, 150, 350, 200, 270, fill = "white", outline = "white")
    draw_oval(canvas, 150, 370, 250, 325, fill = "white", outline = "white")
    draw_oval(canvas, 80, 380, 250, 350, fill = "white", outline = "white")
    draw_oval(canvas, 300, 500, 200, 305, fill = "white", outline = "white")
    draw_oval(canvas, 650, 450, 220, 280, fill = "white", outline = "white")
    draw_oval(canvas, 650, 470, 250, 345, fill = "white", outline = "white")
    draw_oval(canvas, 580, 580, 350, 170, fill = "white", outline = "white")
def draw_fence(canvas):
    for i in range(12):
        draw_rectangle(canvas, (i * 70) +50, 80,  (i* 70) , 200, fill = "white", outline = "black")
# this program will start executing.
main()