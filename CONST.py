import os
import librosa

def calculate_ann(x, Fs):
    x_duration = (x.shape[0])/Fs
    return [(0.0, x_duration, "X")], None, x_duration

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