import os
import time

mydir = "/var/lib/jenkins/workspace/HDK_Board855_git/"

for subdir,dirs,files in os.walk(mydir):
    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".html"):
            if filename=="test_result.html":
	        file1=filepath
		print(file1)
os.system("sudo chmod -R 777 /var/lib/jenkins/workspace/HDK_Board855_git/")
old=file1
print(old)


new="/var/lib/jenkins/workspace/HDK_Board855_git/test_result.html"
os.rename(old,new)
