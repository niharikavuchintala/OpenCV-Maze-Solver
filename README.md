# OpenCV-Maze-Solver

## Problem Statement

Given a set of maze images:

- Red cells represent walls
- White cells represent open paths
- Start position: top-left corner (0,0)
- End position: bottom-right corner (39,39)

The goal is to:

1. Convert each maze image into a grid.
2. Find the shortest path using BFS.
3. Generate a solved maze image with the path highlighted.
4. Handle impossible mazes separately.
5. Compute a final password using the product of all valid path lengths modulo 1000000007.

## Prerequisites

Before running the project, make sure the following are installed:

- Python 3.x
- OpenCV

Install OpenCV using:
python -m pip install opencv-python numpy

## Generating Maze Images

This project requires maze images as input.

1. Download the **Maze Maker** folder.
2. Extract the contents.
3. Open a terminal in the folder containing the executable.
   Windows: .\MazeMaker 100
5. Generate exactly 100 maze images:
The generated maze images should be placed inside the mazes/ folder of this project.

## Smaple Images

-Access the images folder.
-To view a solved sample maze output, refer to 'solved maze.png'
-To view an impossible maze output, refer to 'impossible maze.png'

## Approach

### Image Processing
- Read maze images using OpenCV.
- Divide the image into a 40 × 40 grid.
- Detect wall cells based on red pixel count.

### Path Finding
- Use Breadth First Search (BFS).
- BFS guarantees the shortest path in an unweighted grid.
- Store parent cells to reconstruct the final path.

### Output Generation
- Valid mazes:
 - Shortest path highlighted in green.
- Impossible mazes:
  - Generate a special output image.

## Project Structure

project/
- mazes/    #input maze images
- code.py/  #main python code
- answers/  #generated solved answers
- password.txt  #final password
- runlog.txt   #execution log

### Run the Program

Open a terminal in the project folder and execute:
python code.py

### What the Program Does

1. Reads all maze images from the mazes/ folder.
2. Converts each maze image into a 40 × 40 grid.
3. Detects walls and valid paths.
4. Uses Breadth First Search (BFS) to find the shortest path.
5. Saves solved maze images in the answers/ folder.
6. Generates:
   - password.txt
   - runlog.txt

## Technologies Used

- Python
- OpenCV
- BFS (Breadth First Search)

## Learning Outcomes

- Image processing with OpenCV
- Grid representation of images
- BFS shortest path algorithm
- File handling in Python
- Basic project structuring
