#!/usr/bin/env python3
from pwn import xor

key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_key123 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# key2 = key1 ^ (key1_2)
key2 = xor(key1_2, key1)

# key3 = key2 ^ (key2_3)
key3 = xor(key2_3, key2)

# key1 2 3 = (key1_2) ^ key3
key123 = xor(key1_2, key3)

# flag = (key123) ^ (flag_key123)
flag = xor(flag_key123, key123)

print("Flag:")
print(flag)