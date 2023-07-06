import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.ndimage import zoom
from moviepy.editor import AudioFileClip
import cv2

# Cargar la imagen y convertirla en una matriz numérica
image=cv2.imread("/home/emiliano/proyecto_INAOE/GATU/corona3.jpeg",0)


# Redimensionar la imagen utilizando submuestreo
subsample_factor = 10
subsampled_image = image[::subsample_factor, ::subsample_factor]

# Normalizar la matriz numérica
normalized_image = (subsampled_image - np.min(subsampled_image)) / (np.max(subsampled_image) - np.min(subsampled_image))

# Definir los parámetros de la señal de audio
sample_rate = 1300
duration = 3
frequencies = normalized_image * 1000

# Generar la señal de audio
time = np.linspace(0, duration, int(sample_rate * duration))
audio_signal = np.sin(2 * np.pi * frequencies[np.newaxis].T * time)
audio_signal = np.sum(audio_signal, axis=0)
audio_signal /= np.max(np.abs(audio_signal))

# Guardar la señal de audio en un archivo WAV
output_wav = "/home/emiliano/proyecto_INAOE/GATU/copia_gatu.py"
wavfile.write(output_wav, sample_rate, audio_signal)

# Convertir el archivo WAV a formato MP4
output_mp4 = "/home/emiliano/proyecto_INAOE/GATU/copia_gatu.py"
audio_clip = AudioFileClip(output_wav)
audio_clip.write_videofile(output_mp4, codec="libx264", audio_codec="aac")

# Eliminar el archivo WAV si no se necesita
# import os
# os.remove(output_wav)
