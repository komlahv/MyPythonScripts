#!/usr/bin/env python

import os
import shutil

fullpath = os.path.join
start_directory = "."
Music_directory = "./Newmp3"
ON = False


def main():
    if os.path.isdir(Music_directory): #Creating directories for each type
        print "Music folder exists"
    else:
        print "Creating a new directory for Music"
        os.mkdir(Music_directory)
        print "Created"       
    for dirname, dirnames, filenames in os.walk(start_directory):
        print "Scanning" 
        for filename in filenames:
            lowcapfilename = filename.lower()
            source = fullpath(dirname, filename)
            if lowcapfilename.endswith("mp3") or lowcapfilename.endswith("mkv"):
                shutil.move(source, fullpath(Music_directory, filename))
                
            

if ON == False:
    main()
    ON = True