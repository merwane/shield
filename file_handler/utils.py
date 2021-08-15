import datetime
import hashlib

# converts file size from bytes to a given unit
def bytesto(bytes, to, bsize=1000): 
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    return bytes / (bsize ** a[to])

def datetime_to_string(time):
    return time.strftime("%m/%d/%Y, %I:%M:%S %p")

def calculate_file_checksum(filepath):
    checksum = hashlib.md5(open(filepath, 'rb').read()).hexdigest()

    return checksum