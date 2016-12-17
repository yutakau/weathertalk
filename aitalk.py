#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-

import sys
import httplib2
import json

class AITalkClient(object):

	def __init__(self):
		# REST API のエンドポイント
		self._endpoint = "http://webapi.aitalk.jp/webapi/v2/ttsget.php"
		# 表現のフォーマット
		self._format = "json"
		self._ext    = "wav"
		self._username = "XXXXXXXXXXX"   #API username
		self._password = "XXXXXXXXXXX"   #API passwordß
		self._speaker  = "nanako"

	def request(self, text):
		# HTTPクライアントを得る
		http_client = httplib2.Http(".cache")
		uri = "%s?%s=%s&%s=%s&%s=%s&%s=%s&%s=%s" % \
		(self._endpoint,
		"username",self._username,
		"password",self._password,
		"text",text,
		"ext",self._ext,
		"speaker_name",self._speaker)

		#debug print
		#print uri

		# REST APIを呼び出す
		resp, content = http_client.request(uri, "GET")
		print resp
		#print content
		f=open ("aitalk.wav","w")
		f.write(content)
		f.close()
		return 

	def talk(self, text):
		return self.request(text)


if __name__ == '__main__':
	client = AITalkClient()
	response = client.talk(u"テストメッセージ。")
	print response

