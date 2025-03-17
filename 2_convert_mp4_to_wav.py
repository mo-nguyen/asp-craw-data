import subprocess
import os
# cmd = "ffmpeg -i ./audio.mp4 -ab 160k -ac 2 -ar 44100 -vn ./audio.wav"
# subprocess.call(cmd, shell=True)

path = "./raw_data"
list_mp4 = os.listdir(path)
print(list_mp4)

for i in list_mp4:
	try:
		video_path = os.path.join(path, i, "video")
		video_file_name = os.listdir(video_path)[0]
		print(video_file_name)
		video_file_path = os.path.join(video_path, video_file_name)
		audio_file_path = os.path.join(path, i, "audio", "audio.wav")
		os.makedirs(os.path.dirname(audio_file_path), exist_ok=True)

		cmd = f"ffmpeg -i {video_file_path} -ac 1 -ar 16000 -vn {audio_file_path}"
		subprocess.call(cmd, shell=True)
	except Exception as e:
		print(f"index {i}: {e}")
