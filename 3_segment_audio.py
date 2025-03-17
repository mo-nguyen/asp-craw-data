from pydub import AudioSegment
import librosa
import os
import json

path = "./raw_data"
list_mp4 = os.listdir(path)

data_path = "./data"

for i in list_mp4:
	try:
		audio_file_path = os.path.join(path, str(i), "audio", "audio.wav")
		duration = librosa.get_duration(path=audio_file_path)
		audio = AudioSegment.from_wav(audio_file_path)
		print(f"duration: {duration}")
		t1 = 0
		t2 = 25 * 1000
		count = 0
		code_path = os.path.join(path, str(i), "data", "data.json")
		code_data = {}
		with open(code_path, "r", encoding="utf-8") as f:
			code_data = json.load(f)
		code = code_data.get("code")
		while t2 < (duration * 1000):
			chunk = audio[t1:t2]
			chunk_path = os.path.join(data_path, "audio", f"{i}_chunk_{count}.wav")
			metadata_path = os.path.join(data_path, "metadata", f"{i}_chunk_{count}.json")
			os.makedirs(os.path.dirname(chunk_path), exist_ok=True)
			os.makedirs(os.path.dirname(metadata_path), exist_ok=True)
			metadata = {"code": code, "filename": f"{i}_chunk_{count}.wav"}
			with open(os.path.join(metadata_path), 'w', encoding='utf-8') as f:
			    json.dump(metadata, f, ensure_ascii=False, indent=4)
			chunk.export(chunk_path, format="wav")
			count += 1
			t1 = 25000 + t1 #Works in milliseconds
			t2 = 25000 + t2
	except Exception as e:
		print(f"index {i}: {e}")