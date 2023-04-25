#!/usr/bin/python
''' Solving lockboxes.
'''


def canUnlockAll(boxes):
    ''' Returns True if all boxes are unlockable.

        Args:
            boxes (list): a list of lists,
            each potentially containing keys to subsequent boxes.

        Notes:
            - each box's index corresponds to its key.
    '''
    keys = set()

    counter = 0
    for box in boxes:
        if counter == 0:
            keys.update(box)
            counter += 1
            continue

        # print(keys)

        if counter not in keys:
            return False

        # ...else
        keys.update(box)
        counter += 1

    # At this point, all boxes have their key in @keys
    return True
