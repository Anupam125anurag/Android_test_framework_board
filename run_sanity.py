import os 
import time
import file_creation
import glob

file_creation.create_screenshot_folder()

os.system("robot tests/contacts_testcases.robot")

folder_path=file_creation.create_automation_folder()

file_creation.move_file("Screenshots",folder_path)
file_creation.move_file("report.html",folder_path)
file_creation.move_file("log.html",folder_path)
file_creation.move_file("output.xml",folder_path)

 #SEARCH_CONTACT_BY_NAME(contact_name)
