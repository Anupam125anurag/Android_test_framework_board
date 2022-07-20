from zipfile import ZipFile

with ZipFile('/var/lib/jenkins/workspace/HDK_Board855_git/android-cts-10_r12-linux_x86-arm.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()
