#!/usr/bin/env python
#coding:utf-8

# Weather forecast 
# libdoor weather API, 2016/12

import urllib2, sys
import json

import aitalk
import audioplayer

from pprint import pprint

citycode = '270000'   #Osakaの都市コード


resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

obj = json.loads(resp)
#print obj['title']
#print obj['description']['text']

forecasts = obj['forecasts']
tomorrow = forecasts[1]
#tomorrow['dateLabel']

tomorrow_weather = tomorrow['telop']

#天気概況テキストを作成する
text = tomorrow['dateLabel'] +u'、'+ tomorrow_weather + u'。'+ obj['description']['text']

#AITALKが受けられる文字列へ変換
# 空行がまずいので分割
a = text.splitlines()
#LivedoorWeatherは半角スペースこみの文字列を返すが、
#これが含まれるとAITalkはエラー(HTTP 400)となるので除去する
txt=""
for i in a:
	txt = txt + i.replace(' ','')
print txt

client = aitalk.AITalkClient()
response = client.talk(txt)
print response

#WAVを再生
player=audioplayer.AudioPlayer()
player.setAudioFile("aitalk.wav")

player.playAudio()




