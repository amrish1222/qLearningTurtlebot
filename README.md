## Project for ENPM808F: Exploration of a Bounded Area using Q Learning
### Author1- Amrish Baskaran
### UID: 116301046

### Author2- Bala Murali Manoghar Sai Sudhakar
### UID: 116150712


### Install dependencies-
- Ubuntu 16.04
- [ROS Kinetic](http://wiki.ros.org/kinetic/Installation)
- Python 2.7 (ROS comes with it)
- [git](https://www.liquidweb.com/kb/install-git-ubuntu-16-04-lts/)

### Instructions
- Follow the steps to add the ROS package to catkin workspace

1. Follow the steps in the link to create a catkin workspace.
http://wiki.ros.org/catkin/Tutorials/create_a_workspace

2. Clone the package
```
git clone https://github.com/bsaisudh/qLearningTurtlebot
```

3. Use catkin_make to make the package in the catkin workspace

```
cd ~/catkin_ws/
catkin build
```
or use
```
catkin_make
```

4. Run the following command to make the python executable

```
cd ~/catkin_ws/
chmod -x src/qLearningTurtlebot/src/trainingMode.py
chmod -x src/qLearningTurtlebot/src/gameMode.py
```

5. Run the following command to update bash

```
source devel/setup.bash
```

### Running Instructions

1. Run the following command will launch the training processs for the corresponding map
- Maze 1
```
roslaunch qLearningTurtlebot trainMaze1.launch
```

- Maze 2
```
roslaunch qLearningTurtlebot trainMaze2.launch
```

- Maze 3
```
roslaunch qLearningTurtlebot trainMaze3.launch
```

2. To run the game on the fulling trained q-Table
- Maze 1
```
roslaunch qLearningTurtlebot gameMaze1.launch
```

- Maze 2
```
roslaunch qLearningTurtlebot gameMaze2.launch
```

- Maze 3
```
roslaunch qLearningTurtlebot gameMaze3.launch
```
