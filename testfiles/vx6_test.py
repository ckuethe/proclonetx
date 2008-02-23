#!/usr/bin/env python
# original code written by LA4RT Jon Kare Hellan
# from http://jk.ufisa.uninett.no/la4rt/vx-6-protocol.html
# modified by W3LOG Logan Browne

# standard libraries
import sys
import time

# non-standard libraries
# pyserial downloaded from http://pyserial.sourceforge.net/
import serial
# good python serial port opening and error handling example at 
# http://www.elifulkerson.com/projects/downloads/tsb.py.txt

### data reading process from VX 6 Commander
# open serial connection 
#   19200, 1, N, 8
#   EOF 1a, ERR 0, BRK 0, XON 11, XOFF 13
#   Shake 1, Replace 40, XONLIMIT 7500, XOFFLIMIT 7500
#   Queue size 30000
# read 10 bytes
# write 1 byte
# read 66, 65, 65, 130, 65, 260, 65 x7, 325, 65 x4, 325, 65 x6, 
#   260, 65 x7, 325, 195, 65 x3, 845, 325, 65 x4, 780, 65 x5, 
#   520, 325, 65 x3, 780, 65, 130, 65 x8, 455, 65 x4, 260, 65, 260
#   65 x7, 455, 65 x4, 455, 65 x10, 455, 65 x4, 325, 65, 130, 65 x3,
#   130, 65 x4, 325, 65 x6, 455, 65 x10, 520, 65 x3, 130, 65 x3, 195
#   65 x3, 390, 65 x5, 390, 65 x5, 520, 65 x9, 260, 65 x7, 195, 65 x2,
#   130, 65 x5, 260, 65 x7, 455, 65 x11, 195, 65 x22, 195, 65 x20, 195
#   65 x3, 195, 65 x8, 195, 65 x15, 520, 65 x3, 130, 65 x3, 130, 65 x4, 780
#   65 x5, 325, 65 x7, 260, 65 x8, 260, 52?

def ByteToHex( byteStr ):    """    Convert a byte string to it's hex string representation e.g. for output.
    posted by Simon Peverett to <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/510399>    """        # Uses list comprehension which is a fractionally faster implementation than    # the alternative, more readable, implementation below    #       #    hex = []    #    for aChar in byteStr:    #        hex.append( "%02X " % ord( aChar ) )    #    #    return ''.join( hex ).strip()            return ''.join( [ "%02X " % ord( x ) for x in byteStr ] ).strip()

def HexToByte( hexStr ):    """    Convert a string hex byte values into a byte string. The Hex Byte values may    or may not be space separated.
    posted by Simon Peverett to <http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/510399>    """    # The list comprehension implementation is fractionally slower in this case        #    #    hexStr = ''.join( hexStr.split(" ") )    #    return ''.join( ["%c" % chr( int ( hexStr[i:i+2],16 ) ) \    #                                   for i in range(0, len( hexStr ), 2) ] )     bytes = []    hexStr = ''.join( hexStr.split(" ") )    for i in range(0, len(hexStr), 2):        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )    return ''.join( bytes )
    

def checksum(bytes):
    sum = 0
    for b in bytes:
        sum = sum + ord(b)
    return sum & 0xff

def checksum_ok(s):
    cs1_addr  = 0x024a
    bl1_start = 0x01cb
    bl1_len   = 127
    cs2_addr  = 0x7f4a
    bl2_start = 0x000f
    bl2_end   = 0x7f49
    cs1_calc = checksum(s[bl1_start:bl1_start+bl1_len])
    cs2_calc = checksum(s[bl2_start:bl2_end])
    print "  checksum 1 calc value: %6x" % (cs1_calc) 
    print "  checksum 1 read value: %6x" % (ord(s[cs1_addr]))
    print "  checksum 2 calc value: %6x" % (cs2_calc)
    print "  checksum 2 read value: %6x" % (ord(s[cs2_addr]))
    return (cs1_calc == ord(s[cs1_addr]) and
             cs2_calc == ord(s[cs2_addr]))
    

ACK = chr(6)
HEADER = HexToByte("41 48 30 32 31 00 E0 01 02 01")
EOD = HexToByte("C9 FF")
h1len  = 10
blen   = 32575
b_read = blen / 25
ofname = "out.vx6"
iport  = "/dev/ttyUSB0"

try:    s = serial.Serial(iport,19200)except serial.SerialException:    print "Error opening serial port.  Is it in use?"    sys.exit(1)

print "Reading from ", s.portstr
print 'Turn HT on by pressing "ON/OFF" while pressing "FW".'
print 'Next, press "BAND" on HT.'

# loop through until we get some data
while s.inWaiting() < h1len:
    time.sleep(1)
print "reading header"
h1 = s.read (h1len)
print " header value: ", ByteToHex(h1) 

# check the header value
if (h1 != HEADER):
    print "ERROR: Wrong value in header, maybe not a VX-6?"
    sys.exit(1)
else:
    s.write (ACK)
    s.flushOutput()
    print "sent ACK"


# loop through until we get some data
while s.inWaiting() < 1:
    time.sleep(1)
print "waiting for ACK"
if s.read (1) != ACK:
    print "ERROR: didn't get an ACK, exiting."
    sys.exit(1) 
else:
    print "recieved ACK"

print "reading data block"
# Gather all input - Build a list of strings, then join it
str_list = []
looping = 1
byte_count = 0
while byte_count < blen:
    block = s.read(b_read)
    byte_count += b_read
    print("%3d percent complete" % ((byte_count*100)/blen))
    str_list.append(block)
b =''.join(str_list)

# get the end of data indicator
end = s.read (s.inWaiting())
if end != EOD:
    print "ERROR: failed to get end of data, instead got: ", ByteToHex(end)
else:
    print "got end of data indicator: ", ByteToHex(end)
    #send ack
    s.write (ACK)
    s.flushOutput()
    print "sent ACK"

# loop through until we get some data
while s.inWaiting() < 1:
    time.sleep(1)
print "waiting for ACK"
if s.read (1) != ACK:
    print "ERROR: didn't get an ACK, exiting."
    sys.exit(1) 
else:
    print "recieved ACK"

# get the second checksum
h2 = s.read (s.inWaiting())
print "second checksum: ", ByteToHex(h2)

print "closing serial port"
s.close

# write the file
out = open(ofname, "wb")
out.write (h1)
out.write (b)
out.write (end)
out.write (h2)


# compare checksums
if checksum_ok  (h1 + b + eod + h2):
    print "correct checksum"
else:
    print "wrong checksum"
