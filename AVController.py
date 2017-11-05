import soundmeter
import os
import commands
def GetRms():
    while(1>0):## Real Time Monitoring
       ret=commands.getoutput("/Library/Frameworks/Python.framework/Versions/2.7/bin/soundmeter --collect --seconds 2")
       count=0
       ##Get the average RMS value
       for line in ret.splitlines():
              count=count+1
       index=0;
       for line in ret.splitlines():
              if(index==count-1):
                     rmsline=line
              index=index+1
       colon=rmsline.index(":")
       short=rmsline[colon+1:].lstrip()
       rmsvalue=int(short)
       print(rmsvalue)
       curr=int(int(commands.getoutput("osascript -e 'set ovol to output volume of (get volume settings)'"))/12.5)
       print(curr)
       ##Gradually adjusts the volume
       if(rmsvalue<=200):
           iterator(curr,1)
       elif(rmsvalue>=200 and rmsvalue<500):
           iterator(curr,2)
       elif(rmsvalue>=500 and rmsvalue<800):
           iterator(curr,3)
       elif(rmsvalue>=800 and rmsvalue<1500):
           iterator(curr,4)
       elif(rmsvalue>=1500 and rmsvalue<3000):
           iterator(curr,5)
       elif(rmsvalue>=3000 and rmsvalue<4500):
           iterator(curr,6)
       elif(rmsvalue>=4500 and rmsvalue<6000):
           iterator(curr,7)
       else:
           iterator(curr,8)

def iterator(current,target):
    while(target>current):
        current=current+ 0.5
        a = "osascript -e 'set Volume " + str(current) + "'"
        ##Mac Terminal
        os.system(a)
    while(current>target):
        current=current- 0.5
        a = "osascript -e 'set Volume " + str(current) + "'"
        os.system(a)
GetRms()
