import os
for filename in os.listdir("."): #for current directory
	if filename.startswith("lxdsa"):
		os.rename(filename, filename[5:])#Skips/removes till 6th character
