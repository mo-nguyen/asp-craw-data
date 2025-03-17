from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
import os
import cv2

image_frames = "./image_frames"
os.makedirs(image_frames, exist_ok=True)

def files():

	if not os.path.exists(image_frames):
		os.makedirs(image_frames)

	src_vid = cv2.VideoCapture("./test/2/video/video.mp4")
	return src_vid

def process(src_vid):
	folder = os.path.join(image_frames, "frame")
	os.makedirs(folder, exist_ok=True)
	index = 0
	while src_vid.isOpened():
		ret, frame = src_vid.read()
		if not ret or index > 3000:
			break

		name = os.path.join(folder, str(index) + ".png")

		if index % 100 == 0:
			print("Extracting frames..." + name)
			cv2.imwrite(name, frame)
		index += 1
		if cv2.waitKey(10) & 0xFF == ord("q"):
			break
	src_vid.release()
	cv2.destroyAllWindows()

def get_text():
	for i in os.listdir(os.path.join(image_frames, "frame")):
		my_example = Image.open(os.path.join(image_frames, "frame", i))
		text = pytesseract.image_to_string(my_example, lang="eng")
		print(f"index: {i} - text: {text}")


if __name__ == "__main__":
	vid = files()
	process(vid)
	get_text()