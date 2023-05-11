#!/usr/bin/python3
''' Log parser.
'''
import sys
import re


def parse_log():
    ''' Parse logs piped in from another process.
    '''
    # create dict for aggregating data
    log_tracker = {}

    CYCLE = 1
    status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    # match/search regex parts
    IP_REGEX = r'([1-9]|[1-9][0-9]|' +\
        r'(1[0-9][0-9]|2(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-5])))' +\
        r'\.([1-9]|[1-9][0-9]|' +\
        r'(1[0-9][0-9]|2(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-5])))' +\
        r'\.([1-9]|[1-9][0-9]|' +\
        r'(1[0-9][0-9]|2(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-5])))' +\
        r'\.([1-9]|[1-9][0-9]|' +\
        r'(1[0-9][0-9]|2(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-5])))'
    DATE_REGEX = r'\[.*?\]'  # lazy quantifier
    STATUS_REGEX = r'(200|301|400|401|403|404|405|500)'
    # STATUS_REGEX = r'([2-5]0[01345])'  # in the `status_codes` range
    SIZE_REGEX = r'([0-9]*)'
    # SIZE_REGEX = r'([1-9]|[1-9][0-9]|[1-9][0-9]{2}|10[0-2][0-4])'

    try:
        for log in sys.stdin:
            # print(log)
            # get a Match object, or None
            match = re.search(
                    r'^{} - {} "GET /projects/260 HTTP/1.1" {} {}$'.format(
                        IP_REGEX, DATE_REGEX, STATUS_REGEX, SIZE_REGEX), log)
            # print(match)
            if match:
                # get captured groups, in a tuple
                groups = match.groups()
                # get file size and status code, as strings
                f_size = groups[-1]
                status = groups[-2]
                # update logs
                log_tracker.update({
                    'total_size': log_tracker.get(
                        'total_size', 0) + int(f_size),
                    status: log_tracker.get(status, 0) + 1,
                    })

            # print('##########################')

            if CYCLE % 10 == 0:
                # print stats every 10 log lines
                print('File size:', log_tracker.get('total_size'))
                for status_code in status_codes:
                    if log_tracker.get(status_code):
                        # status code has been seen, and is being tracked
                        print("{}: {}".format(
                            status_code, log_tracker.get(status_code)))

            CYCLE += 1
    except KeyboardInterrupt as e:
        # CTRL + C entered
        print('File size:', log_tracker.get('total_size'))
        for status_code in status_codes:
            if log_tracker.get(status_code):
                # status code has been seen, and is being tracked
                print("{}: {}".format(
                    status_code, log_tracker.get(status_code)))
        raise e


if __name__ == '__main__':
    parse_log()
