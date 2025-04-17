import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

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

#Essa função aqui plota o gráfico no tempo das freq somadas
def plot_time_domain(signal, fs, title="Sinal no domínio do tempo"):
    #Cria uns pontos no tempo pra vc ver direitinho
    time = np.linspace(0, len(signal)/fs, len(signal), endpoint=False)
    
    #Plota o bagulho
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel("Tempo (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

#Função q faz a transformada de Fourier e plota
def plot_frequency_domain(signal, fs, title="Transformada de Fourier"):
    #Faz a FFT
    fft_result = np.fft.fft(signal)
    #Calcula a magnitude q é oq interessa
    magnitude = np.abs(fft_result)
    #Cria os valores de freq pra vc ver no gráfico
    freq_bins = np.fft.fftfreq(len(signal), 1/fs)
    
    #Pega só as freq positivas pq as negativas n importam
    positive_freq_indices = freq_bins >= 0
    
    plt.figure(figsize=(10, 4))
    plt.plot(freq_bins[positive_freq_indices], magnitude[positive_freq_indices])
    plt.title(title)
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.xlim(0, 2000)  #Limita até 2000Hz p ficar + facil d ver
    plt.show()

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
    
    #Plota o gráfico de 2 freq somadas, mt massa
    if len(frequencies) >= 2:
        two_freq_tone = generate_tone(frequencies[:2], duration, fs)
        #Mostra só uns 0.05s p vc conseguir ver o padrão das ondas
        samples_to_show = int(0.05 * fs)
        plot_time_domain(two_freq_tone[:samples_to_show], fs, f"Sinal c/ 2 freqs: {frequencies[0]}Hz e {frequencies[1]}Hz")
    else:
        print("Precisa de pelo menos 2 freq p/ mostrar a soma!")
    
    #Agr plota a transformada d Fourier p vc ver as freq
    plot_frequency_domain(tone[:fs], fs, f"Transformada d Fourier do acorde {chord_name}")
    
    #Toca o bagulho no seu PC
    sd.play(tone, fs)
    #Espera acabar de tocar
    sd.wait()
    print("Execução finalizada.")

if __name__ == "__main__":
    main()
