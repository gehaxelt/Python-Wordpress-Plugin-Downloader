#!/usr/bin/env python3
import requests
import urllib.request
import os
import sys
import re
import zipfile

PLUGINLIST = "urls.txt"
DESTDIR = "./downloaded/"
DESTFILE = DESTDIR + "download.zip"
regex = re.compile(r'(https://downloads..*?zip)')
urls = open(PLUGINLIST,"r").readlines()

if not os.path.exists(DESTDIR) and not os.path.isdir(DESTDIR):
	print(DESTDIR + "is not a folder or doesn't exist.")
	sys.exit(1)

for url in urls:
	url = url.strip()
	try:
		print("Fetching download url for " + url)
		r = requests.get(url)
		content = str(r.content)
		dl_url = regex.findall(content)[0]
	except Exception as e:
		print(e)
		continue

	try:
		print("Starting download of " + dl_url)
		urllib.request.urlretrieve(dl_url, DESTFILE)
		print("Downloaded")
	except Exception as e:
		print(e)
		continue

	try:
		print("Extracting file...")
		zip = zipfile.ZipFile(DESTFILE)
		zip.extractall(path=DESTDIR)
		zip.close()
		print("Done")
	except Exception as e:
		print(e)
		continue
