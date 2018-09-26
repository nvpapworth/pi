import sys
import threading

import boto3

class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
#            sys.stdout.write(
#                "\r%s --> %s bytes transferred" % (
#                    self._filename, self._seen_so_far))
#            sys.stdout.flush()
            print("%s --> %s bytes transferred" % ( self._filename, self._seen_so_far))

