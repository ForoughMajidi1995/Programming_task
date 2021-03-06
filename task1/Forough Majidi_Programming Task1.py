# -*- coding: utf-8 -*-
"""Forough Majidi_Programming Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bq85tr08BX4N_f8hwkQkn2cOF4e5pLix

The purpose of this question is to find the connected components in a graph. We can use Breadth-first search (BFS) to solve this problem.
Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
Thus, this problem can be reduced to finding the number of BFS calling.
"""

from collections import deque

# There are 8 possible movement which we can go from each cell. these movements are listed in below
# (top, right, bottom, left and 4 diagonal moves)
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

# Befor going to each cell we should check whether we can go or not. We should check 3 prerequisite before going to each cell.
# 1)It must be valid matrix coordinates
# 2)It must represent water
# 3)The cell must not be processed
# If these three conditions are met, then function is_safe_to_go returns true
def is_safe_to_go(matrix, x, y, processed):
	return (x >= 0) and (x < len(processed)) and \
		   (y >= 0) and (y < len(processed[0])) and \
		   (matrix[x][y] == 0 and not processed[x][y])

def BFS(matrix, processed, i, j):

	# create an empty queue
	# enqueue source node
	q = deque()
	q.append((i, j))

	# mark source node as processed
	processed[i][j] = True

	# loop till queue is empty
	while q:

		# pop front node from queue and process it
		x, y = q.popleft()

		# The code below Check for safety of each possible movements around the popped up cell by using is_safe_to_go function
		# enter the valid cells from current cell to the queue
		for k in range(8):
			# Skip if location is invalid or already processed or is land
			if is_safe_to_go(matrix, x + row[k], y + col[k], processed):
				# skip if location is invalid or it is already
				# processed or is land
				processed[x + row[k]][y + col[k]] = True
				q.append((x + row[k], y + col[k]))

if __name__ == '__main__':

	matrix = [
		[1, 0, 1, 0, 0, 0, 1],
		[0, 0, 1, 0, 1, 0, 1],
		[1, 1, 1, 1, 0, 0, 1],
		[1, 0, 0, 1, 0, 1, 0],
		[1, 1, 1, 1, 0, 0, 0],
		[0, 1, 0, 1, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 1],
		[0, 0, 0, 1, 0, 0, 1],
		[1, 0, 1, 0, 1, 0, 0],
		[1, 1, 1, 1, 0, 0, 0]
	]

	(M, N) = (len(matrix), len(matrix[0]))

	# stores if cell is processed or not
	processed = [[False for x in range(N)] for y in range(M)]


# The number of lakes is zero at first
	lake = 0
# Strats from top left cell
# Check all nodes in each raw
# Then go to next raw
	for i in range(M):
		for j in range(N):
			# start BFS from each unprocessed node and increment lake count
			if matrix[i][j] == 0 and not processed[i][j]:
				BFS(matrix, processed, i, j)
				lake = lake + 1

	print("Number of lakes are", lake)
