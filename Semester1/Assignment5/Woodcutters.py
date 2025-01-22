n=int(input())
s=[list(map(int,input().split()))for i in range(n)]
count=2

if n ==1:
    print(1)
    exit()

for i in range(1,len(s)-1):

    if s[i][0]-s[i-1][0]> s[i][1]: #left
        count+=1

    elif abs(s[i][0]-s[i+1][0]) > s[i][1]: #right
        count+=1
        s[i][0]+=s[i][1]
    
    else:
        continue

print(count)