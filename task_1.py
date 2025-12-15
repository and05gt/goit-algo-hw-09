def find_coins_greedy(amount):
    """Greedy algorithm for giving out change."""

    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            if count > 0:
                result[coin] = count
                amount = amount - (coin * count)
    
    return result

def find_min_coins(amount):
    """Dynamic programming algorithm for finding the minimum number of coins."""

    coins = [50, 25, 10, 5, 2, 1]
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    last_coin = [0] * (amount + 1)
    
    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin:
                if dp[s - coin] + 1 < dp[s]:
                    dp[s] = dp[s - coin] + 1
                    last_coin[s] = coin
    
    result = {}
    current_amount = amount
    
    if dp[amount] == float('inf'):
        return {}
        
    while current_amount > 0:
        coin = last_coin[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
        
    return result

if __name__ == '__main__':
    amount = 113
    print(f"Сума: {amount}")
    print("Greedy:", find_coins_greedy(amount))
    print("DP:    ", find_min_coins(amount))