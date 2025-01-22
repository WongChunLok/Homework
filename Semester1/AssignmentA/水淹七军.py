from sys import stdin
from collections import deque
get = map(int, stdin.read().split())
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))
def bfs(x, y):
    if (x, y) == (I, J):
        return True
    h = mat[x][y]
    queue = deque()
    queue.append((x, y))
    while queue:
        px, py = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = px + dx, py + dy
            if mat[nx][ny] < h:
                if (nx, ny) == (I, J):
                    return True
                queue.append((nx, ny))
                mat[nx][ny] = h
for _ in range(next(get)):
    yes = False
    M, N = next(get), next(get)
    mat = [[1e9 for i in range(N + 2)]] + [[1e9] + [0 for i in range(N)] + [1e9] for j in range(M)] + [[1e9 for i in range(N + 2)]]
    for i in range(1, 1 + M):
        for j in range(1, 1 + N):
            mat[i][j] = next(get)
    I, J = next(get), next(get)
    for i in range(next(get)):
        if yes:
            next(get)
            next(get)
        else:
            if bfs(next(get), next(get)):
                yes = True
    print("Yes" if yes else "No")