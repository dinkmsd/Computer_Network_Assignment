class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.numOfFrame = 0
		self.isNext = 0
		self.totalFrame = 0

		print('frame = 0')

	def get_total_time_video(self):
		self.totalFrame = 0
		while True:
			data = self.file.read(5)
			if data:
				frameLength = int(data)
				# Read the current frame
				data = self.file.read(frameLength)
				self.totalFrame += 1
			else:
				self.file.seek(0)
				break
			totalTime = self.totalFrame * 0.05
		return totalTime

	def setIsNext(self):
		self.isNext = 1

	def nextFrame(self):
		"""Get next frame."""
		if self.isNext == 1:
			forwardN0Frames = int(self.totalFrame*0.1)
			remainFrames = int(self.totalFrame - self.numOfFrame)
			if forwardN0Frames > remainFrames:
				forwardN0Frames = remainFrames
			self.isNext = 0

		else:
			forwardN0Frames = 1
		if forwardN0Frames:
			for i in range(forwardN0Frames):
				data = self.file.read(5) # Get the frameLength from the first 5 bits
				if data:
					frameLength = int(data)

					# Read the current frame
					data = self.file.read(frameLength)
					self.numOfFrame += 1
			return data

	def prevFrame(self):
		prevFrames = int(self.totalFrame * 0.1)
		if self.numOfFrame <= prevFrames:
			data = self.file.seek(0)
			self.numOfFrame = 0
			if data:
				frameLength = int(data)
				# Read the current frame
				data = self.file.read(frameLength)
				self.numOfFrame += 1
		else:
			data = self.file.seek(0)
			fFrames = self.numOfFrame - prevFrames
			self.numOfFrame = 0
			for i in range(fFrames):
				data = self.nextFrame()

		return data

	def frameNbr(self):
		"""Get frame number."""
		return self.numOfFrame

	
	