# Fork by Petr Belousov, 2017-Jul-15
# Updated by Robert Orr, 2016-Mar-14 - apparently the IA api changed!

# Original code from :
# Robin Camille Davis
# March 24, 2014
# downloads all items in a given Internet Archive collection
# !! will probably crash after 10 or so items !! feel free to edit the script to make it better for bigger collections
# See
# http://programminghistorian.org/lessons/data-mining-the-internet-archive
# for more detailed info
import os
import time
import internetarchive as ia
from internetarchive.session import ArchiveSession
from internetarchive.search import Search
from internetarchive import download, configure

configure()  # interactive login, for automateed scripting use configure('login@email.com', 'password')

s = ArchiveSession()

pattern=None #change this to download only selected filetypes, e.g.: pattern='*mobi' will download only Kindle formatted e-books

# fill this in -- searches for the ID of a collection in IA
coll = ia.Search(s, 'collection:xxxxxxxx')
# example of collection page: https://archive.org/details/johnjaycollegeofcriminaljustice
# the collection ID for that page is johnjaycollegeofcriminaljustice
# you can tell a page is a collection if it has a 'Spotlight Item' on the left

num = 0

for result in coll:  # for all items in a collection
    num = num + 1  # item count
    itemid = result['identifier']
    print 'Downloading: #' + str(num) + '\t' + itemid
    try:
        download(itemid, ignore_existing=True, glob_pattern=pattern)
        print '\t\t Download success.'
    except Exception, e:
        print "Error Occurred downloading () = {}".format(itemid, e)
    print 'Pausing for 40 minutes'
    # IA restricts the number of things you can download. Be nice to
    time.sleep(2400)
    # their servers -- limit how much you download, too. For me, this
    # time restriction is still not polite enough, and my connection gets
    # cut off all the dang time.
