#!/use/bin/evn python3
"""
Tool Name: ZipKrack
Author: Sajjad
GitHub: https://github.com/Cyber-Anonymous
"""

from zipfile import ZipFile
import sys
import os

argv=False
try:
	if (sys.argv[1]=="-version" or sys.argv[1]=="--version"):
		print("ZipKrack - version 1.1")
		argv=True
	else:
		pass
except:
	pass

def print_help():
	print("""
	
     zipfile          :   Specify the zip file.
     password list    :   Specify the password list.
     help             :   Show help.
     quit             :   Exit from the tool.
     --version        :   Display the version of ZipKrack.
     --help           :   Show help.
	""")


try:
	if (sys.argv[1]=="-help" or sys.argv[1]=="--help"):
		print_help()
		argv=True
	else:
		pass
except:
	pass

if (argv==True):
	sys.exit()
else:
	pass

os.system("clear")

print("""\033[1;96m


  ______       _  __               _
 |__  (_)_ __ | |/ /_ __ __ _  ___| | __
   / /| | '_ \| ' /| '__/ _` |/ __| |/ /
  / /_| | |_) | . \| | | (_| | (__|   <
 /____|_| .__/|_|\_\_|  \__,_|\___|_|\_\\
        |_|              Coded by Sajjad


\033[0;0m""")

while(True):
	exit=False
	action=input("Zip file > ")
	if(action=="quit" or action=="exit"):
		exit=True
		sys.exit()
	elif(action=="help"):
		print_help()
	else:
		pass
	try:
		zip = ZipFile(action,"r")
		break

	except:
		if(action==""):
			pass
		else:
			print("\n\033[0;91m[ERROR] Unable to locate the zip file.\033[0;0m\n")


while(True):
	list=input("Password list > ")
	if(list=="quit" or list=="exit"):
		sys.exit()
	elif(list=="help"):
		print_help()
	try:
		wordlist = open(list,"r")
		break
	except:
		if(list == ""):
			pass
		else:
			print("\n\033[0;91m[ERROR] Unable to locate the password list.\033[0;0m\n")
	

	
print("\n")

condition=0
attempts = 0
for password in wordlist:
	password = password.strip()
	sys.stdout.write("\r\033[K")
	sys.stdout.write("\r{}".format(password))
	sys.stdout.flush()
	try:
		zip.extractall(path="Extract",pwd=password.encode("utf-8"))
		print("\n\n\033[1;92mFound password: {}".format(password))
		condition+=1
		break
	except:
		pass
	attempts +=1
	
if(condition==0):
	print("\nNo valid password found.")
	print("Attempted a total of {} passwords.".format(attempts))
else:
	pass

zip.close()
wordlist.close()