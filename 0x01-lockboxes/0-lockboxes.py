#!/usr/bin/python3
""" Lockboxes algorithm implementation """


def canUnlockAll(boxes):
    """ implementation of lockboxes algorithm

    Args:
        boxes (list of lists): list to check if all the boxes can be opened
    """
    if not boxes:
        return True
    nboxes = len(boxes)
    unlocked = [False] * nboxes
    unlocked[0] = True
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if 0 <= key < nboxes and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
