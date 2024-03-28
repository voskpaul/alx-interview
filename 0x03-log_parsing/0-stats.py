<<<<<<< HEAD
=======

>>>>>>> cd37138257ac8caac446518ae71c29bf0e61ade8
#!/usr/bin/python3
"""
This module contains a method that reads stdin line by line and
computes metrics
"""
<<<<<<< HEAD
import sys

=======
import dis
import sys


>>>>>>> cd37138257ac8caac446518ae71c29bf0e61ade8
def display_metrics(total_size, status_code):
    """
    Function that print the metrics
    """
<<<<<<< HEAD
=======

>>>>>>> cd37138257ac8caac446518ae71c29bf0e61ade8
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

<<<<<<< HEAD
if __name__ == '__main__':
    total_size = 0
    status_code = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
=======

if __name__ == '__main__':
    total_size = 0
    status_code = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
>>>>>>> cd37138257ac8caac446518ae71c29bf0e61ade8
    }

    try:
        i = 0
        for line in sys.stdin:
            args = line.split()
            if len(args) > 6:
<<<<<<< HEAD
                status = int(args[-2])
                file_size = int(args[-1])
                total_size += file_size
                if status in status_code:
                    status_code[status] += 1
                    i += 1
                    if i % 10 == 0:
                        display_metrics(total_size, status_code)
=======
                status = args[-2]
                file_size = args[-1]
                total_size += int(file_size)
                if status in status_code:
                    i += 1
                    status_code[status] += 1
                    if i % 10 == 0:
                        display_metrics(total_size, status_code)

>>>>>>> cd37138257ac8caac446518ae71c29bf0e61ade8
    except KeyboardInterrupt:
        display_metrics(total_size, status_code)
        raise
    else:
        display_metrics(total_size, status_code)

