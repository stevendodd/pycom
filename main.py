import pycom
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--power", action='store_true', help="Power On")
parser.add_argument("-o", '--off', action='store_true', help="Power Off")
args = parser.parse_args()

radio = pycom.PyCom(debug=False)

if args.power:
    radio.power_on()
elif args.off:
    radio.power_off()