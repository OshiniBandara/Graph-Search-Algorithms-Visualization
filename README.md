# Graph-Search-Algorithms-Visualization
This project is a Python-based GUI application built using PyQt6 and NetworkX to visualize and compare various graph search algorithms. 

It allows users to select a start and end node in a predefined graph and run different search algorithms to find the shortest path. The program also displays the path, execution time, and the number of nodes explored for each algorithm.

## Features
### Graph Representation:

The graph represents a supermarket layout, with nodes as sections (e.g., "Entrance", "Fruits", "Dairy") and edges as paths between sections with associated weights.

The graph is predefined and visualized using NetworkX and Matplotlib.

# Search Algorithms:

* BFS (Breadth-First Search)

* DFS (Depth-First Search)

* Dijkstra's Algorithm

* A* Search

* UCS (Uniform Cost Search)

* DLS (Depth-Limited Search)

* IDS (Iterative Deepening Search)

* BDS (Bidirectional Search)

## GUI Features:

- Dropdown menus to select the start and end nodes.

- A table to display the results of each algorithm, including:

    * Algorithm name

    * Path found

    * Execution time

    * Number of nodes explored

- A graph visualization that highlights the path found by the selected algorithm.

## Requirements

To run this program, you need the following Python libraries installed:

* PyQt6: For the graphical user interface.

* NetworkX: For graph creation and manipulation.

* Matplotlib: For graph visualization.

## Code Structure

### Graph Definition:

The graph is defined using NetworkX with weighted edges representing the supermarket layout.

### Search Algorithms:

BFS, DFS, Dijkstra, and A* are implemented using NetworkX functions.

UCS, DLS, IDS, and BDS are implemented as custom algorithms.

## GUI:

The GUI is built using PyQt6 and includes:

* A QTableWidget to display results.

* A FigureCanvas to visualize the graph.

* Dropdown menus and buttons for user interaction.


