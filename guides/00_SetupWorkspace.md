# ROS2 Workspace Setup Instructions
To set up a ROS2 workspace, you must first have a linux environment to work in. If you are on windows, this means installing [WSL](https://learn.microsoft.com/en-us/windows/wsl/about) on your machine.

## Installing WSL

To install WSL, open up a powershell terminal as admin and run the following command:

```bash
wsl --install
```

It will ask you to make a default user account. Fill out all necessary info. 

## Installing Docker
The simplest way to develop in ROS2 is to launch a docker image with it already installed. For this you'll need to [install docker](https://docs.docker.com/engine/install/ubuntu/). Ensure that you run these commands in your linux or WSL environment.

## Creating your own Branch
Open a new linux terminal and navigate to the home directory by running `cd ~`. 

Then, clone this github repo into your linux environment using the following commands.

```bash
git clone https://github.com/willd182/learn-ros2-cavs.git
```

Change the current directory to the repo and make your own branch to work on. Name the branch using your own first and last name in the same format.

```bash
cd learn-ros2-cavs
git branch first-last
git checkout first-last
```

You should now have a copy of this repository within the WSL 

## Opening ROS2 Workspace in Docker using VSCode
Visual Studio Code provides a useful extension, [devcontainers](https://code.visualstudio.com/docs/devcontainers/containers), for working with docker images. 

To get started, open a new VSC window and connect it to WSL using `CTRL+SHIFT+P` and running `WSL: Connect to WSL`. The bottom left of the window should now show a remote development indicator (>< WSL: UBUNTU>).

Next, open the github repo in VSC. It should automatically detect the devcontainer and prompt you to "re-open in container". Feel free to click this. Otherwise, use `CTRL+SHIFT+P` and run `Dev Containers: Reopen in Container`. The remote development indicator should now be (>< Dev Container: ROS2 Jazzy).

## Final Checks
As a final check, try running `which ros2` in a new terminal. It should output something like `/opt/ros/jazzy/bin/ros2` which is the location of the ROS2 executable. This image comes preinstalled with everything you need to complete the tutorials in this repo.

By this point, you should have a working ROS2 workspace! The next time you open this project in VSCode, it will remember your configuration and open the devcontainer. 

If you open a new project, remember that you can use File->Open Recent to access this project again.