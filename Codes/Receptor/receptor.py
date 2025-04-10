import numpy as np
import sounddevice as sd
import time
import matplotlib.pyplot as plt
from scipy import fftpack  # Importando fftpack do scipy para a transformada de Fourier

fs = 44100  #Taxa de amostragem em Hz
duration = 5  #Duração da gravação em segundos
channels = 1  #Mono

def record_audio():
    print("Iniciando gravação!")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()

    print("Gravação finalizada.")
    
    return audio.flatten()  #flatten pra ficar unidimensional (garante que seja)

def compute_fft(audio):

    N = len(audio)
    #Calcular a FFT
    yf = fftpack.fft(audio)
    #Criar array de frequências correspondentes
    xf = np.linspace(0.0, fs/2, N//2)
    
    #pega freqs positivas e normaliza amplitudes
    return xf[:N//2], 2.0/N * np.abs(yf[:N//2])

def plot_audio_signal(audio):

    t = np.linspace(0, duration, len(audio))
    plt.figure(figsize=(10, 4))
    plt.plot(t, audio)
    plt.title('Sinal de Áudio no Domínio do Tempo')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

def plot_fft(frequencies, magnitudes):

    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, magnitudes)
    plt.title('Espectro de Frequência do Sinal')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    
    #Limita o eixo x até 2000 Hz para melhor visualização
    plt.xlim(0, 2000)
    plt.show()

# Gravar o áudio
audio = record_audio()

# Plotar o sinal no domínio do tempo
plot_audio_signal(audio)

# Calcular a transformada de Fourier
frequencies, magnitudes = compute_fft(audio)

# Plotar o espectro de frequência
plot_fft(frequencies, magnitudes)