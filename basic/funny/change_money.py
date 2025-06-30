from functools import lru_cache

@lru_cache(maxsize=128)
def change_money(total, max_coin=5):
    """
    现有2元、3元、5元共三种面额的货币，如果需要找零99元，一共有多少种找零的方式？
    
    参数:
    total: 剩余金额
    max_coin: 当前允许使用的最大面额（避免顺序重复）

    分解为3个子问题（按硬币面额从大到小）：
        - coin=5 ：调用 change_money(5, 5) （剩余金额5，最大面额5）
        - coin=3 ：调用 change_money(7, 3) （剩余金额7，最大面额3）
        - coin=2 ：调用 change_money(8, 2) （剩余金额8，最大面额2）

    - coin=5 ：使用1个5元后，剩余金额 10-5=5 ，后续只能用 ≤5元的硬币（即5、3、2元），因此调用 change_money(5, 5) 。
    - coin=3 ：使用1个3元后，剩余金额 10-3=7 ，后续只能用 ≤3元的硬币（即3、2元），因此调用 change_money(7, 3) 。
    - coin=2 ：使用1个2元后，剩余金额 10-2=8 ，后续只能用 ≤2元的硬币（即2元），因此调用 change_money(8, 2) 。
    通过这种拆分方式，函数确保了硬币的使用顺序是 从大到小 （例如，先5元后3元，不会出现先3元后5元的重复组合），从而避免了重复计数，保证了结果的准确性。
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    
    ways = 0
    # 按面额从大到小使用，避免重复计数
    coins = [5, 3, 2]
    for coin in coins:
        # 只使用不超过当前最大面额的硬币
        if coin <= max_coin:
            ways += change_money(total - coin, coin)
    return ways

def count_ways_to_make_change(target, coins):
    """
    创建一个数组来存储每种金额的找零方式数量
    dp[i] 表示找零金额 i 的方式数量

    target=10 ， coins=[2,3,5]
    初始状态 ： dp = [1,0,0,0,0,0,0,0,0,0,0] （索引0到10）。

    假设 target=10 ， denominations=[2,3,5] ， dp 数组的更新过程如下：

    - 初始状态 ： dp = [1,0,0,0,0,0,0,0,0,0,0] （索引0到10）。
    - 处理硬币2 ：
    遍历 amount=2→10 ， dp[amount] += dp[amount-2] 。
    结果： dp[2]=1 （2元）， dp[4]=1 （2+2）， dp[6]=1 （2+2+2），依此类推，最终 dp[10]=1 （2×5）。
    - 处理硬币3 ：
    遍历 amount=3→10 ， dp[amount] += dp[amount-3] 。
    例如： dp[3] += dp[0] → dp[3]=1 （3元）； dp[5] += dp[2] → dp[5]=1 （2+3）； dp[6] += dp[3] → dp[6]=2 （2×3 或 3+3）。
    - 处理硬币5 ：
    遍历 amount=5→10 ， dp[amount] += dp[amount-5] 。
    例如： dp[5] += dp[0] → dp[5]=2 （5元 或 2+3）； dp[10] += dp[5] → dp[10]=1+2=3 （2×5 或 2+3+5 或 5×2）。

    """
    dp = [0] * (target + 1)
    dp[0] = 1  # 金额为 0 的找零方式只有一种，即不使用任何硬币

    # 遍历每种面额
    for coin in coins:
        # 更新 dp 数组
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]




if __name__ == '__main__':
    print(change_money(99, 5))

    # 定义目标金额和面额
    target_amount = 99
    coins = [2, 3, 5]
    # 计算找零方式数量
    ways = count_ways_to_make_change(target_amount, coins)
    print(f"找零 {target_amount} 元的方式数量是: {ways}")
