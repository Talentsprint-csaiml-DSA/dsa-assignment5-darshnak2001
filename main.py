def min_coins(coins, target_amount):
    # Initialize a dp array with infinity (or a large number) for all amounts greater than 0
    dp = [float('inf')] * (target_amount + 1)
    dp[0] = 0  # No coins needed to make amount 0

    # Iterate through all amounts from 1 to target_amount
    for i in range(1, target_amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[target_amount] is still infinity, return -1 (meaning it's not possible)
    return dp[target_amount] if dp[target_amount] != float('inf') else -1