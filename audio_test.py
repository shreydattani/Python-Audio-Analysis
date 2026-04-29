import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the audio file
file_path = 'test_audio.wav'
print(f"Loading {file_path}...")
y, sr = librosa.load(file_path)
# 2. Get the Tempo (BPM)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
print(f"Estimated Tempo: {tempo[0]:.2f} BPM")

# 3. Create a Mel-Spectrogram (Visual representation of frequencies)
print("Generating Spectrogram...")
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
S_dB = librosa.power_to_db(S, ref=np.max)

# 4. Display the image
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000)
plt.colorbar(format='%+2.0f dB')
plt.title('Mel-Spectrogram')
plt.tight_layout()
plt.show()