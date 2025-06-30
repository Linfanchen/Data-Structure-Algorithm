
def climb_stairs(n):
    """
    假设你正在爬楼梯，每次你可以爬1级或2级台阶。你有多少种不同的方法可以爬到顶部？
    
    我们可以定义一个数组 dp，其中 dp[i] 表示到达第 i 级台阶的方法数。状态转移方程为：
    dp[i]=dp[i−1]+dp[i−2]

    这是因为到达第 i 级台阶的方法数等于到达第 i-1 级台阶的方法数（再走1级）加上到达第 i-2 级台阶的方法数（再走2级）。
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    # 初始化动态规划数组
    dp = [0] * (n + 1)
    dp[1] = 1  # 到达第1级台阶的方法数
    dp[2] = 2  # 到达第2级台阶的方法数

    # 填充动态规划数组
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs_recursive(n):
    """
    递归解法
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)



if __name__ == "__main__":
    n = 10
    print(f"[动态规划]爬 {n} 级台阶的方法数是: {climb_stairs(n)}")
    print(f"[递归]爬 {n} 级台阶的方法数是: {climb_stairs_recursive(n)}")
