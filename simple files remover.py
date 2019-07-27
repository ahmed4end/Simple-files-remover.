import os, sys, time
from glob import glob 
from shutil import rmtree
from pprint import pprint
try:
	from cprint import cprint
	from pprint import pprint
except:
	print("this script will be ugly cuz you don't have the cprint&pprint libraries xD")
	def bprint(txt, *args, speed=1/99, newline=True):
		print(txt)
	cprint = bprint
	pprint = print


cprint("Enter (t) to select 'Tree mode' or continue on the current directory: ", "fow")
ans = input()
treeMode = True if ans == "t" else False
startpath, fullpaths =os.getcwd(), []
cprint("Enter extention you want to remove: ")
ex = input()
if len(ex) < 2:
	cprint("invalid extention senpai!")
	time.sleep(5)
	sys.exit()
for root, dirs, files in os.walk(startpath):
	for f in files:
		try:
			path = str(os.path.join(root, f))
			ext = str(os.path.join(root, f))[::-1].split(".")[0][::-1]
			if any([len(ext)>4, ext != ex]):continue
		except:continue
		fullpaths.append(path)
		cprint(path, "fo", speed=0.0001, newline=True)
	if not treeMode:break
if len(fullpaths) ==0:
	cprint("couldn't find this extention!")
	time.sleep(3)
	sys.exit()
cprint("press (y) if you want to proceed and remove all: ", newline=True)
ans = input()
if ans == "y":
	for p in fullpaths:
		#path = os.path.join(os.getcwd(), i)
		cprint("removing "+os.path.basename(p), speed=0.01/99, newline=True)
		os.remove(p)
