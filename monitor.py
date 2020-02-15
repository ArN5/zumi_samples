from zumi.zumi import Zumi
from zumi.util.screen import Screen

import numpy as np
import time
import os
import sys

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))
    
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

# Return % of CPU used by user as a character string                                
def getCPUuse():
    #http://helloraspberrypi.blogspot.com/2015/03/get-cpu-load-from-procloadavg.html
    #p = os.popen("w")
    #p = os.popen("cat /proc/loadavg")
    #usage = os.popen("awk '{print $1}' /proc/loadavg").readline(4)
    
    #usage = os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''')
    CPU_Pct=str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
    #https://stackoverflow.com/questions/9229333/how-to-get-overall-cpu-usage-e-g-57-on-linux
    
    #msg = (p.readlines())
    #return(msg)
    return CPU_Pct
           
zumi = Zumi()
zumi.MIN_I2C_DELAY = 0.01

time_end = 0

while(1):
    time_start = time.time()
    data = zumi.get_all_arduino_data()
    print(data)
    print("batt",data[6]/58)
    print("vcc",data[7]/48)
    print("ver",(data[8]/10+1))
    print(measure_temp())

    print(getCPUuse(), "%")
    #time.sleep(0.5)
    print(time.time()-time_start)
    os.system('clear')
