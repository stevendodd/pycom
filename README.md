# PyCOM
Python library for communicating with iCOM radios using CI-V. Modified for ic-9700

```
C:\pycom>python main.py -h
usage: main.py [-h] [-p PORT] [-b {4800,9600,19200,38400,57600,115200}] [-x {on,off}]
               [--modInputDataMod {MIC,ACC,MIC_ACC,USB,MIC_USB,LAN}] [--usbAfOutputLevel (1..100)]
               [--usbModLevel (1..100)]

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial Port
  -b {4800,9600,19200,38400,57600,115200}, --baud {4800,9600,19200,38400,57600,115200}
                        Baudrate
  -x {on,off}, --power {on,off}
                        Power On/Off
  --modInputDataMod {MIC,ACC,MIC_ACC,USB,MIC_USB,LAN}
                        SET > Connectors > MOD Input > DATA MOD
  --usbAfOutputLevel (1..100)
                        SET > Connectors > USB AF/IF Output > AF Output Level
  --usbModLevel (1..100)
                        SET > Connectors > MOD Input > USB MOD Level
```