from collections import defaultdict

cases = int(input())

for _ in range(cases):
    situation = "alive"
    n, m, b = map(int, input().split())
    a = defaultdict(list)
    
    for _ in range(n):
        x, y = map(int, input().split())
        a[x].append(y)
        
    for x in sorted(a):
        if m >= len(a[x]):
            b -= sum(a[x])
        else:
            a[x].sort(reverse=True)
            b -= sum(a[x][:m])
        if b <= 0:
            situation = x
            break
    
    print(situation)