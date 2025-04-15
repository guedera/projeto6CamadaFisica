import numpy as np
import sounddevice as sd

chords = {
    "Dó maior": [523.25, 659.25, 783.99],
    "Ré menor": [587.33, 698.46, 880.00],
    "Mi menor": [659.25, 783.99, 987.77],
    "Fá maior": [698.46, 880.00, 1046.50],
    "Sol maior": [783.99, 987.77, 1174.66],
    "Lá menor": [880.00, 1046.50, 1318.51],
    "Si menor 5b": [493.88, 587.33, 698.46],
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
