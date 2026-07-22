# ROS2 Package Creation
Your first task is to create a new package to contain your code.

## C++ Package Creation Command
To create a package for c++ based code, use the following command

```bash
cd /workspaces/learn-ros2-cavs 
ros2 pkg create set_speed_manager --build-type ament_cmake --dependencies rclcpp
```

A new directory should appear in your workspace with the name `set_speed_manager`. This directory is an empty template to fill with your code. Commit this to your feature branch.

```bash
git add .
git commit -m "Package Creation"
```

> **Note:** Try using `git status` before and after `git add .` to see how the command output changes.

This commit acts as a baseline which allows you to start tracking changes you make to your package. 

# About Package Structure
A ROS2 package is a directory containing source code,. build files, and configuration files for a specific node or software module. The layout of the package can depend on the build type (ament_cmake or ament_python).

An `ament_cmake` package typically includes:
- **include/<package_name>/:** Contains public C++ header files for the package.
- **src/:** Contains the package's C++ source files and node implementations.
- **CMakeLists.txt:** Defines how the package is built, including source files, dependencies, executables, and installation rules.
- **package.xml:** Contains metadata (name, version, maintainer, dependencies)

# Test-Build your New Package
To ensure that your package was built correctly, run the following command:

```bash
colcon build
```

You should see an output like:
> Starting >>> set_speed_manager
>
> Finished <<< set_speed_manager [3.91s]          
> 
> Summary: 1 package finished [4.88s]

This command will create three directories with build artifacts:
- /build
- /install
- /log

This is the compiled version of your code, which is ignored by git on purpose since it tends to change frequently.