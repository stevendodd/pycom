import pycom
import argparse

dataMods = list(pycom.DataMods.__members__)

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--power", choices=['on', 'off'], help="Power On/Off")
parser.add_argument("-p", '--port', type=str, default='COM6', help="Serial Port")
parser.add_argument("-b", '--baud', type=int, choices=['4800','9600','19200','38400','57600','115200'], default='115200', help="Baudrate")
parser.add_argument("-m", "--dataMod", type=str, choices=dataMods, help="SET > Connectors > MOD Input > DATA MOD")
args = parser.parse_args()

radio = pycom.PyCom(debug=False,port=args.port,baud=args.baud)

if args.power == 'on':
    radio.power_on()
elif args.power == 'off':
    radio.power_off()
else:
    if args.dataMod:
        radio.send_data_mod(pycom.DataMods[args.dataMod].value)

    print(radio.read_power_off_setting())
    print(radio.read_data_mod())

# b'\xfe\xfe\xe0\xa2\xfa\xfd' - power off resp