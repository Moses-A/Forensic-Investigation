#!/usr/bin/env python2
# Written by Moses Arocha
# Written with the help of TJ O'Connor in his book "Violent Python"


import urllib2
import optparse
from urlparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS


def URLImages(url):
    print '\n\n[+] Searching For Images On : ' + url +'\n'		
    urlContent = urllib2.urlopen(url).read()			# grabs the url, opens the website, then reads it.
    soup = BeautifulSoup(urlContent, "lxml")			# Uses the library bs4 in its function BeautifulSoup to parse HTMl, XML files.
    ImageTags = soup.findAll('img')				# Finds any extension that is related to images after parsing.
    return ImageTags

def ImageChecker(ImageTag):
    try: # Attempted per image in the ImageTags list
        print '[Attempt] Scanning Image ...'			
	ImageSource = ImageTag['src']
	ImageContent = urllib2.urlopen(ImageSource).read()	
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
	ImageFile = Image.open(ImageName)			
	Data = ImageFile._getexif()				# Command used to extract the Metadata using ExifTools
	if Data:
	    for (tag,value) in Data.items():
	        decoded = TAGS.get(tag, tag)
		exifData[decoded] = value
	exifGPS = exifData['GPSInfo']				# Anaylzes the Image and checks for GPSInfo
	if exifGPS:
	    print '\t[Success] ' + ImageName + ' This Image Contains GPS Data'	
    except:
        pass


def main():
    UserOptions = optparse.OptionParser('usage%prog -U <Target URLl>')
    UserOptions.add_option('-U', '--URL', dest='url', type='string', help='Specify URL ADDRESS')
    (options, args) = UserOptions.parse_args()
    url = options.url
    if url == None:						
        print parser.usage
	exit(0)
    else:
	ImageTags = URLImages(url)
	for ImageTag in ImageTags:			
	    ImageName = ImageChecker(ImageTag)			# Needs to be last, so that all error handling can occur.
	    checkExifData(ImageName)			

if __name__ == '__main__':
    main()
