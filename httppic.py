# -*- coding:utf-8 -*-
#    author    :   丁雪峰
#    time      :   2019-03-16 19:10:56
#    email     :   fengidri@yeah.net
#    version   :   1.0.1


import logging
import sys
import time
import upyun
import os

import subprocess
import config

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(level=logging.DEBUG)

def pbcopy(msg):
    process = subprocess.Popen(
            'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(msg.encode('utf-8'))

def notice(msg, title):
    cmd = 'osascript -e \'display notification "%s"  with title "%s"\''
    cmd = cmd % (msg, title)
    os.popen(cmd)


def upload(path):
    url = '/pic/%s.png' % time.time()
    res  = upyun.putfile(path, url)

    url = config.domain + url

    if res.status_code == 200:
        pbcopy(url)
        print url
        notice("upload to: %s" % url, "HTTPPic")
    else:
        notice("error %s" % res.status_code, "HTTPPic")

class MyEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.debug(event)
        upload(event.src_path)

    def catch_all_handler(self, event):
        pass

    def on_moved(self, event):
        pass

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        pass

upyun.config = config.upyun

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, config.public, recursive=False)
observer.schedule(event_handler, config.private, recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
