from slitherzenith import *
from components.game_object.game_object import GameObject


class Collider(GameObject):
    """
    A collider for a game_object
    """

    def __init__(self, parent: GameObject) -> None:
        self.parent = parent
        super().__init__(parent.x, parent.y, parent.width, parent.height)

        # Width and height offset for collider
        self.offset_width = 0
        self.offset_height = 0

        # Apply offset
        self.width += self.offset_width
        self.height += self.offset_height

    def collides_with(self, other) -> bool:
        """
        Check if the collider collides with another collider

        :param other: The other collider
        :return: Whether the collider collides with the other collider
        """
        return self.x < other.x + other.width and \
            self.x + self.width > other.x and \
            self.y < other.y + other.height and \
            self.y + self.height > other.y

    def update(self) -> None:
        """
        Update the collider

        :return: None
        """
        self.x = self.parent.x
        self.y = self.parent.y

    def draw(self) -> None:
        """
        Draw the collider

        :return: None
        """
        rect((255, 0, 0), self.x, self.y, self.width, self.height)
