n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x + 1, y + 1))
a = sorted(a, key = lambda _: _[0])
dp = [0] * 65
for i in range(n):
    for j in range(a[i][1], 62):
        dp[j] = max(dp[j], dp[a[i][0] - 1] + 1)
print(dp[61])