import serial
import os.path

i = input("enter file name: ")
if(os.path.exists(i)==False):
    f=open(i,'x')
    f.truncate(0)
    f.close()
    print("file created")
f=open(i,'w')
f.truncate(0)
f.close()
f=open(i,'w')
ser = serial.Serial(port='COM6',baudrate=9600)
while (True):
    vs = str(ser.readline())
    f.write(vs+"\n")
    f.flush()



f.close()
print("data written to file")