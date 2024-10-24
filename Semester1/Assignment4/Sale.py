n,m = map(int,input().split())
price = list(map(int,input().split()))           #输入价格
minimum=[]


for j in range(m):                                                          
    smallest=(min(price))                        #找出最小的值
    if smallest <= 0:                            #要是负数
        minimum.append(smallest) 
        price.remove(smallest)                   #取出最小的继续loop
    else:
        continue
                   


minimum = list(map(abs,minimum))                 #转成正数

print(sum(minimum))