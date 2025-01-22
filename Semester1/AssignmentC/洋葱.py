import math
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
sums = [0] * math.ceil(n / 2)
if n % 2 == 1:
    sums[-1] = matrix[math.ceil(n / 2) - 1][math.ceil(n / 2) - 1]
for layer in range(math.ceil(n / 2)):
    i, j = layer, layer
    for di, dj in directions:
        for _ in range(n - layer * 2 - 1):
            sums[layer] += matrix[i][j]
            i += di
            j += dj
print(max(sums))