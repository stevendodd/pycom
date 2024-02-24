import pycom
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--on", action='store_true', help="Power On")
parser.add_argument("-f", '--off', action='store_true', help="Power Off")
parser.add_argument("-p", '--port', type=str, default='COM6', help="Serial Port")
parser.add_argument("-b", '--baud', type=int, default='115200', help="Baudrate")

args = parser.parse_args()

radio = pycom.PyCom(debug=False,port=args.port,baud=args.baud)

if args.on:
    radio.power_on()
elif args.off:
    radio.power_off()