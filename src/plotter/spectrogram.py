import numpy as np

from matplotlib import pyplot as plt


def plot_spectrogram(audio_path: str, title: str, sr: int = 32000, n_mels: int = 128, fmax: int = 16000,
                     cmap: str = 'magma'):
    import librosa
    y, sr = librosa.load(audio_path, sr=sr, mono=True)
    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)

    melspec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
    melspec = librosa.power_to_db(melspec).astype(np.float32)

    import librosa.display
    img = librosa.display.specshow(melspec, x_axis='time', y_axis='mel', sr=sr, fmax=fmax, ax=ax, cmap=cmap)
    ax.set_title(title)

    plt.savefig("assets/spectrogram.jpg")
    plt.show(img)
