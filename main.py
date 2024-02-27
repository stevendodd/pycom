import pycom
import argparse

def render_list_as_hex(data):
    s = '[ '
    for c in data:
      s += '%02x ' % c
    s += ']'
    return s;

def convert_bcd(n,count):
    n = int(n)
    bcd = []
    for i in range(count):
      bcd.append((n % 10) | ((n//10) % 10) << 4)
      n //= 100
    return bcd

dataMods = list(pycom.DataMods.__members__)

parser = argparse.ArgumentParser()
parser.add_argument("-p", '--port', type=str, default='COM6', help="Serial Port")
parser.add_argument("-b", '--baud', type=int, choices=['4800','9600','19200','38400','57600','115200'], default='115200', help="Baudrate")
parser.add_argument("-x", "--power", choices=['on', 'off'], help="Power On/Off")
parser.add_argument("--modInputDataMod", type=str, choices=dataMods, help="SET > Connectors > MOD Input > DATA MOD")
parser.add_argument('--usbAfOutputLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > USB AF/IF Output > AF Output Level")
parser.add_argument('--usbModLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > MOD Input > USB MOD Level")
args = parser.parse_args()

radio = pycom.PyCom(debug=False,port=args.port,baud=args.baud)

if args.power == 'on':
    radio.power_on()
elif args.power == 'off':
    radio.power_off()
else:
    if args.modInputDataMod:
        radio.send_data_mod(pycom.DataMods[args.modInputDataMod].value)
    if args.usbAfOutputLevel:
        radio.send_af_output_level(args.usbAfOutputLevel)
    if args.usbModLevel:
        radio.send_usb_mod_level(args.usbModLevel)
   
   
    print(radio.read_power_off_setting())
    print(radio.read_data_mod())
    print("Connectors > USB AF/IF Output > AF Output Level: " + str(radio.read_af_output_level()) + "%")
    print("Connectors > MOD Input > USB MOD Level: " + str(radio.read_usb_mod_level()) + "%")


    
    
 