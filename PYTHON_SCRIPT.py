import os 
import time

# checking for connected devices
#print("Stability test has been completed.")
#print("Android logs and Kernel log has been generated in the workspace.")

device = os.popen("adb devices").read()
print(device)

# connect to the selected device 172.0.0.1:62001
connect = os.popen("adb connect "+device).read()
#print(connect)

#sanity test

#os.system("robot tests/contacts_testcases.robot")



# gradle build apk and install apk
uninstall = os.popen("adb uninstall com.example.mytcsapp1")
os.system("./gradlew installDebug ")
time.sleep((1000*10)/1000)

#testing and collecting logcat

os.system("adb shell monkey -p com.example.mytcsapp1 -v 2000 2> Monkeylogs.txt")
time.sleep((1000*10)/1000)

#drozer - Pentesting
print("Pentesting - Drozer started")
time.sleep((1000*1)/1000)

os.system("robot tests/z_drozer.robot")
os.system("adb forward tcp:31415 tcp:31415")
os.system("drozer console connect --command 'run scanner.provider.finduris -a com.google.android.partnersetup'> drozerlog.txt")
os.system("drozer console connect -c 'run app.provider.query content://com.google.settings/partner/' >> drozerlog.txt")


print("Pentesting - Drozer completed")

os.system("robot tests/settings_testcases.robot")

#run cts - Pre certification

os.system("/home/idm/Desktop/HDK855/android-cts-10_r11-linux_x86-arm/android-cts/tools/cts-tradefed run cts -m CtsPermissionTestCases")

#echo <password> | sudo -S <cmd> 






