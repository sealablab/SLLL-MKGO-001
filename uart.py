#!/usr/bin/env python3
import serial
import time
import sys
#// From pinata/main.c:
#// #define CMD_SWAES256_ENC 0x60
#// define CMD_SWAES256_DEC 0x61

#serial_port="/dev/tty.usbserial-FT7EWINH"
serial_port="/dev/ttyUSB0"
S = serial.Serial(serial_port, 115200, timeout=2)
plaintext = bytearray([0x61, 0x41, 0x42, 0x43, 0x44,0x61,0x62,0x63,0x64,0x51,0x52,0x53,0x54,0x71,0x72,0x73,0x74])
print(len(plaintext))
print(plaintext.decode())
S.write(plaintext)

print("About to ask pinata to encrypt: %s" % (plaintext[1:].decode()))
n = 1000000
print("Going for %d iterations in 1:" % (n))
ret=""
for i in range(1, n):
	if (i % 1000 ==0):
		print(f"#{i}")
	S.write(plaintext)
	ret=S.read(16)
print("Done")
