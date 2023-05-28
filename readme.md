# JorCademy Engine
This template is built for courses on programming, created for JorCademy. It will therefore mainly be used for educational purposes.  

---

## Contents
This section is used to quickly browse through the documentation.
- [Files](#files)
- [Libraries](#libraries)
- [Practical information](#practical-information)

---

## Files
The following files are crucial to understand the inner workings of the template.

<br>

### <i>engine.py</i>
This file is used to setup the PyGame renderer and to render all the drawable objects onto the screen. This file should not contain any gameplay code.  

<br>

### <i>jorcademy.py</i>
This file contains helper functions the developer can use to build their game in <i>game.py</i>. This file mainly contains functions which can be used to draw shapes and change the properties of the game screen. Besides, this module contains the ```draw_buffer```, which contains all objects that need to be drawn onto the screen by the engine. 

<br>

### <i>primitives.py</i>
This file contains classes for objects which can be drawn onto the screen. To be more precise, it contains the ```DrawableObject``` class and its subclasses. The most important method inside these classes is ```draw```, which is used by the engine to easily draw different types of objects onto the screen.

<br>

### <i>game.py</i>
This file is meant to contain the gameplay code of the game. It is the file the gameplay developer will work with. The other files are not relevant to the gameplay developer. 

---


## Libraries

## Practical information
