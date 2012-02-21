import os
import glob
import string

# first function
def getDirList():
	path=os.getenv("HOME")+"/cleaneddata"
	dirList=os.listdir(path)
	return dirList


# second function
def readFile(file):
# file=dirList(i)
	f=open(file,'r')
#	print f
	resp='False'
	for line in f :
		if 'N' in line: resp='True'
	f.close()
	return resp

# third function
def switchGender(file,line):
	if readFile(file):
		f=open(file,'r+')
		for line in f:
			if 'N' in line:
				string.replace(line,'N','M')
		f.close()




# main
dirList=getDirList()
i=1
for fname in dirList:
	if readFile(dirList[i]): switchGender(dirList[i],



