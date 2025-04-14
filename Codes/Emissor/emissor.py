import numpy as np
import sounddevice as sd

chords = {
    "C Major": [261.63, 329.63, 392.00],  # C, E, G
    "G Major": [196.00, 246.94, 392.00],  # G, B, D
    "A Minor": [220.00, 261.63, 329.63],  # A, C, E
}

fs = 44100
duration = 8

def generate_tone(frequencies, duration, fs):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    tone = sum(np.sin(2 * np.pi * f * t) for f in frequencies)
    return tone / len(frequencies)

def main():
    print("Escolha um acorde para tocar:")
    for i, chord in enumerate(chords.keys(), start=1):
        print(f"{i}. {chord}")
    
    choice = int(input("Digite o número do acorde escolhido: ")) - 1
    chord_name = list(chords.keys())[choice]
    frequencies = chords[chord_name]
    
    print(f"Tocando o acorde: {chord_name} ({frequencies} Hz)")
    tone = generate_tone(frequencies, duration, fs)
    sd.play(tone, fs)
    sd.wait()
    print("Execução finalizada.")

if __name__ == "__main__":
    main()
