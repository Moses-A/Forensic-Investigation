#!/usr/bin/env python2
# written by Moses Arocha
# Created in Python, with the help of TJ O'Connor's book "Violent Python"

import os
import optparse
from _winreg import *

def IDConverter(UserID):			
	try:    # Directs the directories to where on the local machine lays each user.
	    key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"+'\\'+UserID) 
		(value, type) = QueryValueEx(key, 'ProfileImagePath')
		user = value.split('\\')[-1]	# Converts the users SID into readable names that the user can recongize.
		return user
	except:
		return UserID			 	    # A catch all if a user's SID cannot be decoded, it just returns the SID.

def ReturnsDirectory():
	dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']	# Directs to each users recycle bin directories.
	for RecycleBinDirectory in dirs:
		if os.path.isdir(RecycleBinDirectory):
		    return RecycleBinDirectory			
	return None

def findRecycled(RecycleBinDirectory):
	DirectoryListing = os.listdir(RecycleBinDirectory)
	for UserID in DirectoryListing:
		files = os.listdir(RecycleBinDirectory + UserID)	# Per user, it analyzes each directory.
		user = IDConverter(UserID)			            	# References the IDConverter function, which converts the SID.
	    print '\n\t[*] Listing Recycle Bin Files For User : ' + str(user) 
		i = 0
		for file in files:				                	# For loop that grabs each file within each recycle bin directory per user.
             i = i + 1				                    	
			print "[", i, "] Found File: " + str(file)

def main():
    RecycledDirectory = ReturnsDirectory()
	findRecycled(RecycledDirectory)

if __name__ == '__main__':
    main()
