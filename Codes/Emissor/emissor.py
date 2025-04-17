import numpy as np
import sounddevice as sd

#Acordes da lista
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

#Taxa de amostragem
fs = 44100
#Quanto tempo vai rolar o som
duration = 10

#Essa função aqui gera os sons
def generate_tone(frequencies, duration, fs):
    #Cria uns pontos no tempo pra calcular as ondas
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    tone = sum(np.sin(2 * np.pi * f * t) for f in frequencies)
    #Normaliza pra não estourar seu fone
    return tone / len(frequencies)

def main():
    print("Escolha um acorde para tocar:")
    #Mostra as opções pra vc não ficar boiando
    for i, chord in enumerate(chords.keys(), start=1):
        print(f"{i}. {chord}")
    
    #Pega o que vc escolheu
    choice = int(input("Digite o número do acorde escolhido: ")) - 1
    chord_name = list(chords.keys())[choice]
    frequencies = chords[chord_name]
    
    #Avisa qual som vai tocar
    print(f"Tocando o acorde: {chord_name} ({frequencies} Hz)")
    #Gera o som com as paradas que vc escolheu
    tone = generate_tone(frequencies, duration, fs)
    #Toca o bagulho no seu PC
    sd.play(tone, fs)
    #Espera acabar de tocar
    sd.wait()
    print("Execução finalizada.")

if __name__ == "__main__":
    main()
