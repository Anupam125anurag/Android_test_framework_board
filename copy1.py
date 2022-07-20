import shutil

original = r'/home/idm/Downloads/android-cts-10_r12-linux_x86-arm.zip'
target = r'/var/lib/jenkins/workspace/HDK_Board855_git/android-cts-10_r12-linux_x86-arm.zip'

shutil.copyfile(original, target)
