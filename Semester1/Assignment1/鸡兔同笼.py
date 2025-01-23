n=int(input())

if n%4 ==0:
    less=n/4
elif n%4==2:
    less=(n/4)+1
else:
    less=n/4

if n%2==0:
    print(int(less),int(n/2))
else:
    print(0,0)