import pyo

# Inicializa o servidor de áudio
s = pyo.Server().boot()

# Define a taxa de amostragem e o tamanho do bloco
sample_rate = 44100
block_size = 1024

# Cria um objeto de entrada de áudio
input_signal = pyo.Input()  # Captura o áudio do microfone

# Define o efeito de overdrive
# A função `overdrive` é um exemplo de processamento de distorção
def overdrive(signal, drive=1.0):
    return pyo.Limiter(pyo.Distortion(signal * drive, drive=drive), threshold=0.8)

# Aplica o efeito de overdrive
processed_signal = overdrive(input_signal)

# Cria um objeto de saída de áudio
output = pyo.Output(processed_signal)

# Inicia o servidor de áudio
s.start()

print("Processando áudio em tempo real. Pressione Ctrl+C para parar.")

try:
    # Mantém o programa em execução até que o usuário o interrompa
    s.gui(locals())
except KeyboardInterrupt:
    print("Interrompido pelo usuário.")

# Para o servidor de áudio
s.stop()
s.close()
