#coding:utf-8
import sys
import string
reload(sys)
import requests
from lxml import etree
sys.setdefaultencoding('gb18030')

def gettext (keywords):
    url = 'https://baike.baidu.com/item/'+keywords
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = []
    li_list = tree.xpath('//div[contains(@class,"lemma-summary")]')

    for li in li_list:
        name = li.xpath('.//text() |.//b/text()')
        for name_com in name:
            name_com = [name_com.strip() for name_com in name if name_com.strip() != '']
            name_com = ' '.join(name_com)
    #print(name_com.encode('utf-8').strip())
    return(name_com.encode('utf-8').strip())
#keywords = '相对论'
#gettext(keywords)
