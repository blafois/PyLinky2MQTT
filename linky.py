import serial
import requests
import paho.mqtt.client as mqtt

BROKER_HOST = "172.16.50.30"
BROKER_TOPIC = "linky/"
BROKER_CLIENT = "linky"

def connectBroker():
    global client
    client = mqtt.Client(BROKER_CLIENT)
    client.connect(BROKER_HOST)

def disconnectBroker():
    client.disconnect()

def processline(line):
    data = line.split(' ')
    if data[0] == 'PAPP':
        postMQTTPapp(data[1])
    elif data[0] == 'HCHC':
        postMQTTHC(data[1])
    elif data[0] == 'HCHP':
        postMQTTHP(data[1])
    elif data[0] == 'PTEC':
        postMQTTPTEC(data[1])

def postMQTTPTEC(ptec):
    val = ptec[0:2]
    client.publish("linky/PeriodeEnCours",val)

def postMQTTPapp(papp):
    client.publish("linky/PAPP",papp)

def postMQTTHC(hc):
    val = int(hc) / 1000
    client.publish("linky/IdxHCreuses",val)

def postMQTTHP(hp):
    val = int(hp) / 1000
    client.publish("linky/IdxHPleines",val)

port = '/dev/LINKY'
baudrate = 1200
parity = serial.PARITY_EVEN
hardcontrol = False
bytesize = serial.SEVENBITS
ser = serial.Serial(port = port, baudrate = baudrate, parity = parity, xonxoff = hardcontrol, bytesize = bytesize)

connectBroker()

while True:
    line = ser.readline().decode()
    try:
        processline(line)
    except:
        print("oops...")

ser.close()             # close port
disconnectBroker()

