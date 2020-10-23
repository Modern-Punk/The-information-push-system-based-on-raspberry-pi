#coding:utf-8
import os
import pyaudio
import wave
import time
import baiduservice
import tuling_service
RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 1
RESPEAKER_WIDTH = 2
CHUNK = 1024
RECORD_SECONDS = 3
#WAVE_OUTPUT_FILENAME = "input.wav"
p=pyaudio.PyAudio()
stream=p.open(
            rate=RESPEAKER_RATE,
            format=p.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            frames_per_buffer=CHUNK
            )

def save_wave_file(filename,data):
    
    wf=wave.open(filename,'wb')
    wf.setnchannels(RESPEAKER_CHANNELS)
    wf.setsampwidth(RESPEAKER_WIDTH)
    wf.setframerate(RESPEAKER_RATE)
    wf.writeframes(b"".join(data))
    wf.close()
    
def record():
    stream.start_stream()
    print("recording")
    frames=[]
    for i in range(0,int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data=stream.read(CHUNK)
        frames.append(data)
    print("done recording")
    save_wave_file('input.wave',frames)
    stream.stop_stream()
while(True):  
	record()
	print('over')
	result_record=baiduservice.get_asr_result('/home/pi/Desktop/SRTP/input.wave')
	if result_record:
		print("我：{}".format(result_record))
		tuling_service.talk(result_record)
	else:
		print("语音输入失败")
