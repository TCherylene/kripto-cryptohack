from pwn import xor

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

string = "crypto{"
# 7 huruf pertama di xor kan buat dapet key
key = "".join((chr(message[i] ^ ord(string[i]))) for i in range(7))

# hasil dapet key: myXORke -> myXORkey
key = "myXORkey"

# key nya di encode dulu, lalu di xor kan dengan message agar dapet flag
flag = xor(message, key.encode())

print("Flag:")
print(flag.decode())
