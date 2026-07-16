# ROS2 Package Creation
Your first task is to create a new package to contain your 

## Python Package Creation Command
To create a package for python based code, use the following command

```bash
cd /workspaces/learn-ros2-cavs 
ros2 pkg create --build-type ament_python --dependencies rclpy --license Apache-2.0 Set_Speed_Manager
```

A new directory should appear in your workspace with the name `Set_Speed_Manager`. This directory is an empty template to fill with your code. Commit this to your feature branch.

```bash
git add .
git commit -m "Package Creation"
```

> **Note:** Try using `git status` before and after `git add .` to see how the command output changes.

This commit acts as a baseline which allows you to start tracking changes you make to your package. 

# About Package Structure
A ROS2 package is a directory containing source code,. build files, and configuration files for a specific node or software module. The layout of the package can depend on the build type (ament_cmake or ament_python).

Python packages follow the standard python module distribution format.
- **resource/:** Contains a marker file that allows the package to be found
- **<package_name>/:** Subdirectory matching package name that contains your python source code
- **test/:** Contains tests for your python source code
- **package.xml:** Contains metadata (name, version, maintainer, dependencies)
- **setup.cfg:** Required configuration when a package has executables (so ROS2 can find them)
- **setup.py:** Defines package attributes and installation instructions

> **Note:** The most commonly used directories will be your source code, tests, and package metadata in real world development.

# Test-Build your New Package
To ensure that your package was built correctly, run the following command:

```bash
colcon build
```

You should see an output like:
> Starting >>> Set_Speed_Manager
>
> Finished <<< Set_Speed_Manager [3.91s]          
> 
> Summary: 1 package finished [4.88s]

This command will create three directories with build artifacts:
- /build
- /install
- /log

This is the compiled version of your code, which is ignored by git on purpose since it tends to change frequently.