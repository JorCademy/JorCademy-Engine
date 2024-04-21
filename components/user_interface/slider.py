from components.support.input import *
from components.support.settings import scale
from slitherzenith import *


class Slider:

    def __init__(self,
                 x, y,
                 width, height,
                 component_color,
                 min_value, max_value,
                 value) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.orig_color = component_color
        self.color = component_color
        self.hover_color = (component_color[0] + 50,
                            component_color[1] + 50,
                            component_color[2] + 50)

        self.min_value = min_value
        self.max_value = max_value
        self.value = value

        self.selected = False
        self.dragging = False

    def update(self) -> None:
        """
        Update the slider

        :return: None
        """
        if (is_mouse_button_down("left") and
                self.x - self.width / 2 <=
                pygame.mouse.get_pos()[0] <=
                self.x + self.width / 2 and
                self.y - self.height / 2 <=
                pygame.mouse.get_pos()[1] <=
                self.y + self.height / 2):
            self.dragging = True

        # Update value
        if self.dragging:
            self.value = self.min_value + (self.max_value - self.min_value) * \
                         (pygame.mouse.get_pos()[0] -
                          (self.x - self.width / 2)) / self.width

            # Clamp value
            if self.value < self.min_value:
                self.value = self.min_value
            elif self.value > self.max_value:
                self.value = self.max_value

        # Update value with controller
        elif self.selected:
            if is_nintendo_switch_pro_button_down(SWITCH_D_LEFT):
                self.value -= 0.01
            elif is_nintendo_switch_pro_button_down(SWITCH_D_RIGHT):
                self.value += 0.01

            # Clamp value
            if self.value < self.min_value:
                self.value = self.min_value
            elif self.value > self.max_value:
                self.value = self.max_value

        if not is_mouse_button_down("left") and not self.selected:
            self.dragging = False

    def draw(self):
        if self.selected:
            self.color = self.hover_color
        else:
            self.color = self.orig_color

        # Draw component backdrop
        rect(self.color, self.x, self.y, self.width, self.height)

        # Draw slider value
        text(str(round(self.value, 2)),
             int(25 * scale),
             (0, 0, 0),
             self.x - self.width / 2 + self.width *
             (self.value - self.min_value) / (self.max_value - self.min_value),
             self.y - 40 * scale,
             "../assets/fonts/pixel.ttf")

        # Draw slider
        rect((50, 50, 50),
             self.x - self.width / 2 + self.width *
             (self.value - self.min_value) / (self.max_value - self.min_value),
             self.y,
             10 * scale,
             self.height * 4)
