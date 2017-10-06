import os
import time

source = [r'F:\研3\python\backup.py', r'F:\研3\python']
target_dir = r'F:\研3\python'
today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")
comment = input("Enter a comment-->")
if len(comment) == 0:
	target = today + os.sep + now + '.rar'
else:
	target = today + os.sep + now + '_' +\
	         comment.replace(' ', '_') + '.rar'
if not os.path.exists(today):
	os.mkdir(today)
	print("Successfully created directory", today)
zip_command = "Winrar A %s %s -r"%(target, ' '.join(source))
if os.system(zip_command) == 0:
	print("Successful backup to", target)
else:
	print("backup failed")
print(target, ' '.join(source))
