# -*- coding: utf-8 -*-
import pyaudio
import wave
from   time import sleep

class AudioPlayer:
	""" A Class for Playing Audio """

	def __init__(self):
		self.audio_file=""

	def setAudioFile(self, audio_file):
		self.audio_file = audio_file

	def playAudio(self):
		if (self.audio_file == ""):
			return
		self.wf=wave.open(self.audio_file,'rb')
		p=pyaudio.PyAudio()
		stream = p.open(format=p.get_format_from_width(self.wf.getsampwidth()),
						channels=self.wf.getnchannels(),
						rate=self.wf.getframerate(), output=True,
						stream_callback=self.callback)
		stream.start_stream()

		while stream.is_active():
			sleep(0.1)

		stream.stop_stream()
		stream.close()
		self.wf.close()
		p.terminate()

	def callback(self, in_data, frame_count, time_info, status):
		data = self.wf.readframes(frame_count)
		return(data, pyaudio.paContinue)


if __name__ == "__main__":
	player=AudioPlayer()
	player.setAudioFile("aitalk.wav")

	player.playAudio()
