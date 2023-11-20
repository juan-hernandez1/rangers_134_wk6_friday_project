import hashlib
import time

public_key = "55b2972a0b1191e408ad488a5cc0af2d"
private_key = "00c00cd62bdc091f9ce4007aaa6fe2a31b863b91"
timestamp = str(int(time.time()))  # Current Unix timestamp

concatenated_string = private_key + public_key + timestamp
hash_value = hashlib.md5(concatenated_string.encode()).hexdigest()

print("Timestamp:", timestamp)
print("Hash Value:", hash_value)