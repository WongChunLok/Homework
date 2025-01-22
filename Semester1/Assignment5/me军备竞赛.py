starting=int(input())
cost=sorted(list(map(int,input().split())))

left=0
right=len(cost)-1
me=0
enemy=0

while True:
    if left < right:
            if cost[0]>starting:
                left+=1

            if cost[left] > starting:
                left+=1
                enemy+=1
            else:
                me+=1
                starting-=cost[left]
                starting+=cost[right]
                right-=1
                left+=1
    else:
         break


print(me-enemy)





