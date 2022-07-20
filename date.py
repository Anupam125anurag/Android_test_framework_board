from datetime import datetime
import os
import pytz

#os.remove("/home/idm/Desktop/HDK855/cts_results.zip")

IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
d=datetime_ist.strftime('%Y.%m.%d_%H')
#print(d)
file2 = ''
for file in os.listdir("/home/idm/Desktop/HDK855/android-cts-10_r11-linux_x86-arm/android-cts/results"):
  if file.startswith(d):
    #print(file)
    file2=file
    break
              
old="/home/idm/Desktop/HDK855/android-cts-10_r11-linux_x86-arm/android-cts/results/" + file2 
print(old)

new="/home/idm/Desktop/HDK855/cts_results.zip"
os.rename(old,new)


