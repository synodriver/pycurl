#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import os, sys
import pycurl

# Class which holds a file reference and the read callback
class FileReader:
    def __init__(self, fp):
        self.fp = fp
    def read_callback(self, size):
        return self.fp.read(size)

# Check commandline arguments
if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <url> <file to upload>")
    raise SystemExit
url = sys.argv[1]
filename = sys.argv[2]

if not os.path.exists(filename):
    print("Error: the file '%s' does not exist" % filename)
    raise SystemExit

# Initialize pycurl
c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.UPLOAD, 1)

c.setopt(pycurl.READFUNCTION, FileReader(open(filename, 'rb')).read_callback)
# Set size of file to be uploaded.
filesize = os.path.getsize(filename)
c.setopt(pycurl.INFILESIZE, filesize)

# Start transfer
print(f'Uploading file {filename} to url {url}')
c.perform()
c.close()
