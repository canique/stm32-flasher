import os
import sys
import time
import serial
from YModem import YModem

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: upload.py flashfile.bin [serialDevice] [baudrate]")
        exit(1)

    binaryFile = sys.argv[1]
    serialDevice = "/dev/ttyS1"
    bdRate = 500000 # CANIQUE devices run USART @ 500 kbps

    if len(sys.argv) > 2:
        serialDevice = sys.argv[2]

    if len(sys.argv) > 3:
        bdRate = int(sys.argv[3])


    print("Using serial device {} @ speed {} bps".format(serialDevice, bdRate))


    serial_io = serial.Serial(serialDevice, baudrate=bdRate)
    #serial_io.parity = "N"
    #serial_io.bytesize = 8
    #serial_io.stopbits = 1
    #serial_io.timeout = 2

    def sender_getc(size):
        return serial_io.read(size) or None

    def sender_putc(data, timeout=15):
        return serial_io.write(data)

    sender = YModem(sender_getc, sender_putc)
    os.chdir(sys.path[0])

    serial_io.write('d'.encode()) # start download - specific command to CANIQUE devices

    file_path = os.path.abspath(binaryFile)
    sent = sender.send_file(file_path)

    print("Sent {} bytes".format(sent))
    serial_io.close()
