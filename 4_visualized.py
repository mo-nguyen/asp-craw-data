import soundfile as sf
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def plot_spectrogram(signal, sample_rate):
	stft = librosa.stft(signal)
	spectrogram = np.abs(stft)
	spectrogram_db = librosa.amplitude_to_db(spectrogram)

	plt.figure(figsize=(10,4))
	img = librosa.display.specshow(spectrogram_db, y_axis="log", x_axis="time", sr=sample_rate, cmap="inferno")
	plt.xlabel("Time [s]")
	plt.ylabel("Frequency [Hz]")
	plt.colorbar(img, format="%+2.f dBFS")
	plt.show()

def main():
	plt.rcParams.update({"font.size": 20})
	signal, sample_rate = sf.read(Path("./data/audio/0_chunk_2.wav"))
	print(f"Sample rate: {sample_rate}")
	plot_spectrogram(signal, sample_rate)


if __name__ == "__main__":
	main()