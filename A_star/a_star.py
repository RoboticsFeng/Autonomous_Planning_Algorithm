from grid_map import GridMap
import numpy as np

N = 20

map_matrix = [[0]*N for i in range(N)]
for i in range(5, 8):
	map_matrix[5][i] = 1
for j in range(3, 8):
	map_matrix[j][2] = 1
map_matrix[3][3] = 1
map_matrix[3][4] = 1

f_map = [[0]*N for i in range(N)]
g_map = [[0]*N for i in range(N)]
parents = [[[0,0]]*N for i in range(N)]
close_map = [[False]*N for i in range(N)]

open_list = []

isSuccess = False
#1.add start to open list
open_list.append([0,0])

while len(open_list) > 0:
	#find the grid with min F
	open_list.sort(key = lambda x : f_map[x[0]][x[1]], reverse = True)
	#add to close list
	x = open_list[-1]
	close_map[x[0]][x[1]] = True
	open_list.pop()
	#search neighbor grids
	for i in [x[0]-1, x[0], x[0]+1]:
		for j in [x[1]-1, x[1], x[1]+1]:
			if i < 0 or i >= N or j < 0 or j >= N or map_matrix[i][j] == 1 or close_map[i][j]:
				continue
			else:
				if abs(i-x[0]) + abs(j-x[1]) == 2:
					cur_g = g_map[x[0]][x[1]] + 14
				else:
					cur_g = g_map[x[0]][x[1]] + 10
				
				if [i, j] not in open_list:
					open_list.append([i,j])
					parents[i][j] = x
					g_map[i][j] = cur_g
					f_map[i][j] = g_map[i][j] + abs(N-i-1)*10 + abs(N-j-1)*10
				else:
					if cur_g < g_map[i][j]:
						parents[i][j] = x
						g_map[i][j] = cur_g
						f_map[i][j] = g_map[i][j] + abs(N-i-1)*10 + abs(N-j-1)*10

	if [N-1, N-1] in open_list:
		isSuccess = True
		break;

#add path
path = []
cur = [N-1, N-1]
while True:
	path.append(cur)
	cur = parents[cur[0]][cur[1]]
	if cur == [0,0]:
		break;
path.append([0,0])
print(path)

grid_map = GridMap(map_matrix)
grid_map.add_path(path)
grid_map.show()

