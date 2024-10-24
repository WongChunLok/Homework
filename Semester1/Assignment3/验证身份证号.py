n = int(input())
multiply=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
dict1 = {0:'1',1:'0',2:'X',3:'9',4:'8',5:'7',6:'6',7:'5',8:'4',9:'3',10:'2'}  #余数对应身份证尾号的字典


for i in range(n) :
    a = input().strip()
    list1 = []

    for j in range(17):
        list1.append(int(a[j]) * (multiply[j])) #step1
    
    total_list1 = sum(list1)   #step2

    remainder = total_list1% 11   #step3
    
    check_digit = dict1[remainder] #check the remainder,key in dict1
    
    if check_digit == a[-1].upper(): 
        print('YES')
    
    else:
        print('NO')


        

