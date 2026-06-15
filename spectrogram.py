import librosa
import numpy as np
from matplotlib import pyplot as plt

y, sr = librosa.load('assets/call_me_merzbow_lo-fi.mp3', sr=32000, mono=True)
fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)

melspec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels = 128)
melspec = librosa.power_to_db(melspec).astype(np.float32)

import librosa.display
img = librosa.display.specshow(melspec, x_axis='time',  y_axis='mel', sr=sr, fmax=16000, ax=ax, cmap='magma')
ax.set_title('Melspectrogram of an harsh noise song')

plt.savefig("assets/output.jpg")
plt.show()