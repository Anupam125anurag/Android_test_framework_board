import os
from matplotlib import pyplot as plt    
%matplotlib inline
os.system("robot tests/camera_testcases.robot")
os.system("adb shell dumpsys meminfo com.google.android.GoogleCamera > CAPpics1.txt")

for i in range(0,5):
    os.system("robot tests/camera_testcases.robot")
    os.system("adb shell dumpsys meminfo com.google.android.GoogleCamera >> CAPpics1.txt")
    print(i)

# to get PSS values

file=open("CAPpics.txt",'r').read().splitlines()

f=open("file2.txt" , "w")
f.close()
for elements in range(0,len(file)):
	if "TOTAL PSS:" in file[elements]:
            f=open("file2.txt" , "a")
            f.write(file[elements])
           
f.close()

with open("file2.txt", "r") as word_list:
    words = word_list.read().split(' ')
    

res=[]
for ele in words:
    if ele.strip():
        res.append(ele)
        
res1=[]
for i in res:
    if i not in res1:
        res1.append(i)

res1.remove('TOTAL')
res1.remove('PSS:')
res1.remove('RSS:')
res1.remove('SWAP')

j=0
PSS=[]
RSS=[]
Swap=[]
for i in range(0,len(res1)):
    if j<(len(res1)-2):
        PSS.append(res1[j])
        RSS.append(res1[j+1])
        Swap.append(res1[j+2])
        j=j+3
    
    


x=[]
for s in range(0,len(PSS)):
    x.append(s+1)   
        
y=list(map(int,PSS))
z=list(map(int,RSS))       
        

plt.plot(x, y, color='r', label='PSS values')
plt.plot(x, z, color='g', label='RSS values')
  
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("50 iterations")
plt.ylabel("Memory in KB")
plt.title("PSS and RSS values")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
  
# To load the display window
plt.show()
