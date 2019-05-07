# raise an exception

class myError(Exception):
    pass

# main

try:
    raise myError
    print ('no error')
except myError:
    print ('myError raised')
