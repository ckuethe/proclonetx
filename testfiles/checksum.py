#!/usr/bin/env python

def checksum(bytes):
    sum = 0
    for b in bytes:
        sum = sum + ord(b)
    return sum & 0xff

def checksum_ok(s):
    cs1_addr  = 0x024a  
    bl1_start = 0x01cb
    bl1_len   = 127     
    cs2_addr  = 0x7f4b  
    bl2_start = 0x0000	
    bl2_end   = 0x7f4a   
    cs1_calc = checksum(s[bl1_start:bl1_start+bl1_len])
    cs2_calc = checksum(s[bl2_start:bl2_end])
    print "  checksum 1 calc value: %6x" % (cs1_calc) 
    print "  checksum 1 read value: %6x" % (ord(s[cs1_addr]))
    print "  checksum 2 calc value: %6x" % (cs2_calc)
    print "  checksum 2 read value: %6x" % (ord(s[cs2_addr]))
    return (cs1_calc == ord(s[cs1_addr]) and
             cs2_calc == ord(s[cs2_addr]))
             
f=open('vx6.out', 'rb')
checksum_ok(f.read())
