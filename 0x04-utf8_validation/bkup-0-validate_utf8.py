#!/usr/bin/python3
'''Validate encodings for UTF-8.
'''


def get_full_binary(bins):
    '''Ensures a list of binary representations is in full 8 bits.

    Args (list):
        a list of binary representations of integers.
    Returns (list): list of binaries fully represented as eight bits.
    '''
    full_bins = []
    for b in bins:
        bin_length = len(b)
        diff = 8 - bin_length
        full_bin = b
        if diff != 0:
            # pad with zeros
            full_bin = ('0' * diff) + b
        full_bins.append(full_bin)

    return full_bins


def validUTF8(data):
    '''Determines if a given data set represents a valid UTF-8 encoding.

    Args (list):
        a list of integers.

    Returns (bool): True, if data contains a valid
    ...utf8 encoding sequence; otherwise False.
    '''
    assert isinstance(data, list)
    if not data:
        # empty list
        return True
    for i in data:
        assert isinstance(i, int)

    # data is a list of at least one integer
    bins = [bin(n)[2:] for n in data]  # convert integer to binary
    full_bins = get_full_binary(bins)  # ensure 8 digits each
    print(full_bins)

    list_len = len(full_bins)
    continuation = 0
    while list_len != 0:
        # handle most significant bytes and get continuation values
        if not continuation:
            # current list item not a continuation byte
            if full_bins[0].startswith('0'):
                # a single byte; pop and go to next
                full_bins.pop(0)
                list_len -= 1
                continue
            if full_bins[0].startswith('110'):
                # two bytes marker
                continuation = 1
                full_bins.pop(0)
                list_len -= 1
                continue
            if full_bins[0].startswith('1110'):
                # three bytes
                continuation = 2
                full_bins.pop(0)
                list_len -= 1
                continue
            if full_bins[0].startswith('11110'):
                # four bytes
                continuation = 3
                full_bins.pop(0)
                list_len -= 1
                continue

        # handle continuation bytes
        if full_bins[0].startswith('10'):
            # expected continuation byte
            continuation -= 1
            full_bins.pop(0)
            list_len -= 1
        else:
            # invalid sequence
            return False

    return True
