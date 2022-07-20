from datetime import datetime
import shutil
#import base_lib
import os




def create_automation_folder():
    now = datetime.now()
    device_name=os.popen("adb shell getprop ro.product.device").read()
    print("Took current date and time")
    dt_string = now.strftime("%d_%m_%Y_at_%H_%M_%S")
    folder_name = "Automation" + dt_string
    print("Concatenated")
    path = os.path.join("Sanity", folder_name)
    os.makedirs(path)
    print("Successful")
    return path


def create_screenshot_folder():
    screenshot_folder_name="Screenshots"
    path = os.path.join(screenshot_folder_name)
    os.makedirs(path)


def move_file(source_path,destination_path):
    shutil.move(source_path,destination_path)

