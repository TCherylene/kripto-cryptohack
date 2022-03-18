#!/usr/bin/env python3

string = "label"
integer = 13
flag = ""

for i in string:
    #string diubah ke nomor ascii nya, di xor dengan 13, diubah kembali jadi char
    flag = flag + chr(ord(i) ^ 13)

print("Here is your flag:")
print("crypto{" + str(flag) + "}")