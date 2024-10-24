n  = int(input())
coin_value=list(map(int,input().split()))

if n>2:                                                       #2个以下我拿完
    coin_split = n//2 +1                                      #2个以上比他拿多一个
    
else:
    coin_split = n


biggest_coin_value=[]

for i in range(coin_split):                                   #其他情况：我拿的n个币的面值比剩下的多的话，只拿n个      
    biggest_coin_value.append(max(coin_value))                  
    coin_value.remove(max(coin_value))

    if sum(biggest_coin_value) > sum(coin_value):
        break
    else:
        continue

print(i+1)
