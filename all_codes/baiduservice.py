# coding:utf-8
from aip import AipSpeech
import json
import wave

RESPEAKER_RATE = 16000


class Baidu_Asr:
    #baidu语音识别
    def __init__(self, APP_ID, API_KEY, SECRET_KEY, FILEPATH):
        self.__app_id = APP_ID
        self.__api_key = API_KEY
        self.__secret_key = SECRET_KEY
        self.__client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)  # 创建百度用户

        self.filepath = FILEPATH  # 录音文件地址

    def get_file_content(self):
        with open(self.filepath, 'rb') as fp:
            return fp.read()

    def get_asr_result(self):
        text = self.__client.asr(self.get_file_content(), 'wav', RESPEAKER_RATE, {'dev_pid': 1537, })
        # print(text)
        if text['err_msg'] == 'success.':
            text_output = text['result'][0].encode('utf-8')  # linux使用utf-8编码
            return text_output
        else:
            return None
    #百度语音合成
    def tts_file(self,file_name):
        f = open(filename,'r')
        command = f.read()
        if len(command) != 0:
            word = command
        f.close()
        result  = self.__client.synthesis(word,'zh',1, {
            'vol': 5,'per':0,
        })
        # 合成正确返回audio.mp3，错误则返回dict 
        if not isinstance(result, dict):
            with open('audio.mp3', 'wb') as f:
                f.write(result)
            f.close()
            print("tts successful")
    
    
    def tts_word(self,word):
        result  = self.__client.synthesis(word,'zh',1, {
            'vol': 5,'per':4,
        })
        # 合成正确返回audio.mp3，错误则返回dict 
        if not isinstance(result, dict):
            with open('audio.mp3', 'wb') as f:
                f.write(result)
            f.close()
            print("tts successful")
        else:
            print("error")
