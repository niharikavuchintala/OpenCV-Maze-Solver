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
