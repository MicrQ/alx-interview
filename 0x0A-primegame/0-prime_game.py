#!/usr/bin/python3
""" prime game """


def isWinner(x, nums):
    """ returns the winner name """
    if x <= 0:
        return None
    if x > len(nums):
        return None
    player = 0
    score = 0
    for i in range(x):
        for j in range(i + 1):
            if nums[i] % (j + 1) == 0:
                player = (player + 1) % 2
        if player == 0:
            score += 1
        else:
            score -= 1
    if score > 0:
        return "Ben"
    if score < 0:
        return "Maria"
    return None
