# coding:utf-8
import os
import pyaudio
import wave
import time


RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 1
RESPEAKER_WIDTH = 2
CHUNK_re = 1024
RECORD_SECONDS = 3
# WAVE_OUTPUT_FILENAME = "input.wav"
p = pyaudio.PyAudio()
stream_re = p.open(
    rate=RESPEAKER_RATE,
    format=p.get_format_from_width(RESPEAKER_WIDTH),
    channels=RESPEAKER_CHANNELS,
    input=True,
    frames_per_buffer=CHUNK_re
)


def save_wave_file(filename, data):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(RESPEAKER_WIDTH)
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b"".join(data))
    wf.close()


def record():
    stream_re.start_stream()
    print("录音中")
    frames = []
    for i in range(0, int(RESPEAKER_RATE / CHUNK_re * RECORD_SECONDS)):
        data = stream_re.read(CHUNK_re)
        frames.append(data)
    print("录音完成")
    save_wave_file('input.wave', frames)  # 存至当前目录
    stream_re.stop_stream()
    
def record_corr(): #为了修复界面的数据流和record的数据流冲突
    stream_re.start_stream()
    print("录音中")
    frames = []
    for i in range(0, int(RESPEAKER_RATE / CHUNK_re * 1)):
        data = stream_re.read(CHUNK_re)
        frames.append(data)
    print("录音完成")
    save_wave_file('input.wave', frames)  # 存至当前目录
    stream_re.stop_stream()

def play_audio():
    music_path = '/home/pi/Desktop/SRTP2/audio.mp3'
    os.system('mplayer %s' % music_path)

"""
def play_audio():
    wf=wave.open("input.wave",'rb')
    p = pyaudio.PyAudio()
    stream_re = p.open(
        rate=RESPEAKER_RATE,
        format=p.get_format_from_width(RESPEAKER_WIDTH),
        channels=RESPEAKER_CHANNELS,
        input=True,
        frames_per_buffer=CHUNK_re
    )
            
    data=wf.readframes(chunk)
    while len(data) > 0:
        stream_re.write(data)
        data = wf.readframes(CHUNK)
    stream_re.stop_stream()
    stream_re.close()
    p.terminate()
    
    
def play():
    wf = wave.open(r"/home/pi/Desktop/SRTP2/input.wave",'rb') # 打开audio.wav
    p = pyaudio.PyAudio()                     # 实例化pyaudio
    # 打开流
    stream = p.open( 
                     format=p.get_format_from_width(wf.getsampwidth()),
                     channels=wf.getnchannels(),
                     rate=RESPEAKER_RATE,
                     output=True)
    # 播放音频
    while True:
        data = wf.readframes(chunk)
        if data == "":break
        stream.write(data)
	
    # 释放IO
    stream.stop_stream()
    stream.close()
    p.terminate()
"""

    


