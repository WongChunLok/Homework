def is_blessed_id(A):

    squares = set()
    i = 1
    while i * i <= 10**9:
        squares.add(i * i)
        i += 1
    
    digits = list(map(int, str(A)))
    
    def dfs(idx):
        if idx == len(digits):
            return True
        
        num = 0
        for i in range(idx, len(digits)):
            num = num * 10 + digits[i]
            if num in squares:
                if dfs(i + 1):
                    return True
        return False
    
    return "Yes" if dfs(0) else "No"

A = int(input())

print(is_blessed_id(A))