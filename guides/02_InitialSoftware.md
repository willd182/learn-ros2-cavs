# Initial Software
To start writing the code for the Set-Speed Manager, you need to create a new python file under `/Set_Speed_Manager/Set_Speed_Manager/`. You can do this in VSCode by right clicking on that folder and hitting 'New File'.

We'll be using the concepts of [Object Oriented Programming](https://www.geeksforgeeks.org/python/python-oops-concepts/) (OOP) to create an *object* that contains all the functionality of our Set-Speed Manager. In short, that means defining a class with all the necessary attributes and methods.

> **Note:** OOP also contains concepts such as *inheritance* and *polymorphism*. These are used for modeling more complex hierarchies of classes, which isn't super relevant here.

## Python Class Usage Example
Below is an example of an incomplete `SetSpeedManager` class. It initializes the set speed at 0 meters per second and provides a public method for retrieving the set speed.

```Python
class SetSpeedManager:
    def __init__(self):
        # Initialize the set speed as 0 m/s
        self.set_speed = 0
    
    def get_set_speed(self):
        return self.set_speed
```
> **Note:** Methods can be added and removed as needed, however, the `__init__` method is mandatory. The first input to all methods is a "self-reference" to the object itself. 


## Set-Speed Manager Blueprint
Below is a brief description of the likely attributes and methods your class will need. Use this to create an initial version of your class.

### Attributes

The `SetSpeedManager` stores the data it needs to manage the current set speed.

| Attribute | Description |
|-----------|-------------|
| `set_speed` | The currently stored set speed. |
| `minimum_speed` | The lowest speed that can be set. |
| `maximum_speed` | The highest speed that can be set. |

### Methods

The `SetSpeedManager` exposes methods that allow other parts of the application to interact with the stored set speed.

| Method | Description |
|--------|-------------|
| `__init__()` | Creates a new `SetSpeedManager` object and initializes its attributes. |
| `set_speed(speed)` | Updates the stored set speed after validating the value. |
| `get_speed()` | Returns the current set speed. |
| `increment_speed()` | Increases the set speed by one increment. |
| `decrement_speed()` | Decreases the set speed by one increment. |
