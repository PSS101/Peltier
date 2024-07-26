import matplotlib.pyplot as plt
import statistics
import serial
import os.path
import numpy as np




i = int(input("enter no of files: "))
max_time=0
max_temp=0
min_temp=0
l=""
for j in range(i):
    q = input("Enter file name: ")
    l += q.strip('.txt')+" "
    print("blue-b   magenta-m "
          "green-g  yellow-y "
          "red-r    black-k "
          "cyan-c   white-w ")
    c = input("Enter color: ")

    f=open(r"C:/Users/saish/Downloads/Peltier/"+q, 'r')
    temp=[]
    time=[]
    for row in f:


        row = row.split(" ")

        temp.append(float(row[0]))

        row[-1] = row[-1].split(":")


        if len(row[-1][-1]) == 1:
            row[-1][-1] = "0" + row[-1][-1]
        if len(row[-1][0]) == 1:
            row[-1][0] = "0" + row[-1][0]
        time.append(int((row[-1][0]))*60 + int(row[-1][-1]))

    plt.plot(time, temp, color=c)
    plt.title('Peltier Casade')
    plt.xlabel('Time in sec-->')
    plt.ylabel('Temperature in \u2103-->')


    print(" ")
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
    print(" ")
    if round(max(temp))>max_temp:
        max_temp= round(max(temp))
    if round(min(temp))<min_temp:
        min_temp = round(min(temp))
    if max(time)>max_time:
        max_time = max(time)


    f.close()
if max_temp%5!=0:
    max_temp = max_temp + 5 - max_temp%5
if min_temp%5!=0:
    min_temp = min_temp + (min_temp*-1)%5 -5
plt.yticks(np.arange(min_temp,max_temp,5))
if max_time>300:
    time_int =300
else:
    time_int = 60
plt.xticks(np.arange(0,max_time,time_int))
l=l.split(" ")
plt.legend(l)
plt.grid()
plt.show()

