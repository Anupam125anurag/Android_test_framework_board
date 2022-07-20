import os
import time

mydir = "/home/idm/Desktop/HDK855"

for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".html"):
            if filename=="test_result.html":
	        file1=filepath
		print(file1)
os.system("sudo chmod -R 777 /home/idm/Desktop/HDK855")
old=file1
print(old)


new="/home/idm/Desktop/HDK855/test_result.html"
os.rename(old,new)
