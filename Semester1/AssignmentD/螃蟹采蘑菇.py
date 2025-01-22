from collections import deque

def chk():
    for i in range(n):
        for j in range(n):
            if a[i][j] == 5:
                for nx, ny in directions:
                    tx, ty = i + nx, j + ny
                    if 0 <= tx < n and 0 <= ty < n and a[tx][ty] == 5:
                        return i, j, nx, ny

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
sx, sy, adjustx, adjusty = chk()
flag = [[False] * n for _ in range(n)]
flag[sx][sy] = True
q = deque([(sx, sy)])
while q:
    x, y = q.popleft()
    if a[x][y] == 9 or a[x + adjustx][y + adjusty] == 9:
        print("yes")
        exit(0)
    for nx, ny in directions:
        tx, ty = x + nx, y + ny
        tx2, ty2 = tx + adjustx, ty + adjusty
        if 0 <= tx < n and 0 <= ty < n and 0 <= tx2 < n and 0 <= ty2 < n and\
                not flag[tx][ty] and a[tx][ty] != 1 and a[tx2][ty2] != 1:
            flag[tx][ty] = True
            q.append((tx, ty))
print("no")