import hashlib


def hash256(x):
    sha256 = hashlib.sha256()
    sha256.update(x.encode())
    return sha256.hexdigest()


hashlib.new('ripemd160', hashlib.sha256("mvm74FACaagz94rjWbNmW2EmhJdmEGcxpa".encode('utf-8')).digest()).hexdigest()