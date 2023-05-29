# JorCademy Engine

This template is built for courses on programming, created for JorCademy. It will therefore mainly be used for educational purposes.  

---

## Contents
This section is used to quickly browse through the documentation.
- [Files](#files)
- [Dependencies](#dependencies)
- [Practical information](#practical-information)
- [Maintenance](#maintenance)

---

## Files
The following files are crucial to understand the inner workings of the template.


### <i>engine.py</i>
This file is used to setup the PyGame renderer and to render all the drawable objects onto the screen. This file should not contain any gameplay code.  


### <i>jorcademy.py</i>
This file contains helper functions the developer can use to build their game in <i>game.py</i>. This file mainly contains functions which can be used to draw shapes and change the properties of the game screen. Besides, this module contains the ```draw_buffer```, which contains all objects that need to be drawn onto the screen by the engine. 
<br>
The JorCademy module provides the following building blocks at the moment (we suppose that the functionalities of these functions are clear):
- ```screen(width: int, height: int) -> None```
- ```title(t: str) -> None```
- ```backdrop(c: color) -> None```
- ```ellipse(c: color, x: float, y: float, w: float, h: float) -> None```
- ```rect(c: color, x: float, y: float, w: float, h: float) -> None```
- ```text(content: str, c: color, x: float, y: float) -> None```
- ```image(url: str, x: float, y: float, scale: float) -> None```



### <i>primitives.py</i>
This file contains classes for objects which can be drawn onto the screen. To be more precise, it contains the ```DrawableObject``` class and its subclasses. The most important method inside these classes is ```draw```, which is used by the engine to easily draw different types of objects onto the screen.


### <i>game.py</i>
This file is meant to contain the gameplay code of the game. It is the file the gameplay developer will work with. The other files are not relevant to the gameplay developer. 

---


## Dependencies
The template is supported by PyGame, a library used to create games with. In this template, it is used to set-up a screen to draw shapes on. In order to use this template, the installation of PyGame is required. This can be done through ```pip```, Python's package manager, using the terminal. The following terminal command can be used to install PyGame: 
```
pip install pygame
```

---

## Practical information
This section contains some instructions on how to use this template properly, as well as a number of examples. 


### Setup & Draw
The templates starts of with two functions: ```setup``` and ```draw```. Like with most game engines, the ```setup``` function is only executed once and can be used to initialize starting values of the game. The ```draw``` function is executed 60 times per second (once per frame) and can be used to update the game state (e.g, moving drawable objects).  
```
def setup() -> None:
    pass

def draw() -> None:
    pass
```


### Setting up the screen
Setting up the screen can be done using the ```screen``` function. Besides, the template provides helper functions to change properties of the screen, such as the title and backdrop (the latter can also be changed in the ```draw``` phase).
```
def setup() -> None:
    screen(800, 600)
    title("The best game ever made! UwU")
    backdrop((255, 255, 255))
```


### Drawing & moving shapes
Drawing and moving shapes can be done in the ```draw``` functions. Adding shapes is fairly easy due to helper functions from the JorCademy module. The code snippet below shows a program which draws a circle and slowly moves the circle to the bottom right of the screen. 
```
#Circle properties
x: float = 400
y: float = 300
w: int = 100
h: int = 100
circle_color: color = (12, 57, 100)

def setup() -> None:
    screen(800, 600)


def draw() -> None:
    global x
    global y
    global w
    global h
    global circle_color

    # Moving circle to the bottom-right
    x += 5
    y += 5

    # Drawing backdrop
    backdrop((0, 0, 0)))

    # Drawing the circle 
    ellipse(circle_color, x, y, w, h)
```
---

## Maintenance
As this template is used for educational purposes, we are planning to keep it up-to-date for the upcoming Python versions. However, it deserves to mention that JorCademy is, as it stands, a non-profit organization. Therefore, updates might take some time to be released. 

---

## Contact
If you have any questions or remarks, feel free to reach out: nickjordan2002@gmail.com
