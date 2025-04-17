import numpy as np
import sounddevice as sd
import time
import matplotlib
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy.signal import find_peaks

fs = 44100
duration = 5
channels = 1

# Acordes desejados:
# Dó maior: 523.25 Hz; 659.25 Hz; 783.99 Hz
# Ré menor: 587.33 Hz; 698.46 Hz; 880.00 Hz
# Mi menor: 659.25 Hz; 783.99 Hz; 987.77 Hz
# Fá maior: 698.46 Hz; 880.00 Hz; 1046.50 Hz
# Sol maior: 783.99 Hz; 987.77 Hz; 1174.66 Hz
# Lá menor: 880.00 Hz; 1046.50 Hz; 1318.51 Hz
# Si menor 5b: 493.88 Hz; 587.33 Hz; 698.46 Hz

matplotlib.use('TkAgg')

def record_audio():
    print("Gravando...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    return audio.flatten()

def compute_fft(audio):
    N = len(audio)
    yf = fftpack.fft(audio)
    xf = np.linspace(0.0, fs/2, N//2)
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

def find_top_frequencies(frequencies, magnitudes, min_distance=20):
    peaks, _ = find_peaks(magnitudes, distance=min_distance * (len(frequencies) / (frequencies[-1] - frequencies[0])))
    sorted_peaks = sorted(peaks, key=lambda x: magnitudes[x], reverse=True)
    top_peaks = sorted_peaks[:5]
    top_frequencies = frequencies[top_peaks]
    top_magnitudes = magnitudes[top_peaks]
    return top_frequencies, top_magnitudes

def plot_fft(frequencies, magnitudes):
    plt.figure(figsize=(10, 4))
    plt.plot(frequencies, magnitudes)
    plt.title('Espectro de Frequência do Sinal')
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.xlim(0, 2000)
    top_frequencies, top_magnitudes = find_top_frequencies(frequencies, magnitudes)
    plt.scatter(top_frequencies, top_magnitudes, color='red', label='Picos principais')
    for freq, mag in zip(top_frequencies, top_magnitudes):
        plt.text(freq, mag, f'{freq:.2f} Hz', fontsize=9, ha='center', va='bottom', color='blue')
    plt.legend()
    print("Frequências dos 5 picos mais presentes:", top_frequencies)
    
    #Identificar o acorde
    detected_chord = identify_chord(top_frequencies)
    print(f"Acorde detectado: {detected_chord}")
    
    plt.show()

def identify_chord(peak_frequencies, tolerance=1.5):
    #acordes cadastradsos
    chords = {
        "Dó maior": [523.25, 659.25, 783.99],
        "Ré menor": [587.33, 698.46, 880.00],
        "Mi menor": [659.25, 783.99, 987.77],
        "Fá maior": [698.46, 880.00, 1046.50],
        "Sol maior": [783.99, 987.77, 1174.66],
        "Lá menor": [880.00, 1046.50, 1318.51],
        "Si menor 5b": [493.88, 587.33, 698.46],
        "Jimi Hendrix (E7#9)": [329.63, 392.00, 587.33],
    }
    
    best_match = None
    max_matches = 0
    
    for chord_name, chord_freqs in chords.items():
        matches = 0
        
        #Para cada frequência do acorde ve se tem um pico próximo (tolerancia de erro de 1.5 Hz)
        for chord_freq in chord_freqs:
            for peak_freq in peak_frequencies:
                if abs(peak_freq - chord_freq) <= tolerance:
                    matches += 1
                    break  #Encontrou correspondência para esta frequência vai pra next
        
        #atualizar melhor correspondência
        if matches > max_matches:
            max_matches = matches
            best_match = chord_name
    
    #3 frequências do acorde para uma correspondência completa
    if max_matches == 3:
        return best_match
    else:
        return "Acorde não identificado"

audio = record_audio()
plot_audio_signal(audio)
frequencies, magnitudes = compute_fft(audio)
plot_fft(frequencies, magnitudes)