#!/usr/bin/python3
''' Solving lockboxes.
'''


def canUnlockAll(boxes):
    ''' Returns True if all boxes are unlockable.

        Args:
            boxes (list): a list of lists,
            each potentially containing keys to subsequent boxes.

        Notes:
            You have n number of locked boxes in front of you.
            ..Each box is numbered sequentially from 0 to n - 1 and
            ..each box may contain keys to the other boxes.
            - Each box's index corresponds to its key.
            - A key with the same number as a box opens that box.
            - You can assume all keys will be positive integers.
            - There can be keys that do not have boxes.
            - The first box boxes[0] is unlocked.
            - Return True if all boxes can be opened, else return False.
    '''
    if not boxes or len(boxes) == 1:
        # Empty container, or only one box
        return True

    if not boxes[0]:
        # No keys for other boxes
        return False

    # At this point, there're at least two boxes, with the first non-empty.
    keys = boxes[0]  # initialize the keys list
    boxes_opened = {}  # dictionary, for tracking opened boxes

    boxes_opened.update({0: True})  # first box opened by default

    key_idx = 0  # will store key indices into @keys
    while True:
        box_idx = keys[key_idx]  # key index into @boxes

        if (len(boxes) > box_idx) and not boxes_opened.get(box_idx, False):
            # box_idx is a valid @boxes index, and box not opened yet

            # push the contents of current box to keys list
            keys.extend(boxes[box_idx])
            # register this box as opened
            boxes_opened.update({box_idx: True})

        # print(keys)
        # print('###############')
        # print(boxes_opened)

        # move to next key index
        key_idx += 1

        # Check if this next index is valid
        if len(keys) > key_idx:
            # valid and accessible index
            continue

        # ...else, no more keys for boxes; finalize
        if len(boxes_opened) == len(boxes):
            # All boxes opened
            return True

        # not all boxes opened
        break

    # not all boxes opened
    return False
