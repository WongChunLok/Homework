# 22 信科 吴明睿
# 读取输入
p = int(input())
cost = sorted(list(map(int, input().split())))

# 初始化变量
i, j, cnt = 0, len(cost) - 1, 0

# 使用双指针方法处理成本列表
while i < j:
    if cost[i] <= p:
        # 如果当前最小成本小于或等于剩余金额，则购买并更新相关变量
        cnt += 1
        p -= cost[i]
        i += 1
    elif cnt:
        # 如果剩余金额不足以支付当前最小成本且已购数量不为零，则回退最后一个购买项
        cnt -= 1
        p += cost[j]
        j -= 1
    else:
        # 如果无法再进行任何操作则退出循环
        break

# 输出最终能够购买的数量
print(cnt + (cost[i] <= p))