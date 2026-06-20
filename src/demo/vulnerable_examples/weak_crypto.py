import hashlib

def hash_customer_pin(pin):
    return hashlib.md5(pin.encode("utf-8")).hexdigest()

def hash_password(password):
    return hashlib.sha1(password.encode("utf-8")).hexdigest()
