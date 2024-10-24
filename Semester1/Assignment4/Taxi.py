input()
 
a,b,c,d=map(input().count,('1','2','3','4'))   #算对应组别的数量

total_taxi=d                                   #4个人直接一辆

if a>c:
    total_taxi+=c
    a-=c

    if  a%4==0:
        total_taxi+=a//4
        a-= (a//4)*4

    total_taxi+= b//2                         #若b是基数，b只会剩下1组2个人
    if b%2==0:
        b=0
        total_taxi+=1
    else:
        b=1
        if a==1 or a==2:
            total_taxi+=1
        elif a==3:
            total_taxi+=2

elif a<c:
    total_taxi+=c

    if b%2==0:
        total_taxi+=b//2
    else:
        total_taxi = total_taxi + b//2 +1

elif a==c:
    total_taxi+=a

    if b%2==0:
        total_taxi+=b//2
    else:
        total_taxi = total_taxi + b//2 +1

print(total_taxi)
    

    

    

