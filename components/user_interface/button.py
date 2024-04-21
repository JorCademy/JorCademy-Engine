from components.support.settings import scale
from components.support.input import *
import components.support.input as inp
from slitherzenith import *


class Button:
    """
    A button
    """

    def __init__(self, pos,
                 w, h,
                 content, content_size, content_color,
                 button_color, hover_color,
                 border=False, border_size=5, border_color=(50, 50, 50)) \
            -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.width = w
        self.height = h

        # Button state
        self.selected = False

        # Button text
        self.content = content
        self.content_size = content_size
        self.content_color = content_color
        self.font = "fonts/pixel.ttf"

        # Button color
        self.button_color = button_color
        self.orig_button_color = button_color
        self.hover_color = hover_color

        # Border
        self.border_enabled = border
        self.border_size = border_size
        self.border_color = border_color

    def is_hovered(self) -> bool:
        """
        Check if the button is hovered

        :return: Whether the button is hovered
        """
        if self.selected:
            return True

        if (self.x - self.width / 2 * scale <=
                pygame.mouse.get_pos()[0]
                <= self.x + self.width / 2 * scale and
                self.y - self.height / 2 * scale
                <= pygame.mouse.get_pos()[1]
                <= self.y + self.height / 2 * scale):
            return True

    def clicked(self) -> bool:
        """
        Check if the button is clicked

        :return: Whether the button is clicked
        """
        if not inp.clickable:
            return False

        if self.is_hovered():
            inp.clickable = not (pygame.mouse.get_pressed()[0] or
                                 is_nintendo_switch_pro_button_down(SWITCH_A))
            return pygame.mouse.get_pressed()[0] or return_key_pressed()

    def update(self) -> None:
        """
        Update the button

        :return: None
        """
        if self.is_hovered():
            self.button_color = self.hover_color
        else:
            self.button_color = self.orig_button_color

    def draw(self) -> None:
        """
        Draw the button
        :return: None
        """
        # Draw border
        if self.border_enabled:
            rect(self.border_color,
                 self.x,
                 self.y,
                 self.width * scale + self.border_size * scale,
                 self.height * scale + self.border_size * scale)

        # Draw button
        rect(self.button_color,
             self.x,
             self.y,
             self.width * scale,
             self.height * scale)

        # Draw text
        text(self.content,
             int(self.content_size * scale),
             self.content_color,
             self.x,
             self.y,
             self.font)
