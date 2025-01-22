T = int(input())

for i in range(T):
    list1 = list(map(int, input().split()))
    n = list1[0]
    m = list1[1]
    x = list1[2]
    y = list1[3]

    direct = [(-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    def dfs(x, y, lst, t):
        s = 0
        if t == n * m:
            return 1
        else:
            for v, w in direct:
                if (x + v, y + w) not in lst and x + v in range(n) and y + w in range(m):
                    lst.append((x + v, y + w))
                    s += dfs(x + v, y + w, lst, t + 1)
                    lst.pop()

        return s

    lst = [(x, y)]
    print(dfs(x, y, lst, 1))