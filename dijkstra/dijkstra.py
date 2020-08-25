N = 5
map = [[10000]*N for i in range(N)]
map[0][1] = 2
map[1][3] = 2
map[3][4] = 3
map[0][4] = 7
map[0][2] = 3
map[2][4] = 5


known = [[0,0]]
unknown = []

for i in range(1, N):
    unknown.append([i, map[0][i]])
unknown.sort(key = lambda x : x[1])

while len(unknown) > 0:
    known.append(unknown[0])
    del unknown[0]
    for node in unknown:
        node[1] = min(node[1], known[-1][1] + map[known[-1][0]][node[0]])
    unknown.sort(key = lambda x : x[1])

print(known)


