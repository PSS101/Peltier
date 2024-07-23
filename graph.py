import matplotlib.pyplot as plt
import statistics
import serial
import os.path
print("r-read w-write")
m = input("Enter mode:")
if (m=="r"):
    i = input("enter file name: ")
    if (os.path.exists(i) == False):
        f = open(i, 'x')
        f.truncate(0)
        f.close()
        print("file created")
    f = open(i, 'w')
    f.truncate(0)
    f.close()
    f = open(i, 'w')
    ser = serial.Serial(port='COM6', baudrate=9600)
    while (True):
        vs = str(ser.readline())
        f.write(vs + "\n")
        f.flush()

    f.close()
    print("data written to file")
else:
    i = int(input("enter no of files: "))

    for j in range(i):
        q = input("Enter file name: ")
        print("blue-b   magenta-m "
              "green-g  yellow-y "
              "red-r    black-k "
              "cyan-c   white-w ")
        c = input("Enter color: ")

        f=open(q, 'r')
        temp=[]
        time=[]
        for row in f:
            row = row[1:]
            row = row.replace("'", "")
            row = row.replace("\r", "")
            row = row.split("\n")

            row = row[0].split(" ")
            temp.append(float(row[0]))

            row[-1] = row[-1].split(":")

            row[-1][1] = row[-1][1].strip("\\r\\n")
            if len(row[-1][-1]) == 1:
                row[-1][-1] = "0" + row[-1][-1]
            if len(row[-1][0]) == 1:
                row[-1][0] = "0" + row[-1][0]
            time.append(int((row[-1][0]))*60 + int(row[-1][-1]))

        plt.plot(time, temp, color=c)
        plt.title('Peltier Casade')
        plt.xlabel('Time in sec-->')
        plt.ylabel('Temperature in \u2103-->')
        print("Highest temp: "+str(max(temp))+"\u2103")
        print("Lowest temp: "+str(min(temp))+"\u2103")
        temp = [round(x) for x in temp]
        t=0
        for x in temp:
            if x==statistics.mode(temp):
                t+=1
        s=int(t%60)
        m=int(t/60)
        print("Stable temp: "+str(statistics.mode(temp))+"\u2103"+" time: "+str(m)+"mins "+str(s)+"sec")

        f.close()
    plt.grid()
    plt.show()

