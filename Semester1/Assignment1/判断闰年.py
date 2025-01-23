n=int(input())

if n%4!=0 or (n%100==0 and n%400!=0) or n%3200==0:
    print('N')
else:
    print('Y')