# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time
from mutagen.mp3 import MP3

music_path = '/home/pi/Desktop/SRTP2/audio.mp3'
mp3 = MP3(music_path)
os.system('mplayer %s' % music_path)
# 可以根据mp3时长进行休眠
#time.sleep(mp3.info.length)
