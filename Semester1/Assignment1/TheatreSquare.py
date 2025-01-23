x,y,a=map(int,input().split())
g=0
f=0

if x%a==0:
    g+=(x//a)
else:
    g+=(x//a)+1

if y%a==0:
    f+=(y//a)
else:
    f+=(y//a)+1

print(g*f)
