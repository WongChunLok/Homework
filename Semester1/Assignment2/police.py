n=int(input())
lis1=list(map(int,input().split()))
crime=0
police=0

for i in range(len(lis1)):
    if lis1[i]<0:
        if police>=1:
            police-=1
        else:
            crime+=1
    else:
        police+=lis1[i]

print(crime)