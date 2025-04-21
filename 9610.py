import pycom
import argparse
import collections


dataMods = list(pycom.ModInput_DataMod.__members__)
opMode = list(pycom.OperatingMode.__members__)
offOn = list(pycom.OffOn.__members__)
sdMode = list(pycom.Split_DupMode.__members__)
tone = list(pycom.Tone.__members__)

class ValidateOtherVfoMode(argparse.Action):
    def __call__(self, parser, args, values, option_string=None):
        _opMode, _dataMode = values
        if _opMode not in opMode:
            raise ValueError('invalid opMode {o!r}'.format(o=_opMode))
        if _dataMode not in offOn:
            raise ValueError('invalid dataMode {d!r}'.format(d=_dataMode))
        OtherVfoMode = collections.namedtuple('OtherVfoMode', 'opMode dataMode')
        setattr(args, self.dest, OtherVfoMode(_opMode, _dataMode))


parser = argparse.ArgumentParser()
parser.add_argument("-p", '--port', type=str, default='COM5', help="Serial Port")
parser.add_argument("-b", '--baud', type=int, choices=[4800,9600,19200,38400,57600,115200], default='115200', help="Baudrate")
parser.add_argument("-x", "--power", choices=offOn, help="Power On/Off")
parser.add_argument("--vfo", type=str, choices=["A","B"], help="Select VFO Mode and VFO")
parser.add_argument("--split", type=str, choices=sdMode, help="SET > Split/DUP")
parser.add_argument("--satMode", type=str, choices=offOn, help="SET > Satellite Mode")
parser.add_argument("--satBand", type=str, choices=["MAIN","SUB"], help="SET > Satellite Mode and Select Band")
parser.add_argument("--opMode", type=str, choices=opMode, help="SET > Operating Mode")
parser.add_argument("--dataMode", type=str, choices=offOn, help="SET > Data Mode")
parser.add_argument("--tone", type=str, choices=tone, help="SET > Tone")
parser.add_argument("--toneFrequency", type=float, choices=pycom.TONE_FREQUENCIES, help="SET > Tone Frequency")
parser.add_argument("--otherVfoMode", type=str, nargs=2, action=ValidateOtherVfoMode, metavar=(opMode,offOn), help="SET > Operating Mode & Data Mode for other VFO (Not MAIN/SUB). Must be used in conjunction with --vfo")
parser.add_argument("--modInputDataMod", type=str, choices=dataMods, help="SET > Connectors > MOD Input > DATA MOD")
parser.add_argument('--usbModLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > MOD Input > USB MOD Level")
parser.add_argument('--usbAfOutputLevel', type=int, choices=range(1,101), metavar='(1..100)', help="SET > Connectors > USB AF/IF Output > AF Output Level")
parser.add_argument("--preamp", type=str, choices=offOn, help="Internal Preamp On/Off")
parser.add_argument("--extPreamp", type=str, choices=offOn, help="External Preamp On/Off")
parser.add_argument("--extPreamp144", type=str, choices=offOn, help="SET > Connectors > External P.AMP > 144M")
parser.add_argument("--extPreamp430", type=str, choices=offOn, help="SET > Connectors > External P.AMP > 430M")
parser.add_argument("--extPreamp1200", type=str, choices=offOn, help="SET > Connectors > External P.AMP > 1200M")

args = parser.parse_args()

radio = pycom.PyCom(debug=False,port=args.port,baud=args.baud,transceiver_id="00")

if args.power:
    if pycom.OffOn[args.power].name == 'ON':
        radio.power_on()
    elif pycom.OffOn[args.power].name == 'OFF':
        radio.power_off()