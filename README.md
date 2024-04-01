# PyCOM
Python library for communicating with iCOM radios using CI-V. Modified for ic-9700

```
C:\pycom>python main.py
Transceiver Id: a2
PowerOffSetting.STANDBY_SHUTDOWN
Operating Mode: FM, FIL1
Data Mode: OFF
Split_DupMode.OFF
Satellite Mode: ON, SUB Band Selected
ModInput_DataMod.LAN
Tone.TONE
Tone Frequency: 67.0
Connectors > USB AF/IF Output > AF Output Level: 25%
Connectors > MOD Input > USB MOD Level: 60%
Connectors > USB SEND/Keying > USB SEND: USB_B_RTS
PreAmp.PAMP_ON_EXT_ON
Connectors > External P.AMP > 144M: ON
Connectors > External P.AMP > 430M: ON
Connectors > External P.AMP > 1200M: OFF
```


```
C:\pycom>python main.py -h
usage: main.py [-h] [-p PORT] [-b {4800,9600,19200,38400,57600,115200}] [-x {OFF,ON}] [--vfo {A,B}] [--split {OFF,SPLIT_ON,DUP_MINUS,DUP_PLUS}] [--satMode {OFF,ON}] [--satBand {MAIN,SUB}]
               [--opMode {LSB,USB,AM,CW,RTTY,FM,CW_R,RTTY_R,DV,DD}] [--dataMode {OFF,ON}] [--tone {OFF,TONE,TSQL,DTCS,DTCS_T,TONE_T_DTCS_R,DTCS_T_TSQL_R,TONE_T_TSQL_R}]
               [--toneFrequency {67,69.3,71.9,74.4,77,79.7,82.5,85.4,88.5,91.5,94.8,97.4,100,103.5,107.2,110.9,114.8,118.8,123,127.3,131.8,136.5,141.3,146.2,151.4,156.7,159.8,162.2,165.5,167.9,171.3,173.8,177.3,179.9,183.5,186.2,189.9,192.8,196.6,199.5,203.5,206.5,210.7,218.1,225.7,229.1,233.6,241.8,250.3,254.1}]
               [--otherVfoMode ['LSB', 'USB', 'AM', 'CW', 'RTTY', 'FM', 'CW_R', 'RTTY_R', 'DV', 'DD'] ['OFF', 'ON']] [--modInputDataMod {MIC,ACC,MIC_ACC,USB,MIC_USB,LAN}] [--usbModLevel (1..100)]
               [--usbAfOutputLevel (1..100)] [--preamp {OFF,ON}] [--extPreamp {OFF,ON}] [--extPreamp144 {OFF,ON}] [--extPreamp430 {OFF,ON}] [--extPreamp1200 {OFF,ON}]

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
  --tone {OFF,TONE,TSQL,DTCS,DTCS_T,TONE_T_DTCS_R,DTCS_T_TSQL_R,TONE_T_TSQL_R}
                        SET > Tone
  --toneFrequency {67,69.3,71.9,74.4,77,79.7,82.5,85.4,88.5,91.5,94.8,97.4,100,103.5,107.2,110.9,114.8,118.8,123,127.3,131.8,136.5,141.3,146.2,151.4,156.7,159.8,162.2,165.5,167.9,171.3,173.8,177.3,179.9,183.5,186.2,189.9,192.8,196.6,199.5,203.5,206.5,210.7,218.1,225.7,229.1,233.6,241.8,250.3,254.1}
                        SET > Tone Frequency
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