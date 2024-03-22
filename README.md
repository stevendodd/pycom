# PyCOM
Python library for communicating with iCOM radios using CI-V. Modified for ic-9700

```
C:\pycom>python main.py
Transceiver Id: a2
PowerOffSetting.STANDBY_SHUTDOWN
Selected VFO: A
Operating Mode: USB, FIL1
Data Mode: ON, FIL1
Split_DupMode.SPLIT_ON
Satellite Mode: OFF
ModInput_DataMod.USB
Connectors > USB AF/IF Output > AF Output Level: 25%
Connectors > MOD Input > USB MOD Level: 60%
Connectors > USB SEND/Keying > USB SEND: USB_B_RTS
PreAmp.PAMP_ON_EXT_OFF
Connectors > External P.AMP > 144M: OFF
Connectors > External P.AMP > 430M: OFF
Connectors > External P.AMP > 1200M: OFF
```


```
C:\pycom>python main.py -h
usage: main.py [-h] [-p PORT] [-b {4800,9600,19200,38400,57600,115200}] [-x {OFF,ON}] [--vfo {A,B}] [--split {OFF,SPLIT_ON,DUP_MINUS,DUP_PLUS}] [--satMode {OFF,ON}]
               [--satBand {MAIN,SUB}] [--opMode {LSB,USB,AM,CW,RTTY,FM,CW_R,RTTY_R,DV,DD}] [--dataMode {OFF,ON}]
               [--otherVfoMode ['LSB', 'USB', 'AM', 'CW', 'RTTY', 'FM', 'CW_R', 'RTTY_R', 'DV', 'DD'] ['OFF', 'ON']] [--modInputDataMod {MIC,ACC,MIC_ACC,USB,MIC_USB,LAN}]
               [--usbModLevel (1..100)] [--usbAfOutputLevel (1..100)] [--preamp {OFF,ON}] [--extPreamp {OFF,ON}] [--extPreamp144 {OFF,ON}] [--extPreamp430 {OFF,ON}]
               [--extPreamp1200 {OFF,ON}]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial Port
  -b {4800,9600,19200,38400,57600,115200}, --baud {4800,9600,19200,38400,57600,115200}
                        Baudrate
  -x {OFF,ON}, --power {OFF,ON}
                        Power On/Off
  --vfo {A,B}           Select VFO Mode and VFO
  --split {OFF,SPLIT_ON,DUP_MINUS,DUP_PLUS}
                        SET > Split/DUP
  --satMode {OFF,ON}    SET > Satellite Mode
  --satBand {MAIN,SUB}  SET > Satellite Mode and Select Band
  --opMode {LSB,USB,AM,CW,RTTY,FM,CW_R,RTTY_R,DV,DD}
                        SET > Operating Mode
  --dataMode {OFF,ON}   SET > Data Mode
  --otherVfoMode ['LSB', 'USB', 'AM', 'CW', 'RTTY', 'FM', 'CW_R', 'RTTY_R', 'DV', 'DD'] ['OFF', 'ON']
                        SET > Operating Mode & Data Mode for other VFO (Not MAIN/SUB). Must be used in conjunction with --vfo
  --modInputDataMod {MIC,ACC,MIC_ACC,USB,MIC_USB,LAN}
                        SET > Connectors > MOD Input > DATA MOD
  --usbModLevel (1..100)
                        SET > Connectors > MOD Input > USB MOD Level
  --usbAfOutputLevel (1..100)
                        SET > Connectors > USB AF/IF Output > AF Output Level
  --preamp {OFF,ON}     Internal Preamp On/Off
  --extPreamp {OFF,ON}  External Preamp On/Off
  --extPreamp144 {OFF,ON}
                        SET > Connectors > External P.AMP > 144M
  --extPreamp430 {OFF,ON}
                        SET > Connectors > External P.AMP > 430M
  --extPreamp1200 {OFF,ON}
                        SET > Connectors > External P.AMP > 1200M
```