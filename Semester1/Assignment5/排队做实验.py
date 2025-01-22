n = int(input())
# 读取输入并直接创建排序后的列表
t = sorted(enumerate(input().split(), 1), key=lambda x: int(x[1]))

# 提取索引，即为答案
ans = [i[0] for i in t]
print(*ans)

# 计算动态规划数组dp，并计算平均值
dp, total = [0], 0
for _, value in t[:-1]:
    total += int(value)
    dp.append(total)

# 计算平均值时去掉dp的第一个元素（它是0），然后除以n得到平均数
average = (sum(dp) - dp[0]) / n
print(f'{average:.2f}')