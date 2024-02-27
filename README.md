# PyCOM
Python library for communicating with iCOM radios using CI-V. Modified for ic-9700

C:\pycom>python main.py
Transceiver Id: a2
PowerOffSetting.STANDBY_SHUTDOWN
Operating Mode: USB, FIL1
Data Mode: ON, FIL1
Split_DupMode.OFF
ModInput_DataMod.LAN
Connectors > USB AF/IF Output > AF Output Level: 25%
Connectors > MOD Input > USB MOD Level: 25%



```
C:\pycom>python main.py -h
usage: main.py [-h] [-p PORT] [-b {4800,9600,19200,38400,57600,115200}] [-x {on,off}]
               [--opMode {LSB,USB,AM,CW,RTTY,FM,CW_R,RTTY_R,DV,DD}] [--split {OFF,SPLIT_ON,DUP_MINUS,DUP_PLUS}]
               [--dataMode {OFF,ON}] [--modInputDataMod {MIC,ACC,MIC_ACC,USB,MIC_USB,LAN}] [--usbModLevel (1..100)]
               [--usbAfOutputLevel (1..100)]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial Port
  -b {4800,9600,19200,38400,57600,115200}, --baud {4800,9600,19200,38400,57600,115200}
                        Baudrate
  -x {on,off}, --power {on,off}
                        Power On/Off
  --opMode {LSB,USB,AM,CW,RTTY,FM,CW_R,RTTY_R,DV,DD}
                        SET > Operating Mode
  --split {OFF,SPLIT_ON,DUP_MINUS,DUP_PLUS}
                        SET > Split/DUP
  --dataMode {OFF,ON}   SET > Data Mode
  --modInputDataMod {MIC,ACC,MIC_ACC,USB,MIC_USB,LAN}
                        SET > Connectors > MOD Input > DATA MOD
  --usbModLevel (1..100)
                        SET > Connectors > MOD Input > USB MOD Level
  --usbAfOutputLevel (1..100)
                        SET > Connectors > USB AF/IF Output > AF Output Level
```