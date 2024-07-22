import matplotlib.pyplot as plt
import statistics
i = input("enter file name: ")

f=open(i, 'r')
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

plt.plot(time, temp, color='b')


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
plt.grid()
plt.show()
