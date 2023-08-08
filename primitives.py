import pygame


# Super class - representing objects that can be drawn on the screen
class DrawableObject:
    def __init__(self, x, y, w, h, rotation=0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.object_name = "Drawable"
        self.rotation = rotation

    def get_type(self):
        return self.object_name

    def draw(self, context: pygame.display):
        pygame.draw.circle(context, self.x, self.y, 100)

    def rotate(self, image, angle, pivot):
        pos = (self.x, self.y)
        originPos = pivot

        # offset from pivot to center
        image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

        return rotated_image, rotated_image_rect


# Derived class - representing an ellipse object
class Ellipse(DrawableObject):
    def __init__(self, color, x, y, w, h, rotation=0):
        super().__init__(x, y, w, h, rotation)
        self.object_name = "Ellipse"
        self.color = color

    def draw(self, context: pygame.display):
        # Determine circle rect
        center = (self.x, self.y)
        rect = pygame.Rect(center[0] - self.width / 2,
                           center[1] - self.height / 2,
                           self.width,
                           self.height)

        # Create surface for rotated circle
        target_rect = pygame.Rect(rect)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.ellipse(shape_surf, self.color, (0, 0, *target_rect.size), self.width)

        # Rotate circle
        rotated_surf, rotated_rect = self.rotate(shape_surf, self.rotation, (self.width / 2, self.height / 2))

        # Draw circle
        context.blit(rotated_surf, rotated_rect)


# Derived class - representing a rectangular object
class Rectangle(DrawableObject):
    def __init__(self, color, x, y, w, h, rotation=0):
        super().__init__(x, y, w, h, rotation)
        self.object_name = "Rectangle"
        self.color = color

    def draw(self, context: pygame.display):
        # Create rect surface
        surface = pygame.Surface((self.width, self.height))
        surface.set_colorkey((0, 0, 0))
        surface.fill(self.color)

        # Convert surface to image
        image = surface.copy()

        # Rotate surface
        image, rect = self.rotate(image, self.rotation, (self.width / 2, self.height / 2))
        rect.center = (self.x, self.y)

        # Draw surface
        context.blit(image, rect)


# Derived class - representing a text object
class Text(DrawableObject):
    def __init__(self, content, surface, color, x, y, w, h, size, font, rotation):
        super().__init__(x, y, w, h, rotation)
        self.object_name = "Text"
        self.color = color
        self.contents = content
        self.surface = surface
        self.size = size
        self.font = font

    def draw(self, context: pygame.display):
        # Set the position of the text
        self.surface, text_position = self.rotate(self.surface, self.rotation, (self.width / 2, self.height / 2))
        text_position.center = (self.x, self.y)  # Centered on the screen
        context.blit(self.surface, text_position)


# Derived class - representing an image object
class Image(DrawableObject):
    def __init__(self, url, scale, x, y, flipped=False, rotation=0):
        super().__init__(x, y, None, None, rotation)
        self.flipped = flipped
        self.object_name = "Image"
        self.url = url
        self.scale = scale

    # NOTE: image must be inside the assets folder
    def draw(self, context: pygame.display):
        image = pygame.image.load("assets/" + self.url)

        # Resize image
        w = image.get_width()
        h = image.get_height()
        new_size = (w * self.scale, h * self.scale)
        image = pygame.transform.scale(image, new_size)

        # Place image in center of specified coordinates
        image_rect = image.get_rect()
        image_rect.center = (self.x, self.y)

        # If needed, flip image
        if self.flipped:
            image = pygame.transform.flip(image, True, False)

        # Rotate image
        image = pygame.transform.rotate(image, self.rotation)

        # Draw image
        context.blit(image, image_rect)


# Representing an audio object
class Audio:
    def __init__(self, channel: int, path: str):
        self.filepath = path
        self.channel = channel
