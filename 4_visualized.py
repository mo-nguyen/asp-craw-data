import soundfile as sf
from pathlib import Path


def plot_spectrogram_and_save(signal, sample_rate, output_path: Path):
	

def main():
	signal, sample_rate = sf.read(Path("data")/ 'LibriSpeech-84-121123-0001.flac')
	print(f"Sample rate: {sample_rate}")
	plot_spectrogram_and_save(signal, sample_rate, Path("img")/'spectrogram.png')


if __name == "__main__":
	main()