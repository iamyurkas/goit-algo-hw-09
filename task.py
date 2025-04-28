import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        count = amount // coin  # how many coins of this denomination we can use
        if count > 0:
            result[coin] = count
            amount -= coin * count  # decrease the remaining amount
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    
    # minimum number of coins for each amount
    min_coins = [float('inf')] * (amount + 1)

    # coin used last
    last_coin = [0] * (amount + 1)

    min_coins[0] = 0

    for sub_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= sub_amount:
                if min_coins[sub_amount - coin] + 1 < min_coins[sub_amount]:
                    min_coins[sub_amount] = min_coins[sub_amount - coin] + 1
                    last_coin[sub_amount] = coin

    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

if __name__ == "__main__":
    amount = 1961
    print(f"Calculating change for amount: {amount}\n")

    # Timing greedy algorithm
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    print("Greedy algorithm result:", greedy_result)
    print(f"Greedy algorithm execution time: {greedy_time:.6f} seconds\n")

    # Timing dynamic programming algorithm
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time
    print("Dynamic programming result:", dp_result)
    print(f"Dynamic programming execution time: {dp_time:.6f} seconds")