import argparse
import os

from spectrogram import plot_spectrogram
from img_scrambler import scramble_img

def main():
    parser = argparse.ArgumentParser(description='Generate a spectrogram from an audio file, then scramble it.')
    parser.add_argument('filepath', help='Path to the audio file.')
    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        parser.error(f"File not found: {args.filepath}")

    os.makedirs(os.path.dirname(args.filepath), exist_ok=True)

    title, ext = os.path.splitext(os.path.basename(args.filepath))

    print(f'Generating a spectrogram for {args.filepath}...')
    plot_spectrogram(args.filepath, f"Spectrogram for {args.filepath} ({ext})")

    print("Scrambling spectrogram...")
    scramble_img("assets/spectrogram.jpg")

    print("Done! Check assets folder for the results.")