from pytubefix import YouTube
from pytubefix.cli import on_progress
import json
import os


list_youtube_file = "./list_youtube_url.json"

list_youtube = []
with open(list_youtube_file, 'r', encoding='utf-8') as f:
    list_youtube = json.load(f)

for i in range(0, len(list_youtube)):
	yt_obj = list_youtube[i]
	try:
		url = yt_obj.get("url")
		code = yt_obj.get("code")

		dir_name = os.path.join("./raw_data", str(i))
		data_dir = os.path.join(dir_name, "data", "data.json")
		video_dir = os.path.join(dir_name, "video")

		os.makedirs(os.path.dirname(dir_name), exist_ok=True)
		os.makedirs(os.path.dirname(data_dir), exist_ok=True)
		os.makedirs(os.path.dirname(video_dir), exist_ok=True)

		yt = YouTube(url, on_progress_callback=on_progress)
		yt.title = "video"
		caption = yt.captions['a.vi']
		txt = caption.generate_srt_captions().splitlines()
		filtered_txt = list(filter(lambda x: x != "", txt))
		# data = []
		full_content = ""
		for i in range(0, len(filtered_txt), 3):
			# number = filtered_txt[i]
			# time_range = filtered_txt[i+1]
			content = filtered_txt[i+2]
			full_content = full_content + " " + content
			# data.append({"number": number, "time_range": time_range, "content": content})
		# print(data)
		data = {"code": code, "content": full_content}
	

		with open(os.path.join(data_dir), 'w', encoding='utf-8') as f:
		    json.dump(data, f, ensure_ascii=False, indent=4)

		ys = yt.streams.get_highest_resolution()
		ys.download(output_path=video_dir)
	except Exception as e:
		print(f"index {i}: error {e}")
