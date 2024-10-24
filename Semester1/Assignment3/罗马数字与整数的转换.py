roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'] #用list index 的方式进行匹配
digit = [1000,900,500,400,100,90,50,40,10,9,5,4,1]


n = input()

if n.isdigit():
    n=int(n)
    for i in range(13):
        x = digit[i]
        if n >= x:
            for _ in range (n//x):
                print(roman[i],end='')
            n -= n // x*x
    print()

else:
    a=0
    for i in range(13):
        if i%2 == 0:
            while n and n[0] == roman[i]:
                a += digit[i]
                n=n[1: ]
        else:
            while len(n) > 1 and n[:2] == roman[i]:
                a += digit[i]
                n=n[2:]
    print(a)

        









