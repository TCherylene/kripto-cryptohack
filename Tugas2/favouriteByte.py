#!/usr/bin/env python3
from pwn import xor

cipher = bytearray.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
flag = ""

for num in range(256): #bruteforce dari 0 - 255
        results = [chr(n ^ num) for n in cipher]

        flag = "".join(results)

        if flag.startswith("crypto"):
            print(flag)