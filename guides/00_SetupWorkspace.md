# ROS2 Workspace Setup Instructions
To set up a ROS2 workspace, you must first have a linux environment to work in. If you are on windows, this means installing [WSL](https://learn.microsoft.com/en-us/windows/wsl/about) on your machine.

## Installing WSL

To install WSL, open up a powershell terminal as admin and run the following command:

```bash
wsl --install
```

It will ask you to make a default user account. Fill out all necessary info. 

## Installing Docker
The simplest way to develop in ROS2 is to launch a docker image with it already installed. For this you'll need to [install docker](https://docs.docker.com/engine/install/ubuntu/).

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