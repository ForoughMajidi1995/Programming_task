# Programming_task
This files contains the answers of the tasks

Forough Majidi - Programming task

Task1:
The purpose of this question is to find the connected components in a graph. We should count the number of groups of connected components. We can use Breadth-first search (BFS) to solve this problem. Thus, this problem can be reduced to finding the number of BFS calls.

What is BFS?
In graph theory, Breadth-first Search (BFS) is one of the graph navigation algorithms. The first level search strategy for graph navigation, as its name implies, is "graph level by level search". The algorithm starts at the root (in graphs or trees without roots, the desired vertex is selected as the root) and places it at level one. At each stage, it visits all the neighbors of the vertices of the last unseen level and places them on the next level. This process stops when all the neighbors of the last level vertices have already been seen. Also, in problems where the various states corresponding to the vertices of a graph and the solution of the problem requires finding the vertex of the target with certain properties, which at the same time is the closest to the root among all the target vertices, the first level search is uncreative. In this way, the algorithm visits all the neighbors of one vertex each time and then goes to the next vertex, so the graph will be scrolled level by level. This process continues until the vertex of the target is found or the entire graph is probably traversed. From a practical point of view, a queue is used to implement this algorithm. In this way, the root is placed in the queue first. Each time the element at the beginning of the queue is pulled out, its neighbors are checked, and any neighbors that have never been seen are added to the bottom of the queue.

The code of this task is in this directory: (Forough Majidi-Programming Task\Task1\Forough Majidi_Programming Task1.ipynb)

Task2:
In this section, it was requested to extract the GitHub pull requests. To extract all the pull requests, a crawler is written in the Python programming language. Libraries such as selenium and Beautiful Soup have been used in this crawler. This program extracts all open and closed pull requests.

The .csv files of this task are in this directory: (Forough Majidi-Programming Task\Task2\csv files)
The codes of crawler are in this directory: (Forough Majidi-Programming Task\Task2\codes of crawler)
