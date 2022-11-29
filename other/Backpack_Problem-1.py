import numpy as np

bag_size = 5

weight = [1, 3, 4, 5]
value = [15, 20, 30, 40]
rows, cols = len(weight), bag_size + 1
dp = np.zeros([rows, cols])

# 初始化dp陣列. 
# 至少放一個物品, 所以初始化第一row都為value[0]
first_item_weight, first_item_value = weight[0], value[0]
for j in range(1, cols): 	
    if first_item_weight <= j: 
        dp[0][j] = first_item_value

# 更新dp陣列: 先遍歷物品, 再遍歷背包. 
for i in range(1, rows): # i 是 value
    cur_weight, cur_val = weight[i], value[i]
    print("cur_weight, cur_val: ", cur_weight, cur_val)
    
    for j in range(1, cols): # j 是 weight
        print("j - cur_weight: ", j - cur_weight)
        print("cur_weight: ", cur_weight)
        if cur_weight > j: # 說明背包裝不下當前物品. 
            dp[i][j] = dp[i - 1][j] # 所以不裝當前物品. 
        else: 
            # 定義dp陣列: dp[i][j] 前i個物品裡，放進容量為j的背包, 價值總和最大是多少.
            # dp[i - 1][j - weight[i]] 為背包容量為j - weight[i]的時候不放物品i的最大價值,
            # 那麼dp[i - 1][j - weight[i]] + value[i] （物品i的價值），就是背包放物品i得到的最大價值
            # j 是 weight, cur_weight 是 weight[i], j - cur_weight 是移動到最低weight的位置
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight]+ cur_val)

        print(dp)

