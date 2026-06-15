from pycasso import Canvas
from random_seed import random_word



def scramble_img(img_path, slice_size: tuple[int, int] = (1, 1), minlength:int = 10, maxlength: int = 20):
    Canvas(img_path, slice_size, random_word(minlength, maxlength)).export('scramble', 'assets/scrambled_spectrogram', 'jpeg')

