n= int(input())
dp=[None]*(n+1)

def f(n,dp):
    if dp[n] is not None:
        return dp[n]
    if n ==1:
        result= 1
    elif n== 2:
        result= 2
    else:
        result= f(n-1,dp)+f(n-2,dp)
    
    dp[n]=result
    
    return result
print(f(n,dp))