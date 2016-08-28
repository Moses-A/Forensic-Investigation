#!/usr/bin/env python2
# written by Moses Arocha
# Created in Python, with the help of TJ O'Connor's book "Violent Python"

import os
import optparse
from _winreg import *

def IDConverter(UserID):				# Converts the users SID into readable names that the user can recongize
	try:
		key = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"+'\\'+UserID) # directs the directories to where on the local machine lays each user
		(value, type) = QueryValueEx(key, 'ProfileImagePath')
		user = value.split('\\')[-1]		# Each user is split up then is returned
		return user
	except:
		return UserID				# A catch all if a user's SID cannot be decoded, it just returns the SID

def ReturnsDirectory():
	dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']	# Then directs to each users recycle bin directories
	for RecycleBinDirectory in dirs:
		if os.path.isdir(RecycleBinDirectory):
			return RecycleBinDirectory			# Returns the directories
	return None

def findRecycled(RecycleBinDirectory):
	DirectoryListing = os.listdir(RecycleBinDirectory)
	for UserID in DirectoryListing:
		files = os.listdir(RecycleBinDirectory + UserID)	# Per user, it analyzes per directory
		user = IDConverter(UserID)				# References the IDConverter function, which converts the SID
		print '\n\t[*] Listing Recycle Bin Files For User : ' + str(user) # The output the user finally sees
		i = 0
		for file in files:					# For loop that grabs each file within each recycle bin directory per user
                        i = i + 1					# A simple incrementation that allows for easy flows
			print "[", i, "] Found File: " + str(file)

## The beginning of the main function, where it returns the directories, grabs the user's name from the SID, then finds the items inside each recycle bin ## 
def main():
	RecycledDirectory = ReturnsDirectory()
	findRecycled(RecycledDirectory)

if __name__ == '__main__':
	main()
