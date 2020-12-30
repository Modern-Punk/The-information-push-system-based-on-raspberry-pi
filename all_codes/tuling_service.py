# coding:utf-8
import urllib
import requests
import json


class Tuling_Chat:
    def __init__(self, APIKEY, USERID):
        self.api = 'http://openapi.tuling123.com/openapi/api/v2'
        self.__apikey = APIKEY
        self.__userid = USERID

    def talk(self, text):
        data = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": text
                },
                "inputImage": {
                    "burl": "imageUrl"
                },
                "selfInfo": {
                    "location": {
                        "city": "深圳",
                        "province": "广东",
                        "street": "福田路"
                    }
                }
            },
            "userInfo": {
                "apiKey": self.__apikey,
                "userId": self.__userid
            }
        }
        jsondata = json.dumps(data)
        response = requests.post(self.api, data=jsondata)
        robot_res = json.loads(response.content)
        text_output = robot_res["results"][0]['values']['text'].encode('utf-8')
        return text_output
