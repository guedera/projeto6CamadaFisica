# projeto6CamadaFisica
Em caso de erro:

    sudo apt install libportaudio2

## Computador 1
Computador toca audio por alguns segundos com 3 frequências específicas e múltiplos inteiras dessas frequências

(ocidental, 12 freqs)

para reproduzir o som, bib do python "sounddevice"!

gera 3 senoides das frequencias que quero
somo elas
executo elas através de

    sd.play(tone,fs)

    //variavel tone contem o sinal (senoides)
    //fs = frequencia de amostragem

(LISTA DE ACORDES)

#### PC 1
• Perguntar ao usuário qual acorde escolhido para execução.  
• Emitir por alguns segundos as 3 frequências relativas ao acorde escolhido.  
• Plotar o gráfico no domínio do tempo duas frequências somadas: 𝑥(𝑡) 
• Plotar o gráfico no domínio da frequência do sinal emitido (transformada de Fourier  𝑋(𝑓)  ) 

## Computador 2

captura audio (função rec)

    audio= sd.rec(int(numAmostras), freqDeAmostragem,channels = 1)
    sd.wait()
    print("fim")

transformada de fourier pra achar os picos

identifica picos

identifica acorde

#### PC 2
• Captar o sinal de áudio emitido pela aplicação do emissor através do microfone. Tente não gravar silêncio. 
Tente iniciar a gravação logo após o início da execução.  
• Veja se a gravação ficou com um bom volume. Você pode ajustar o volume do sinal gravado multiplicando 
ou dividindo todos os pontos do sinal por um valor. 
• Fazer o Fourier do sinal captado.  
• Identificar os picos. Mais de 4 picos! Você deverá ajustar a sensibilidade da função utilizada para identificar 
picos para ter no mínimo 5 picos).  
• Identificar as frequências dentre os picos relativas aos acordes, e assim identificar o acorde!  
• Plotar o gráfico no tempo do sinal recebido.  
• Plotar o gráfico da transformada de Fourier do sinal recebido.