import pycom
import argparse

dataMods = list(pycom.ModInput_DataMod.__members__)
opMode = list(pycom.OperatingMode.__members__)
offOn = list(pycom.OffOn.__members__)
sdMode = list(pycom.Split_DupMode.__members__)

parser = argparse.ArgumentParser()
parser.add_argument("-p", '--port', type=str, default='COM6', help="Serial Port")
parser.add_argument("-b", '--baud', type=int, choices=['4800','9600','19200','38400','57600','115200'], default='115200', help="Baudrate")
parser.add_argument("-x", "--power", choices=offOn, help="Power On/Off")
parser.add_argument("--opMode", type=str, choices=opMode, help="SET > Operating Mode")
parser.add_argument("--split", type=str, choices=sdMode, help="SET > Split/DUP")
parser.add_argument("--dataMode", type=str, choices=offOn, help="SET > Data Mode")
parser.add_argument("--modInputDataMod", type=str, choices=dataMods, help="SET > Connectors > MOD Input > DATA MOD")
parser.add_argument('--usbModLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > MOD Input > USB MOD Level")
parser.add_argument('--usbAfOutputLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > USB AF/IF Output > AF Output Level")
parser.add_argument("--preamp", type=str, choices=offOn, help="Internal Preamp On/Off")
parser.add_argument("--extPreamp", type=str, choices=offOn, help="External Preamp On/Off")
parser.add_argument("--extPreamp144", type=str, choices=offOn, help="SET > Connectors > External P.AMP > 144M")
parser.add_argument("--extPreamp430", type=str, choices=offOn, help="SET > Connectors > External P.AMP > 430M")
parser.add_argument("--extPreamp1200", type=str, choices=offOn, help="SET > Connectors > External P.AMP > 1200M")

args = parser.parse_args()

radio = pycom.PyCom(debug=False,port=args.port,baud=args.baud,transceiver_id="A2")

if args.power:
    if pycom.OffOn[args.power].name == 'ON':
        radio.power_on()
    elif pycom.OffOn[args.power].name == 'OFF':
        radio.power_off()
else:
    if args.opMode:
        radio.send_operating_mode(pycom.OperatingMode[args.opMode].value)
    if args.dataMode:
        radio.send_data_mode(pycom.OffOn[args.dataMode].value)
    if args.split:
        radio.send_split_mode(pycom.Split_DupMode[args.split].value)
    if args.modInputDataMod:
        radio.send_data_mod(pycom.ModInput_DataMod[args.modInputDataMod].value)
    if args.usbAfOutputLevel:
        radio.send_af_output_level(args.usbAfOutputLevel)
    if args.usbModLevel:
        radio.send_usb_mod_level(args.usbModLevel)
    if args.extPreamp144:
        radio.send_external_preamp(144, pycom.OffOn[args.extPreamp144].value)
    if args.extPreamp430:
        radio.send_external_preamp(430, pycom.OffOn[args.extPreamp430].value)
    if args.extPreamp1200:
        radio.send_external_preamp(1200, pycom.OffOn[args.extPreamp1200].value)
    if args.preamp:
        radio.send_preamp("Internal", pycom.OffOn[args.preamp].value)
    if args.extPreamp:
        radio.send_preamp("External", pycom.OffOn[args.extPreamp].value)
    
    print("Transceiver Id: " + radio.read_transceiver_id())
    print(radio.read_power_off_setting())
    print("Operating Mode: " + ', '.join(radio.read_operating_mode()))
    print("Data Mode: " + ', '.join(radio.read_data_mode()))
    print(radio.read_split_mode())
    print(radio.read_data_mod())
    print("Connectors > USB AF/IF Output > AF Output Level: " + str(radio.read_af_output_level()) + "%")
    print("Connectors > MOD Input > USB MOD Level: " + str(radio.read_usb_mod_level()) + "%")
    print("Connectors > USB SEND/Keying > USB SEND: " + radio.read_usb_send().name)
    print(radio.read_preamp())
    print("Connectors > External P.AMP > 144M: " + radio.read_external_preamp(144).name)
    print("Connectors > External P.AMP > 430M: " + radio.read_external_preamp(430).name)
    print("Connectors > External P.AMP > 1200M: " + radio.read_external_preamp(1200).name)
   # print(radio.send_command(b'\x1a\x05\x00\x55'))
  #  print(radio.send_command(b'\x16\x5a'))
    