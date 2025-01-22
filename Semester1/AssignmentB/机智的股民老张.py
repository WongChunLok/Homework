*a, = map(int, input().split())
min_price = float('inf')
max_profit = 0

for price in a:
    min_price = min(min_price, price)  # 更新最小的值
    max_profit = max(max_profit, price - min_price)  # 更新最大的利润

print(max_profit)