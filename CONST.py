import os
import librosa

def calculate_ann(x, Fs):
    x_duration = (x.shape[0])/Fs
    return [(0.0, x_duration, "X")], None, x_duration

def get_wav(Fs, name='01 Main Theme (Aberration).wav'):
    fn_wav = os.path.join('own_music_data', name)
    return librosa.load(fn_wav, sr=Fs)