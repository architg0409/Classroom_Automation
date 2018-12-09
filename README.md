# Classroom Automation
* Classroom Automation using Arduino.
* Automating lights and fans of a classroom according to Timetable.
* Prerequisites : Good Knowledge of Database and Python Tkinter.
* Tkinter Module is used for GUI.


## Python Modules Used:
* Tkinter
* mysql.connector
* datetime
* pyserial

## Softwares Used:
* WampServer For Database Management.
* Arduino IDE.
* Python 3.6.4 IDLE.

## Hardwares Used:
* Arduino Mega 2560.
* Single Channel Relay Board (5V).
* Cable For Arduino UNO/MEGA (USB A to B).
* Male to Female Jumper Wires.

## Connections:
* Ground: Connect to the Arduino's GND pin.
* 5V Vcc: Connect to the Arduino’s 5V pin.
* Signal: Connect to the Arduino's digital pin (pin 7).

### Note:
* Mainfiles won't run if you haven't connected Arduino to your PC.
* You need to change the Com port in the python file according to your PC.
* There are two types of table in database, one for switching relay on or off every minute and the other one for every hour.
* If you want to run for every minute then run MainFile2 and for every hour run MainFile and change the table name in python file accordingly.



