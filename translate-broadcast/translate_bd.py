# -*- coding: utf-8 -*-  

import urllib2  
import hashlib  
import json  
import random  
import urllib

class Baidu_Translation(object):  
	def __init__(self):
		self._q = 'Welcome to use BaiDu online translation tool'
		self._from = 'en'
		self._to = 'zh'
		self._appid = '20171204000102053'
		self._key = 'Uq6ZdOuiS7RiTqa36Amd'
		self._salt = random.randint(10001,99999)
		self._sign = ''
		self._dst = ''
		self._enable = True
#		print("init")
	def GetResult(self):
		self._q.encode('utf8')
#		print("self._q %s" %(self._q))
		m = str(self._appid)+self._q+str(self._salt)+self._key
#		print("m %s" %(m))
		m_MD5 = hashlib.md5(m)
		self._sign = m_MD5.hexdigest()
		Url_1 = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
		Url_2 = 'q='+urllib.quote(self._q)+'&from='+self._from+'&to='+self._to+'&appid='+str(self._appid)+'&salt='+str(self._salt)+'&sign='+self._sign
		Url = Url_1+Url_2
#		print Url
		PostUrl = Url.decode()
		TransRequest = urllib2.Request(PostUrl)
		TransResponse = urllib2.urlopen(TransRequest)
		TransResult = TransResponse.read()
		data = json.loads(TransResult)
#		print("data %s" %(data))
		if 'error_code' in data:
			print 'Crash'
			print 'error:',data['error_code']
			return data['error_msg']
		else:
			self._dst = data['trans_result'][0]['dst']
#			print("self._dst %s" %(self._dst))
			return self._dst




	def StartTrans(self,sentence):
		while self._enable:
#			self._q = raw_input("请输入你要翻译的句子：")
			self._q = sentence
			if cmp(self._q, '!quit') == 0:
				self._enable = False
				print 'Thanks for using!'
				break
			_q_len = len(self._q)
			if _q_len == 0:
				print 'Thanks for using!'
				break
#			print("_q_len %d" %(_q_len))
			if _q_len < 4096:
				result = self.GetResult()
#				print("result %s" %(result))
				return result
			else:
				print 'Exceeds the maximum limit of 4096 characters'
				break



 
