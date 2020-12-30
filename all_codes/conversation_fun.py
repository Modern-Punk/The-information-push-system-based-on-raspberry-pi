# coding:utf-8
from baiduservice import Baidu_Asr
from tuling_service import Tuling_Chat
from recoder import record,play_audio

asr_client = Baidu_Asr('22783449', 'ulC5G0y6OKKUzq1qXwnceieU', 'D3wvoa3C3LaBFlf9DHlhO53C8oyX9fZa',
                       '/home/pi/Desktop/SRTP2/input.wave')
tuling_client = Tuling_Chat('020f3b022ef54789bb968c370b88718d', '630185')

while True:
    record()
    result_record = asr_client.get_asr_result()
    print("我说：{}".format(result_record))
    result_tuling = tuling_client.talk(result_record)
    print("机器人说：{}".format(result_tuling))
    asr_client.tts_word(result_tuling)
    play_audio()
