#!/usr/bin/env python3

Tool_Name = "ZipKrack"
Version = "1.2.0"
"""
Author: Sajjad
GitHub: https://github.com/Cyber-Anonymous
"""

from zipfile import ZipFile
import sys
import time
import argparse


parser = argparse.ArgumentParser(description="A tool for cracking passwords of encrypted ZIP files using a provided wordlist.")
parser.add_argument("-z", "--zipfile", type=str, help="Specify the ZIP file.")
parser.add_argument("-w", "--wordlist", type=str, help="Specify the password list.")
parser.add_argument("-o", "--output", default="Extract", help="Directory to extract the contents of the ZIP file if the password is found (default: Extract).")
parser.add_argument("--version", action="version", version="{} {}".format(Tool_Name, Version))

args = parser.parse_args()

def banner():

    print("""\033[1;96m
  ______       _  __               _
 |__  (_)_ __ | |/ /_ __ __ _  ___| | __
   / /| | '_ \| ' /| '__/ _` |/ __| |/ /
  / /_| | |_) | . \| | | (_| | (__|   <
 /____|_| .__/|_|\_\_|  \__,_|\___|_|\_\\
        |_|              Coded by Sajjad
\033[0m""")



if (bool(args.zipfile) == True):
	action = args.zipfile
	try:
		zip = ZipFile(action, "r")
	except Exception as error:
		print("\n\033[0;91m[ERROR] {}\033[0;0m\n".format(error))


elif (bool(args.zipfile) == False):
	banner()
	while(True):
		action=input("Zip file > ")
		if(action=="quit" or action=="exit"):
			sys.exit()
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

else:
	pass


if(bool(args.wordlist) == True):
	list = args.wordlist
	try:
		wordlist = open(list, "r", encoding="utf-8", errors="replace")

	except Exception as error:
		print("\n\033[0;91m[ERROR] {}\033[0;0m\n".format(error))

elif(bool(args.wordlist) == False):
	while(True):
		list=input("Password list > ")
		if(list=="quit" or list=="exit"):
			sys.exit()
		try:
			wordlist = open(list,"r")
			break
		except:
			if(list == ""):
				pass
			else:
				print("\n\033[0;91m[ERROR] Unable to locate the password list.\033[0;0m\n")

else:
	pass
	

	
print("\n")

condition=0
attempts = 0
start = time.time()
for password in wordlist:
	password = password.strip()
	sys.stdout.write("\r\033[K")
	sys.stdout.write("\rAttemping password: {}".format(password))
	sys.stdout.flush()
	try:
		zip.extractall(path=args.output,pwd=password.encode("utf-8"))
		print("\n\n\033[1;92mFound password: {}\033[0;0m".format(password))
		timestamp = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
		file_name = "{}.txt".format(timestamp)
		with open(file_name,"w") as pass_file:
			pass_file.write(password)
			print("\nPassword stored in {}.".format(file_name))
			
		condition+=1
		break
	except:
		pass
	attempts +=1

zip.close()
wordlist.close()

if(condition==0):
	print("\nNo valid password found.")
else:
	pass

elapsed = time.time() - start
elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed))

print("Elapsed Time: {}".format(elapsed_time))
print("Attempted a total of {} passwords.".format(attempts))