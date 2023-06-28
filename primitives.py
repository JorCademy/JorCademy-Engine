import pygame


# Super class - representing objects that can be drawn on the screen
class DrawableObject:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.object_name = "Drawable"

    def get_type(self):
        return self.object_name

    def draw(self, context: pygame.display):
        pygame.draw.circle(context, self.x, self.y, 100)


# Derived class - representing an ellipse object 
class Ellipse(DrawableObject):
    def __init__(self, color, x, y, w, h):
        super().__init__(x, y, w, h)
        self.object_name = "Ellipse"
        self.color = color

    def draw(self, context: pygame.display):
        center = (self.x, self.y)
        circle_rect = pygame.Rect(center[0] - self.width / 2,
                                  center[1] - self.height / 2,
                                  self.width,
                                  self.height)
        pygame.draw.ellipse(context,
                            self.color,
                            circle_rect,
                            self.width)


# Derived class - representing a rectangular object
class Rectangle(DrawableObject):
    def __init__(self, color, x, y, w, h):
        super().__init__(x, y, w, h)
        self.object_name = "Rectangle"
        self.color = color

    def draw(self, context: pygame.display):
        center = (self.x, self.y)
        rectangle_rect = pygame.Rect(center[0] - self.width / 2,
                                     center[1] - self.height / 2,
                                     self.width,
                                     self.height)
        pygame.draw.rect(context, self.color, rectangle_rect, self.width)


# Derived class - representing a text object
class Text(DrawableObject):
    def __init__(self, content, surface, color, x, y, w, h):
        super().__init__(x, y, w, h)
        self.object_name = "Text"
        self.color = color
        self.contents = content
        self.surface = surface

    def draw(self, context: pygame.display):
        # Set the position of the text
        text_position = self.surface.get_rect()
        text_position.center = (self.x, self.y)  # Centered on the screen
        context.blit(self.surface, text_position)


# Derived class - representing an image object
class Image(DrawableObject):
    def __init__(self, url, scale, x, y):
        super().__init__(x, y, None, None)
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

        # Draw image
        context.blit(image, image_rect)


# Representing an audio object
class Audio:
    def __init__(self, path):
        self.filepath = path

