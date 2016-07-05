#!/usr/bin/env python2
# written by Moses Arocha
# Written with the help of TJ O'Connor in his book "Violent Python"

import urllib2
import optparse
from urlparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS

def URLImages(url):
	print '\n\n[+] Searching For Images On : ' + url +'\n'		# The output the user finally sees
	urlContent = urllib2.urlopen(url).read()			# grabs the url, opens it, then reads it
	soup = BeautifulSoup(urlContent, "lxml")			# Uses the library bs4 in its function BeautifulSoup to parse HTMl, XML files
	ImageTags = soup.findAll('img')					# Finds any extension that is related to images after parsing
	return ImageTags

def ImageChecker(ImageTag):
	try:
		print '[Attempt] Scanning Image ...'			# Attempted per image in the ImageTags list
		ImageSource = ImageTag['src']
		ImageContent = urllib2.urlopen(ImageSource).read()	# Opens up and reads the Image's Source
		ImageName = basename(urlsplit(ImageSource)[2])
		ImageFile = open(ImageName, 'wb')
		ImageFile.write(ImageContent)
		ImageFile.close()
		return ImageName
	except:
		return ''

def checkExifData(ImageName):
	try:
		exifData = {}
		ImageFile = Image.open(ImageName)			# Command that opens up the Image
		Data = ImageFile._getexif()				# Command used to extract the Metadata using ExifTools
		if Data:
			for (tag,value) in Data.items():
				decoded = TAGS.get(tag, tag)
				exifData[decoded] = value
			exifGPS = exifData['GPSInfo']			# Anaylzes the Image and checks for GPSInfo
			if exifGPS:
				print '\t[Success] ' + ImageName + ' This Image Contains GPS Data'	# If Image has GPS info, user sees this display
	except:
		pass

## The main function that grabs the users input, checks the URL, sends the information to the URLImages function, then grabs that information, downloads the image in the ImageChecker function, then sends the images information to the checkExifData function that analyzes the images for GPS Metadata#

def main():
	UserOptions = optparse.OptionParser('usage%prog -U <Target URLl>')
	UserOptions.add_option('-U', '--URL', dest='url', type='string', help='Specify URL ADDRESS')	# Grabs the users data from the specified URL
	(options, args) = UserOptions.parse_args()
	url = options.url
	if url == None:							# Catch all for parser, if URL as not been inserted, displays usages
		print parser.usage
		exit(0)
	else:
		ImageTags = URLImages(url)
		for ImageTag in ImageTags:				# Items need to be present within the list of ImageTags, or the code will not continue
			ImageName = ImageChecker(ImageTag)		# references the ImageChecker function, analyzes the images present in the ImageTags list and downloads them
			checkExifData(ImageName)			# Sends the downloaded Images to the ExifData function to check for info

if __name__ == '__main__':
	main()
