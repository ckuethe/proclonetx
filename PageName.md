# Introduction #
yaesu programming project

YaeProSuor  YaeProg or something

The windows programming software:
http://www.kc8unj.com/

Heian Software Engineering (Summary In English)
http://hse.dyndns.org/hiroto/RFY_LAB/vx7/e/vx7_8000.htm

Some more engineering data on it:
http://babelfish.altavista.com/urltrurl?lp=ja_en&url=http://hse.dyndns.org/hiroto/RFY_LAB/vx7/vx7_0000.htm

Basic Code Links:
http://babelfish.altavista.com/urltrurl?lp=ja_en&url=http://hse.dyndns.org/hiroto/RFY_LAB/vx7/vx7_8400.htm

In the end I want to be able to do the following for a lot (As many as possible) yaesu radios:
download setttings
edit settings
upload settings
etc

http://ubuntuforums.org/archive/index.php/t-139170.html

In linux to load the serialtousb mod:
http://www.linux-usb.org/USB-guide/x356.html

USB serial converter module: insmod usb-serial.o vendor=0xVVVV product-0xPPPP, where you need to change the VVVV and PPPP to match your device.

The serial port driver uses a major number of 188. Up to sixteen serial ports are supported. To create the appropriate device entries, use the following commands:

mknod /dev/usb/ttyUSB0 c 188 0

You should now be able to plug in a serial device into the adapter,
and use the /dev/usb/ttyUSB0 just as if it were a
normal serial port

serial port info:
http://www.linux.org/docs/ldp/howto/Serial-HOWTO-4.html

serial port communication:
19,200bps, 8bits, Stop-bit:1bit, Parity:none, XON/XOFF control:none



lsusb:

Bus 004 Device 003: ID 0403:6001 Future Technology Devices International, Ltd FT232 USB-Serial (UART) IC

Bus 004 Device 003: ID 0403:6001 Future Technology Devices International, Ltd FT232 USB-Serial (UART) IC
Device Descriptor:
> bLength                18
> bDescriptorType         1
> bcdUSB               1.10
> bDeviceClass            0 (Defined at Interface level)
> bDeviceSubClass         0
> bDeviceProtocol         0
> bMaxPacketSize0         8
> idVendor           0x0403 Future Technology Devices International, Ltd
> idProduct          0x6001 FT232 USB-Serial (UART) IC
> bcdDevice            4.00
> iManufacturer           1
> iProduct                2
> iSerial                 0
> bNumConfigurations      1
> Configuration Descriptor:
> > bLength                 9
> > bDescriptorType         2
> > wTotalLength           32
> > bNumInterfaces          1
> > bConfigurationValue     1
> > iConfiguration          0
> > bmAttributes         0x80
> > > (Bus Powered)

> > MaxPower               90mA
> > Interface Descriptor:
> > > bLength                 9
> > > bDescriptorType         4
> > > bInterfaceNumber        0
> > > bAlternateSetting       0
> > > bNumEndpoints           2
> > > bInterfaceClass       255 Vendor Specific Class
> > > bInterfaceSubClass    255 Vendor Specific Subclass
> > > bInterfaceProtocol    255 Vendor Specific Protocol
> > > iInterface              2
> > > Endpoint Descriptor:
> > > > bLength                 7
> > > > bDescriptorType         5
> > > > bEndpointAddress     0x81  EP 1 IN
> > > > bmAttributes            2
> > > > > Transfer Type            Bulk
> > > > > Synch Type               None
> > > > > Usage Type               Data

> > > > wMaxPacketSize     0x0040  1x 64 bytes
> > > > bInterval               0

> > > Endpoint Descriptor:
> > > > bLength                 7
> > > > bDescriptorType         5
> > > > bEndpointAddress     0x02  EP 2 OUT
> > > > bmAttributes            2
> > > > > Transfer Type            Bulk
> > > > > Synch Type               None
> > > > > Usage Type               Data

> > > > wMaxPacketSize     0x0040  1x 64 bytes
> > > > bInterval               0
cannot read device status, Operation not permitted (1)



possibly useful links:
http://pyvisa.sourceforge.net/
http://docs.python.org/lib/module-struct.html
http://pyserial.sourceforge.net/
http://pyvisa.sourceforge.net/pyvisa/node4.html

Good one:http://blog.makezine.com/archive/2005/05/control_the_par.html
http://mediamatrix.peavey.com/nion/resources/PythonSerial.htm

SVN:

# Non-members may check out a read-only working copy anonymously over HTTP.
svn checkout http://proclonetx.googlecode.com/svn/trunk/ proclonetx-read-only


# Project members authenticate over HTTPS to allow committing changes.
svn checkout https://proclonetx.googlecode.com/svn/trunk/ proclonetx --username 

&lt;username&gt;




--
Steps:
modprobe usbserial

aaron@coreprime:~$ lsmod | grep usbserial
usbserial              35816  1 ftdi\_sio
usbcore               145516  9 ftdi\_sio,usbserial,usblp,usb\_storage,usbhid,libusual,ehci\_hcd,uhci\_hcd

aaron@coreprime:~$ ls -l /dev/ttyUSB0
crw-rw---- 1 root dialout 188, 0 2008-02-21 23:06 /dev/ttyUSB0

add python pyserial module:
http://superb-east.dl.sourceforge.net/sourceforge/pyserial/pyserial-2.2.zip
http://sourceforge.net/projects/pyserial/


Todo:
PythonCard for GUI

how to pull the data from the device?

# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages