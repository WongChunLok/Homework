n=int(input())
count=0

for i in range(n):
    lis1=list(map(int,input().split()))
    if sum(lis1)>=2:
        count+=1

print(count)