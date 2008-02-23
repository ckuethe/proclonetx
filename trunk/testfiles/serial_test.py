#!/usr/bin/python 
# standard libraries
import sys
import time


import serial

def ByteToHex( byteStr ):
    return ''.join( [ "%02X " % ord( x ) for x in byteStr ] )
    
def HexToByte( hexStr ):
    bytes = []    hexStr = ''.join( hexStr.split(" ") )    for i in range(0, len(hexStr), 2):        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )    return ''.join( bytes )

ser = serial.Serial('/dev/ttyUSB0',  baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=1, xonxoff=0, rtscts=0)
print ser.portstr

ser.read(size=8)
while ser.inWaiting():
    print hex(ord(ser.read(1)))

ser.write(chr(6))

ser.read(size=10) 
while ser.inWaiting():
    print hex(ord(ser.read(1)))
 
ser.write(chr(6))

ser.read(size=16193)
while ser.inWaiting(): 
  print hex(ord(ser.read(1)))
