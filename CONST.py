import os
import librosa
import numpy as np

def calculate_ann(x, Fs, n_anns=5):
    x_duration = (x.shape[0])/Fs
    borders = np.linspace(0.0, x_duration, n_anns+1)
    start_points = borders[:-1]
    end_points = borders[1:]
    ann = []
    for start_point, end_point in zip(start_points,end_points):
        ann.append((start_point,end_point,"X"))

    return ann, None, x_duration

def get_wav(Fs, name='01 Main Theme (Aberration).wav'):
    fn_wav = os.path.join('own_music_data', name)
    return librosa.load(fn_wav, sr=Fs)

"""
from CONST import get_wav, calculate_ann

Fs = 22050
x, Fs = get_wav(Fs, '01 Main Theme (Aberration).wav')
ann, color_ann, x_duration = calculate_ann(x, Fs)

fn_wav = os.path.join('own_music_data', '01 Main Theme (Aberration).wav')
"""
