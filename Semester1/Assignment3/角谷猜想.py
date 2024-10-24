n = int(input())

while True:                              #制造loop 
    if n != 1:

        if n%2!= 0:                      #判断偶数

            print(n,end='')
            print('*3+1=',end='')
            n=n*3+1
            print(n)

        elif n%2 == 0:                    #判断奇数
            print(n,end='')
            print ('/2=',end='')
            n=n//2
            print(n)

    else :
        print('End')
        break

