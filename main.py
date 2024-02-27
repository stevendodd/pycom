import pycom
import argparse

dataMods = list(pycom.ModInput_DataMod.__members__)
opMode = list(pycom.OperatingMode.__members__)
dataMode = list(pycom.DataMode.__members__)
sdMode = list(pycom.Split_DupMode.__members__)

parser = argparse.ArgumentParser()
parser.add_argument("-p", '--port', type=str, default='COM6', help="Serial Port")
parser.add_argument("-b", '--baud', type=int, choices=['4800','9600','19200','38400','57600','115200'], default='115200', help="Baudrate")
parser.add_argument("-x", "--power", choices=['on', 'off'], help="Power On/Off")
parser.add_argument("--opMode", type=str, choices=opMode, help="SET > Operating Mode")
parser.add_argument("--split", type=str, choices=sdMode, help="SET > Split/DUP")
parser.add_argument("--dataMode", type=str, choices=dataMode, help="SET > Data Mode")
parser.add_argument("--modInputDataMod", type=str, choices=dataMods, help="SET > Connectors > MOD Input > DATA MOD")
parser.add_argument('--usbModLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > MOD Input > USB MOD Level")
parser.add_argument('--usbAfOutputLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > USB AF/IF Output > AF Output Level")
args = parser.parse_args()

radio = pycom.PyCom(debug=False,port=args.port,baud=args.baud)

if args.power == 'on':
    radio.power_on()
elif args.power == 'off':
    radio.power_off()
else:
    if args.opMode:
        radio.send_operating_mode(pycom.OperatingMode[args.opMode].value)
    if args.dataMode:
        radio.send_data_mode(pycom.DataMode[args.dataMode].value)
    if args.split:
        radio.send_split_mode(pycom.Split_DupMode[args.split].value)
    if args.modInputDataMod:
        radio.send_data_mod(pycom.ModInput_DataMod[args.modInputDataMod].value)
    if args.usbAfOutputLevel:
        radio.send_af_output_level(args.usbAfOutputLevel)
    if args.usbModLevel:
        radio.send_usb_mod_level(args.usbModLevel)
   
    print("Transceiver Id: " + radio.read_transceiver_id())
    print(radio.read_power_off_setting())
    print("Operating Mode: " + ', '.join(radio.read_operating_mode()))
    print("Data Mode: " + ', '.join(radio.read_data_mode()))
    print(radio.read_split_mode())
    print(radio.read_data_mod())
    print("Connectors > USB AF/IF Output > AF Output Level: " + str(radio.read_af_output_level()) + "%")
    print("Connectors > MOD Input > USB MOD Level: " + str(radio.read_usb_mod_level()) + "%")
