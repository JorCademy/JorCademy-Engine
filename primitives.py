import pygame


class DrawableObject:
    """
    Base class for drawable objects
    """

    def __init__(self, x, y, w, h, rotation=0) -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.object_name = "Drawable"
        self.rotation = rotation

    def get_type(self) -> str:
        """
        Get the type of the object

        :return: The type of the object
        """
        return self.object_name

    def draw(self, context: pygame.display) -> None:
        """
        Draw the object

        :param context: The context to draw the object on
        :return: None
        """
        pygame.draw.circle(context, self.x, self.y, 100)

    def rotate(self, image, angle, pivot) -> tuple:
        """
        Rotate an image

        :param image: The image to rotate
        :param angle: The angle to rotate the image by
        :param pivot: The pivot point to rotate the image around
        :return: The rotated image and its rect
        """
        pos = (self.x, self.y)
        origin_pos = pivot

        # offset from pivot to center
        image_rect = image.get_rect(
            topleft=(pos[0] - origin_pos[0],
                     pos[1] - origin_pos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # rotated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # rotated image center
        rotated_image_center = (pos[0] - rotated_offset.x,
                                pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(
            center=rotated_image_center)

        return rotated_image, rotated_image_rect


class Ellipse(DrawableObject):
    """
    Derived class - representing an ellipse object
    """

    def __init__(self, color, x, y, w, h, rotation=0) -> None:
        super().__init__(x, y, w, h, rotation)
        self.object_name = "Ellipse"
        self.color = color

    def draw(self, context: pygame.display) -> None:
        """
        Draw the ellipse

        :param context: The context to draw the ellipse on
        :return: None
        """
        # Determine circle rect
        center = (self.x, self.y)
        rect = pygame.Rect(center[0] - self.width / 2,
                           center[1] - self.height / 2,
                           self.width,
                           self.height)

        # Create surface for rotated circle
        target_rect = pygame.Rect(rect)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.ellipse(shape_surf,
                            self.color,
                            (0, 0, *target_rect.size),
                            self.width)

        # Rotate circle
        rotated_surf, rotated_rect = self.rotate(
            shape_surf,
            self.rotation,
            (self.width / 2, self.height / 2))

        # Draw circle
        context.blit(rotated_surf, rotated_rect)


class Rectangle(DrawableObject):
    """
    Derived class - representing a rectangle object
    """

    def __init__(self, color, x, y, w, h, rotation=0) -> None:
        super().__init__(x, y, w, h, rotation)
        self.object_name = "Rectangle"
        self.color = color

    def draw(self, context: pygame.display) -> None:
        """
        Draw the rectangle

        :param context: The context to draw the rectangle on
        :return: None
        """

        # Create rect surface
        surface = pygame.Surface((self.width, self.height))
        surface.set_colorkey((0, 0, 0))
        surface.fill(self.color)

        # Convert surface to image
        image = surface.copy()

        # Rotate surface
        image, rect = self.rotate(image,
                                  self.rotation,
                                  (self.width / 2, self.height / 2))
        rect.center = (self.x, self.y)

        # Draw surface
        context.blit(image, rect)


class Text(DrawableObject):
    """
    Text object
    """

    def __init__(self,
                 content,
                 surface,
                 color,
                 x, y,
                 w, h,
                 size,
                 font,
                 rotation) -> None:
        super().__init__(x, y, w, h, rotation)
        self.object_name = "Text"
        self.color = color
        self.contents = content
        self.surface = surface
        self.size = size
        self.font = font

    def draw(self, context: pygame.display) -> None:
        """
        Draw the text

        :param context: The context to draw the text on
        :return: None
        """
        self.surface, text_position = self.rotate(
            self.surface,
            self.rotation,
            (self.width / 2, self.height / 2))
        text_position.center = (self.x, self.y)  # Centered on the screen
        context.blit(self.surface, text_position)


class Image(DrawableObject):
    """
    Derived class - representing an image object
    """

    def __init__(self,
                 image,
                 scale=1,
                 x=0, y=0,
                 flipped=False,
                 rotation=0) -> None:
        super().__init__(x, y, None, None, rotation)
        self.flipped = flipped
        self.object_name = "Image"
        self.image = image
        self.scale = scale

    def draw(self, context: pygame.display) -> None:
        """
        Draw the image

        :param context: The context to draw the image on
        :return: None
        """
        # Resize image
        w = self.image.get_width()
        h = self.image.get_height()
        new_size = (w * self.scale, h * self.scale)
        image = pygame.transform.scale(self.image, new_size)

        # Place image in center of specified coordinates
        image_rect = image.get_rect()
        image_rect.center = (self.x, self.y)

        # If needed, flip image
        if self.flipped:
            image = pygame.transform.flip(image, True, False)

        # Rotate image
        image, image_rect = self.rotate(image,
                                        self.rotation,
                                        (new_size[0]/2, new_size[1]/2))

        # Draw image
        context.blit(image, image_rect)
