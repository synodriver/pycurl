#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4:et

import pycurl

c = pycurl.Curl()
c.setopt(c.URL, 'https://httpbin.org/put')

c.setopt(c.UPLOAD, 1)
with open(__file__) as file:
    c.setopt(c.READDATA, file)

    c.perform()
    c.close()
