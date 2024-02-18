# Greedy Algorithm: Coin Change Problem
def coin_change(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    coin_count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coin_count += 1
    if amount == 0:
        return coin_count
    else:
        return -1  # Not possible to make change

# Dynamic Programming: Fibonacci Sequence
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

# Example usage of both algorithms
if __name__ == "__main__":
    # Greedy Algorithm: Coin Change
    coins = [1, 5, 10, 25]
    amount = 43
    print(f"Minimum number of coins required to make {amount}: {coin_change(coins, amount)}")

    # Dynamic Programming: Fibonacci Sequence
    n = 10
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
