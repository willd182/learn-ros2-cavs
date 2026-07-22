# Initial Software
To start writing the code for the Set-Speed Manager, you'll create a C++ class consisting of a header file and a source file.

Create the following files:

- `include/set_speed_manager/set_speed_manager.hpp`
- `src/set_speed_manager.cpp`

We'll be using the concepts of [Object Oriented Programming](https://www.geeksforgeeks.org/cpp/object-oriented-programming-in-cpp/) (OOP) to create an object that contains all the functionality of our Set-Speed Manager. In short, that means defining a class with all the necessary attributes and methods.

> **Note:** OOP also contains concepts such as *inheritance* and *polymorphism*. These are used for modeling more complex hierarchies of classes, which isn't super relevant here.

## C++ Class Usage Example
Below is an example of an incomplete `SetSpeedManager` class. It initializes the set speed at 0 meters per second and provides a public method for retrieving the set speed.

### Header (`set_speed_manager.hpp`)

```cpp
#ifndef SET_SPEED_MANAGER_HPP
#define SET_SPEED_MANAGER_HPP

class SetSpeedManager
{
    public:
        SetSpeedManager();

        int getSpeed() const;
    
    private:
    int set_speed_;
};
#endif
```

### Source (`set_speed_manager.cpp`)
```cpp
#include "set_speed_manager/set_speed_manager.hpp"

SetSpeedManager::SetSpeedManager()
    : set_speed_(0) 
{
}

int SetSpeedManager::getSpeed() const
{
    return set_speed_;
}
```

> **Note:** Member functions can be added or removed as needed, but every class should define a constructor to initialize its member variables.


## Set-Speed Manager Blueprint
Below is a brief description of the likely member variables and member functions your class will need. Use this to create an initial version of your class.

### Member Variables

The `SetSpeedManager` stores the data it needs to manage the current set speed.

| Attribute | Description |
|-----------|-------------|
| `set_speed_` | The currently stored set speed. |
| `minimum_speed_` | The lowest speed that can be set. |
| `maximum_speed_` | The highest speed that can be set. |

### Member Functions

The `SetSpeedManager` exposes methods that allow other parts of the application to interact with the stored set speed.

| Method | Description |
|--------|-------------|
| `SetSpeedManager()` | Creates a new `SetSpeedManager` object and initializes its member variables. |
| `setSpeed(int speed)` | Updates the stored set speed after validating the value. |
| `getSpeed()` | Returns the current set speed. |
| `increment()` | Increases the set speed by one increment. |
| `decrement()` | Decreases the set speed by one increment. |
