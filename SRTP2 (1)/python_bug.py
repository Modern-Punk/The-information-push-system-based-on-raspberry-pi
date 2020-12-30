#coding:utf-8
import requests
import re

def baidusearch (keywords):
	#百度百科爬取
	try:
		url2 = 'https://baike.baidu.com/item/'+keywords
		header={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
			}
		data2 = requests.get(url=url2,headers=header).text
		
		rst = re.findall('''<meta name="description" content="(.*?)...">''',data2)
		print("百度百科搜索结果")
		print(rst[0])
		return(rst[0])
	except IndexError:
		url = 'https://www.baidu.com/s?wd='+keywords
		header={
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47"
			}
		data = requests.get(url=url,headers=header).text
		
		#patweb = '{"title":"(.*?)","url":"http'  # 检索网页源代码，提取搜索结果
		#paturl = ',"url":"(.*?)"}'>'  # 提取对应搜索结果的网址
		rsturl = re.findall('''data-tools='{"title":"(.*?)","url":"http''',data)
		rstweb = re.findall(''',"url":"(.*?)"}'>''',data)
		#print(rsturl[0])
		
		search_result=[]
		search_web=[]
		for j in range(0,len(rsturl)):
			print("search result"+str(j+1)+":"+rsturl[j])
			search_result.append(rsturl[j])
			print("search web"+str(j+1)+":"+rstweb[j])
			search_web.append(rstweb[j])
		zipped=zip(search_result,search_web)
		return zipped
		
    
    
#search("")
	
