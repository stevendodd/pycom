from abc import ABCMeta
from typing import Tuple, Any
from enum import Enum, IntFlag
from datetime import datetime
from collections import namedtuple
from collections.abc import Callable
import serial


class PreAmp(Enum):
    PAMP_OFF_EXT_OFF = 0
    PAMP_ON_EXT_OFF = 1
    PAMP_OFF_EXT_ON = 2
    PAMP_ON_EXT_ON = 3

class USB_Send(Enum):
    OFF = 0
    USB_A_DTR = 1
    USB_A_RTS = 2
    USB_B_DTR = 3
    USB_B_RTS = 4

class Split_DupMode(Enum):
    OFF = 0
    SPLIT_ON = 1
    DUP_MINUS = 17
    DUP_PLUS = 18

class OffOn(Enum):
    OFF = 0
    ON = 1
    
class OperatingMode(Enum):
    LSB = 0
    USB = 1
    AM = 2
    CW = 3
    RTTY = 4
    FM = 5
    CW_R = 7
    RTTY_R = 8
    DV = 17
    DD = 22

class Filter(Enum):
    FIL1 = 1
    FIL2 = 2
    FIL3 = 3

class PowerOffSetting(Enum):
    SHUTDOWN_ONLY = 0
    STANDBY_SHUTDOWN   = 1

class ModInput_DataMod(Enum):
    MIC = 0
    ACC = 1
    MIC_ACC = 2
    USB = 3
    MIC_USB = 4
    LAN = 5


class PyCom:

    def __init__(self, debug: bool = False, port: str = "COM6", baud: int = 115200, transceiver_id: str = "A2"):
        self._ser = serial.Serial(port)
        self._ser.baudrate = baud
        self._transceiver_id = int(transceiver_id, 16).to_bytes()

        self._debug = debug
        if self._debug:
            print(self._ser.name)
            print(self._ser.baudrate)

    def _send_command(self, command, data=b'', preamble=b'') -> Tuple[int, int, bytes]:

        self._ser.write(preamble + b'\xfe\xfe' + self._transceiver_id + b'\xe0' + command + data + b'\xfd')

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
        return(ModInput_DataMod(int.from_bytes(reply[8:9])))
        
    def read_power_off_setting(self):
        reply = self._send_command(b'\x1a\x05\x01\x46')
        return(PowerOffSetting(int.from_bytes(reply[8:9])))
        
    def read_usb_send(self):
        reply = self._send_command(b'\x1a\x05\x01\x20')
        return(USB_Send(int.from_bytes(reply[8:9])))

    def send_command(self, b):
        reply = self._send_command(b)
        return reply

    def read_transceiver_id(self):
        reply = self._send_command(b'\x19\x00')
        return reply[6:-1].hex()

    def send_data_mode(self, data_mode: int):
        reply = self._send_command(b'\x1a\x06', data_mode.to_bytes())
        return(reply)

    def read_data_mode(self):
        reply = self._send_command(b'\x1a\x06')
        if OffOn(int.from_bytes(reply[6:7])).name == "OFF":
            return(OffOn(int.from_bytes(reply[6:7])).name,)
        else:
            return(OffOn(int.from_bytes(reply[6:7])).name,Filter(int.from_bytes(reply[7:8])).name)

    def send_otherVfoMode(self, op_mode: int, data_mode: int):
        #print(b''.join([op_mode.to_bytes(),data_mode.to_bytes()]))
        reply = self._send_command(b'\x26\x01', b''.join([op_mode.to_bytes(),data_mode.to_bytes()]))
        return(reply)

    def send_vfo(self, vfo: str):
        reply = None
        if vfo == "A":
            reply = self._send_command(b'\x07\x00')
        else:
            reply = self._send_command(b'\x07\x01')
        return(reply)

    def send_satellite_band(self, band: str):
        reply = None
        if band == "MAIN":
            reply = self._send_command(b'\x07\xd2\x00')
        else:
            reply = self._send_command(b'\x07\xd2\x01')
        return(reply)
    
    def send_satellite_mode(self, sat_mode: int):
        reply = self._send_command(b'\x16\x5a', sat_mode.to_bytes())
        return(reply)

    def read_satellite_mode(self):
        reply = self._send_command(b'\x16\x5a')
        if OffOn(int.from_bytes(reply[6:7])).name == "OFF":
            return(OffOn(int.from_bytes(reply[6:7])).name,)
        else:
            reply = self._send_command(b'\x07\xd2')
            if int.from_bytes(reply[6:7]):
                return("ON","SUB Band Selected")
            else:
                return("ON","MAIN Band Selected")
        
    def send_split_mode(self, split_mode: int):
        reply = self._send_command(b'\x0f', split_mode.to_bytes())
        if split_mode == 0:
            # Also turn off DUP
            reply = self._send_command(b'\x0f', int(16).to_bytes())
        return(reply)

    def read_split_mode(self):
        reply = self._send_command(b'\x0f')
        return(Split_DupMode(int.from_bytes(reply[5:6])))

    def send_operating_mode(self, opMode: int):
        reply = self._send_command(b'\x06', opMode.to_bytes())
        return(reply)
    
    def read_operating_mode(self):
        reply = self._send_command(b'\x04')
        return(OperatingMode(int.from_bytes(reply[5:6])).name,Filter(int.from_bytes(reply[6:7])).name)

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
       
    def read_operating_frequency(self):
        reply = self._send_command(b'\x03')
        return reply

    def read_preamp(self):         
        reply = self._send_command(b'\x16\x02')
        return(PreAmp(int.from_bytes(reply[6:7])))
        
    def send_preamp(self, preamp: str, status: int):
        reply = None
        
        cur = self.read_preamp()
        internal = external = "Off"
        if cur == PreAmp.PAMP_ON_EXT_OFF or cur == PreAmp.PAMP_ON_EXT_ON:
            internal = "On"
        if cur == PreAmp.PAMP_ON_EXT_ON or cur == PreAmp.PAMP_OFF_EXT_ON:
            external = "On"
            
        if status == 0:
            if preamp == "Internal":
                if external == "Off":
                    #print(PreAmp.PAMP_OFF_EXT_OFF)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_OFF_EXT_OFF.value.to_bytes())
                elif external == "On":
                    #print(PreAmp.PAMP_OFF_EXT_ON)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_OFF_EXT_ON.value.to_bytes())
            elif preamp == "External":
                if internal == "Off":
                    #print(PreAmp.PAMP_OFF_EXT_OFF)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_OFF_EXT_OFF.value.to_bytes())
                elif internal == "On":
                    #print(PreAmp.PAMP_ON_EXT_OFF)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_ON_EXT_OFF.value.to_bytes())
        elif status == 1:
            if preamp == "Internal":
                if external == "Off":
                    #print(PreAmp.PAMP_ON_EXT_OFF)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_ON_EXT_OFF.value.to_bytes())
                elif external == "On":
                    #print(PreAmp.PAMP_ON_EXT_ON)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_ON_EXT_ON.value.to_bytes())
            elif preamp == "External":
                if internal == "Off":
                    #print(PreAmp.PAMP_OFF_EXT_ON)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_OFF_EXT_ON.value.to_bytes())
                elif internal == "On":
                    #print(PreAmp.PAMP_ON_EXT_ON)
                    reply = self._send_command(b'\x16\x02' + PreAmp.PAMP_ON_EXT_ON.value.to_bytes())
        return(reply)

    def _get_preamp_band_command(self, band: int):
        com = None
        if band == 144:
            com = b'\x1a\x05\x00\x93'
        elif band == 430:
            com = b'\x1a\x05\x00\x94'
        elif band == 1200:
            com = b'\x1a\x05\x00\x95'
        else:
            print("Invalid preamp band")
            exit(1)            
        return(com)
        
    def read_external_preamp(self, band: int):         
        reply = self._send_command(self._get_preamp_band_command(band))
        return(OffOn(int.from_bytes(reply[8:9])))
        
    def send_external_preamp(self, band: int, preamp: int):
        reply = self._send_command(self._get_preamp_band_command(band), preamp.to_bytes())
        return(reply)