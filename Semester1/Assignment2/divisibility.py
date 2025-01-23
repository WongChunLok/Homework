n=int(input())

for i in range(n):
    count=0
    a,b=map(int,input().split())
    if a%b != 0:
        if a>b:
            x=a//b
            total=b*(x+1)
            print(total-a)
        else:
            print(b-a)
    else:
        print(0)
        

