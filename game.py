from jorcademy import *

# Circle properties
circle_color: color = (255, 100, 100)
circle_x: float = 400
circle_y: float = 300
circle_width: float = 200 


# Makes circle move based on user input
def handle_user_input():
    global circle_color
    global circle_x
    global circle_y
    global circle_width

    if key_up_down:
        circle_y -= 1
    
    if key_right_down:
        circle_x += 1
    
    if key_down_down:
        circle_y += 1
    
    if key_left_down:
        circle_x -= 1


def setup() -> None:
    # Create an 800x600 screen
    screen(800, 600)


def draw() -> None:
    global circle_color
    global circle_x
    global circle_y
    global circle_width

    # Handle movement of the circle
    handle_user_input()

    # Draw the backdrop
    backdrop((255, 255, 255))

    # Draw the circle
    ellipse(circle_color, 
            circle_x, 
            circle_y, 
            circle_width, 
            circle_width)

