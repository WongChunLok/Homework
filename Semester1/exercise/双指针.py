str1='abc'
visited=[]
def f(n):
    if n ==3:
        print(visited)
    else:
        for i in str1:
            if i not in visited:
                visited.append(i)
                f(n+1)
                visited.remove(i)

f(1)

