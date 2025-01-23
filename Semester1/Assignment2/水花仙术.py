a , b = map(int,input().split())



for i in range(a,b+1):
    first = i //100
    second = (i%100)//10
    last = i%10

    sum = first**3 + second **3 + last**3

    if sum == i:
        print (i)