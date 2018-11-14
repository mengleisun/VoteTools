## python script to vote ##
## reference: https://zhuanlan.zhihu.com/p/30047672 ##

import requests
import json
import time
import re
from random import randint

if __name__ == '__main__':
	print('感谢支持拢龙')
	proxies_list = [{'http':'http://118.190.95.35:9001'},
			{'http':'http://121.31.195.60:8123'},
 			{'http':'http://118.190.95.35:9001'},
 			{'http':'http://61.138.33.20:808'}, 
 			{'http':'http://119.3.20.128:80'}, 
			{'http':'http://182.241.226.25:43584'},
			{'http':'http://27.17.45.90:43411'},
			{'http':'http://113.108.242.36:47713'},
			{'http':'http://218.249.45.162:35586'},
			{'http':'http://58.45.194.188:9000'},
			{'http':'http://119.31.210.170:7777'},
			{'http':'http://36.110.14.186:3128'},
			{'http':'http://218.60.8.98:3129'},
			{'http':'http://120.92.74.237:3128'},
			{'http':'http://218.60.8.99:3129'},
			{'http':'http://113.200.56.13:8010'},
			{'http':'http://120.92.74.189:3128'},
			{'http':'http://114.116.10.21:3128'},
			{'http':'http://119.1.97.193:60916'},
			{'http':'http://183.129.207.73:14823'},
			{'http':'http://140.207.50.246:51426'},
			{'http':'http://59.110.240.249:8080'},
			{'http':'http://117.85.82.158:53128'},
			{'http':'http://171.37.165.77:8123'},
			{'http':'http://120.92.22.253:3128'},
			{'http':'http://171.221.239.11:808'},
			{'http':'http://203.86.26.9:3128'},
			{'http':'http://180.76.111.69:3128'},
			{'http':'http://183.129.244.17:10010'},
			{'http':'http://61.128.208.94:3128'},
			{'http':'http://123.138.89.133:9999'},
			{'http':'http://36.48.73.16:80'},
			{'http':'http://58.251.234.126:9797'},
			{'http':'http://124.152.32.140:53281'},
			{'http':'http://58.251.232.198:9797'},
			{'http':'http://123.185.5.231:8118'},
			{'http':'http://222.186.45.17:65309'},
			{'http':'http://61.187.206.207:46693'},
			{'http':'http://58.62.238.150:32431'},
			{'http':'http://119.3.20.128:80'},
			{'http':'http://121.225.24.52:3128'},
			{'http':'http://219.234.181.194'},
			{'http':'http://222.52.142.246:8080'},
			{'http':'http://203.130.46.108:9090'},
			{'http':'http://111.198.77.169:52915'},
			{'http':'http://114.84.126.36:53281'},
			{'http':'http://106.86.208.98:41683'},
			{'http':'http://183.30.204.165:9999'},
			{'http':'http://119.254.94.105:58999'},
			{'http':'http://121.63.208.119:53281'},
			{'http':'http://182.138.232.114'},
			{'http':'http://116.62.134.173:9999'},
			{'http':'http://203.93.125.238:51108'},
			{'http':'http://113.57.97.63:808'},
			{'http':'http://36.110.234.244:80'}]

	ipid = randint(0, 50)
	proxy_choise = proxies_list[ipid]	
	headers = {
		'Accept':"*/*",
		'Accept-Encoding':"gzip, deflate",
		'Accept-Language':"en-US,en;q=0.5",
		'Connection':"keep-alive",
		'Content-Length':"14",
		'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",
		'Host':"changemakerchina.org",
		'Referer':"http://changemakerchina.org/home/index/zhanshi_d/id/181.html",
		'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
		'X-Requested-With':"XMLHttpRequest"
	}

	url = "http://changemakerchina.org/home/index/tp.html"
	paras = {"article_id":"181"}
	keepvoting=True
	votecount=0
	for i_myip in range(10):
		r = requests.post(url=url, data=paras, headers=headers)
		d = r.json()
		print(d)
		votecount+=1
		time.sleep(30) 
		
	while(keepvoting):
		try:
			r = requests.post(url=url, data=paras, headers=headers, proxies=proxy_choise, timeout=30)
		except(requests.Timeout, requests.ConnectionError):
			print("connection error, try next IP")
			ipid+=1
			if(ipid >= 53):
				keepvoting=False
			proxy_choise = proxies_list[ipid]
		else: 
			d = r.json()
			print(d)
			votecount+=1
			if(votecount >= 20):
				keepvoting=False
		
