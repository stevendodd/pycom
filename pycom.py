from abc import ABCMeta
from typing import Tuple, Any
from enum import Enum, IntFlag
from datetime import datetime
from collections import namedtuple
from collections.abc import Callable
import serial


class OperatingMode(Enum):
    AM   = 0
    AM_N = 1

class PowerOffSetting(Enum):
    SHUTDOWN_ONLY = 0
    STANDBY_SHUTDOWN   = 1

class DataMods(Enum):
    MIC = 0
    ACC = 1
    MIC_ACC = 2
    USB = 3
    MIC_USB = 4
    LAN = 5


class PyCom:
    def __init__(self, debug: bool = False, port: str = "COM6", baud: int = 115200):
        self._ser = serial.Serial(port)
        self._ser.baudrate = baud
        self._debug = debug
        if self._debug:
            print(self._ser.name)
            print(self._ser.baudrate)

    def _send_command(self, command, data=b'', preamble=b'') -> Tuple[int, int, bytes]:

        self._ser.write(preamble + b'\xfe\xfe\xa2\xe0' + command + data + b'\xfd')

        # Our cable reads what we send, so we have to remove this from the buffer first
        self._ser.read_until(expected=b'\xfd')

        # Now we are reading replies
        reply = self._ser.read_until(expected=b'\xfd')
        return reply
        
    def _bcd_to_percentage(self,b):
        #print(b.hex())
        #print(int(b.hex())/255*100)
        return(round(int(b.hex())/255*100))
        
    def _percentage_to_bcd(self,p):
        #print(round(p/100*255))
        percentage = '00' + str(round(p/100*255))
        return(bytes([int(percentage[-3], 16),int(percentage[-2] + percentage[-1], 16)]))

    def power_on(self):
        wakeup_preamble_count = 2
        if self._ser.baudrate == 4800:
            wakeup_preamble_count = 5
        elif self._ser.baudrate == 9600:
            wakeup_preamble_count = 9
        elif self._ser.baudrate == 19200:
            wakeup_preamble_count = 20
        elif self._ser.baudrate == 38400:
            wakeup_preamble_count = 40
        elif self._ser.baudrate == 57600:
            wakeup_preamble_count = 59
        elif self._ser.baudrate == 115200:
            wakeup_preamble_count = 119

        self._send_command(b'\x18\x01', preamble=b'\xfe' * wakeup_preamble_count)


    def power_off(self):
        self._send_command(b'\x18\x00')
        
    def send_data_mod(self, data_mod: int):
        reply = self._send_command(b'\x1a\x05\x01\x16', data_mod.to_bytes())
        return(reply)
    
    def read_data_mod(self):
        reply = self._send_command(b'\x1a\x05\x01\x16')
        return(DataMods(int.from_bytes(reply[8:9])))
        
    def read_power_off_setting(self):
        reply = self._send_command(b'\x1a\x05\x01\x46')
        return(PowerOffSetting(int.from_bytes(reply[8:9])))

    def read_transceiver_id(self):
        reply = self._send_command(b'\x19\x00')
        return reply

    def read_operating_frequency(self):
        reply = self._send_command(b'\x03')
        return reply
    
    def read_operating_mode(self):
        reply = self._send_command(b'\x04')
        return reply

    def read_af_output_level(self):
        reply = self._send_command(b'\x1a\x05\x01\x06')
        #print(reply)
        #print(reply[8:-1])
        return self._bcd_to_percentage(reply[8:-1])
        
    def send_af_output_level(self,p: int):
        reply = self._send_command(b'\x1a\x05\x01\x06' + self._percentage_to_bcd(p))
        return reply
        
    def read_usb_mod_level(self):
        reply = self._send_command(b'\x1a\x05\x01\x13')
        #print(reply)
        #print(reply[8:-1])    
        return self._bcd_to_percentage(reply[8:-1])

    def send_usb_mod_level(self,p: int):
        reply = self._send_command(b'\x1a\x05\x01\x13' + self._percentage_to_bcd(p))
        return reply