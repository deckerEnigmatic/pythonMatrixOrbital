#!/usr/bin/python
import time
import smbus
import sys
import random

def find_letter(letter):
        if  letter == 'A':
		hexcode = 0x41
	if letter == 'B':
		hexcode = 0x42
	if letter == 'C':
		hexcode = 0x43
	if letter == 'D':
		hexcode = 0x44
	if letter == 'E':
		hexcode = 0x45
	if letter == 'F':
		hexcode = 0x46
	if letter == 'G':
		hexcode = 0x47
	if letter == 'H':
		hexcode = 0x48
	if letter == 'I':
		hexcode = 0x49
	if letter == 'J':
		hexcode = 0x4A
	if letter == 'K':
		hexcode = 0x4B
	if letter == 'L':
		hexcode = 0x4C
	if letter == 'M':
		hexcode = 0x4D
	if letter == 'N':
		hexcode = 0x4E
	if letter == 'O':
		hexcode = 0x4F
	if letter == 'P':
		hexcode = 0x50
	if letter == 'Q':
		hexcode = 0x51
	if letter == 'R':
		hexcode = 0X52
	if letter == 'S':
		hexcode = 0x53
	if letter == 'T':
		hexcode = 0x54
	if letter == 'U':
		hexcode = 0x55
	if letter == 'V':
		hexcode = 0x56
	if letter == 'W':
		hexcode = 0x57
	if letter == 'X':
		hexcode = 0x58
	if letter == 'Y':
		hexcode = 0x59
	if letter == 'Z':
		hexcode = 0x5A
	if letter == '[':
		hexcode = 0x5B
	if letter == '\\':
		hexcode = 0x5C
	if letter == ']':
		hexcode = 0x5D
	if letter == '^':
		hexcode = 0x5E
	if letter == '_':
		hexcode = 0x5F

	if letter == '0':
		hexcode = 0x30
	if letter == '1':
		hexcode = 0x31
	if letter == '2':
		hexcode = 0x32
	if letter == '3':
		hexcode = 0x33
	if letter == '4':
		hexcode = 0x34
	if letter == '5':
		hexcode = 0x35
	if letter == '6':
		hexcode = 0x36
	if letter == '7':
		hexcode = 0x37
	if letter == '8':
		hexcode = 0x38
	if letter == '9':
		hexcode = 0x39
	if letter == ':':
		hexcode = 0x3A
	if letter == ';':
		hexcode = 0x3B
	if letter == '<':
		hexcode = 0x3C
	if letter == '=':
		hexcode = 0x3D
	if letter == '>':
		hexcode = 0x3E
	if letter == '?':
		hexcode = 0x3F
	if letter == '@':
		hexcode = 0x40
	if letter == ' ':
		hexcode = 0x20
	if letter == '!':
		hexcode = 0x21
	if letter == '"':
		hexcode = 0x22
	if letter == '#':
		hexcode = 0x23
	if letter == '$':
		hexcode = 0x24
	if letter == '%':
		hexcode = 0x25
	if letter == '&':
		hexcode = 0x26
	if letter == '\'':
		hexcode = 0x27
	if letter == '(':
		hexcode = 0x28
	if letter == ')':
		hexcode = 0x29
	if letter == '*':
		hexcode = 0x2A
	if letter == '+':
		hexcode = 0x2B
	if letter == ',':
		hexcode = 0x2C
	if letter == '-':
		hexcode = 0x2D
	if letter == '.':
		hexcode = 0x2E
	if letter == '/':
		hexcode = 0x2F
	if letter == 'a':
		hexcode = 0x61
	if letter == 'b':
		hexcode = 0x62
	if letter == 'c':
		hexcode = 0x63
	if letter == 'd':
		hexcode = 0x64
	if letter == 'e':
		hexcode = 0x65
	if letter == 'f':
		hexcode = 0x66
	if letter == 'g':
		hexcode = 0x67
	if letter == 'h':
		hexcode = 0x68
	if letter == 'i':
		hexcode = 0x69
	if letter == 'j':
		hexcode = 0x6A
	if letter == 'k':
		hexcode = 0x6B
	if letter == 'l':
		hexcode = 0x6C
	if letter == 'm':
		hexcode = 0x6D
	if letter == 'n':
		hexcode = 0x6E
	if letter == 'o':
		hexcode = 0x6F
	if letter == 'p':
		hexcode = 0x70
	if letter == 'q':
		hexcode = 0x71
	if letter == 'r':
		hexcode = 0x72
	if letter == 's':
		hexcode = 0x73
	if letter == 't':
		hexcode = 0x74
	if letter == 'u':
		hexcode = 0x75
	if letter == 'v':
		hexcode = 0x76
	if letter == 'w':
		hexcode = 0x77
	if letter == 'x':
		hexcode = 0x78
	if letter == 'y':
		hexcode = 0x79
	if letter == 'z':
		hexcode = 0x7A
	if letter == '{':
		hexcode = 0x7B
	if letter == '|':
		hexcode = 0x7C
	if letter == '}':
		hexcode = 0x7D
	#use tilda to specify newline
	if letter == '~':
		hexcode = 0x0A
	return hexcode


def clear_display(busAddr):
	bus.write_byte_data(busAddr,0xFE,0x58)

def off_display(busAddr):
	bus.write_byte_data(busAddr,0xFE,0x46)

def on_display(busAddr):
	print "on"
	bus.write_byte_data(busAddr,0xFE,0x42)

def write_display(busAddr,wordDisp):
	for elem in wordDisp:
		time.sleep(random.randint(1,4)*.10)
		hc = (find_letter(elem))
		bus.write_byte(busAddr,hc)


