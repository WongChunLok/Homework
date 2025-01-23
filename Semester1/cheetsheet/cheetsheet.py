# from collection import deque
# appendleft popleft

# python 打开中端

# ----------------------------------------------------------------------------------------------
# sorted_,key=
# sorted_,reverse=true

# import bisect
# bisect.bisect_left(list,num)    return index in the list 
# bisect.bisect_right(list,num)

# bisect.insort_left(list,num)    return whole list
# bisect.insort_right(list,num)  

# ----------------------------------------------------------------------------------------------
# exit()

# enumerate

# 双指针用while loop

# abc 递归
# str1='abc'
# visited=[]
# def f(n):
#     if n ==3:
#         print(visited)
#     else:
#         for i in str1:
#             if i not in visited:
#                 visited.append(i)
#                 f(n+1)
#                 visited.remove(i)

# f(1)
# --------------------------------------------------------------

# m,n,p=map(int,input().split())
# matrix=[list(input().split()) for _ in range(m)]

# --------------------------------------------------------------

# import heapq

# list1=[2,3,7,1,8]
# heapq.heqpify(list1)    #会帮我排序list       must heapify first

# heapq.heappush(list1,10)   #会放进list 然后排序 

# heapq.heappop(list1)  #pop the smallest element
# if 他是tuple it will only compare the first element of the tuple and pop it 

# heapq.heappushpop(list1,2)  #push 2 into the list and pop the smallest element

# ---------------------------------------------------------------

# lis1=[]
# lis1=sorted(lis1,key=lambda x:x[0],reverse=True/False)

# ----------------------------------------------------------------

# zip 函数
# a = [1, 2, 3]
# b = ['a', 'b', 'c']
# zipped = list(zip(a, b))
# print(zipped) # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]

# -----------------------------------------------------------------
# import math

# math.floor(-23.11)
# output=-24

# math.ceil(25.1)
# output=26


# ---------------------
# round(list,0) 四舍五入 0 位小数