class Camera:
	def capture_photo(self):
		print("took picture")
	def info(self):
		print("this is a camera")

class Stereo:
	def play_music(self):
		print("playing music")
	def info(self):
		print("this is a stereo")

canonEos = Camera()
canonEos.capture_photo()

sonyCmt = Stereo()
sonyCmt.play_music()

