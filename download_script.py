import sys
import urllib.request as urllib
from os.path import basename

if(len(sys.argv) <= 1):
    print("Please provide at least one url to download.")
    exit()
else:
    linksToDl = sys.argv[1:]
    for i in range(len(linksToDl)):
        res = urllib.urlopen(linksToDl[i])
        with urllib.urlopen(linksToDl[i]) as dlFile:
            content = dlFile.read()
            file = open(basename(res.url), "wb")
            file.write(content)
            file.close


