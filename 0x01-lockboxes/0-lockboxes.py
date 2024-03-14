#!/usr/bin/python3
"""
This module provides a function to determine if all lockboxes can be unlocked.

The function canUnlockAll checks if all lockboxes in a list of boxes can be opened
by recursively searching for keys in the boxes and updating a list of open boxes.

Args:
    boxes (list): A list of lists representing the lockboxes and their corresponding keys.

Returns:
    bool: True if all lockboxes can be opened, False otherwise.

Example:
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True
"""

def canUnlockAll(boxes):
    """
    Determine if all lockboxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the lockboxes and their corresponding keys.

    Returns:
        bool: True if all lockboxes can be opened, False otherwise.
    """
    if not boxes:
        return False
    box_len = len(boxes)
    open_box = [0]

    for key in open_box:
        for box in boxes[key]:
            if box not in open_box and box < box_len:
                open_box.append(box)

    if len(open_box) == box_len:
        return True
    return False

