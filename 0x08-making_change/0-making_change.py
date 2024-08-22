#!/usr/bin/python3
""" making_change module """


def makeChange(coins, total):
    if total <= 0:
        return 0

    minCoins = [float('inf')] * (total + 1)
    minCoins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    return minCoins[total] if minCoins[total] != float('inf') else -1
