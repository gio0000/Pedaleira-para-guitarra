import pyaudio
import wave

def gravar_audio(nome_arquivo="gravacao.wav", duracao=None):
    # Configurações do áudio
    formato = pyaudio.paInt16
    canais = 1
    taxa_amostragem = 44000
    frames_por_buffer = 1024

    audio = pyaudio.PyAudio()

    # Abrir o stream de entrada para captura de áudio
    stream = audio.open(
        format=formato,
        channels=canais,
        rate=taxa_amostragem,
        input=True,
        frames_per_buffer=frames_por_buffer
    )

    frames = []

    try:
        if duracao:
            # Captura de áudio por um período de tempo especificado
            for _ in range(int(taxa_amostragem / frames_por_buffer * duracao)):
                bloco = stream.read(frames_por_buffer)
                frames.append(bloco)
        else:
            # Captura de áudio indefinidamente até interrupção do usuário (Ctrl+C)
            while True:
                bloco = stream.read(frames_por_buffer)
                frames.append(bloco)
    except KeyboardInterrupt:
        pass
    finally:
        # Finaliza o stream de áudio
        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Salva os frames capturados em um arquivo WAV
        with wave.open(nome_arquivo, "wb") as arquivo_final:
            arquivo_final.setnchannels(canais)
            arquivo_final.setsampwidth(audio.get_sample_size(formato))
            arquivo_final.setframerate(taxa_amostragem)
            arquivo_final.writeframes(b"".join(frames))

        print(f"Gravação finalizada. Arquivo salvo como '{nome_arquivo}'.")

# Exemplo de uso para gravar áudio por 5 segundos
if __name__ == "__main__":
    duracao_gravacao = 5  # Tempo em segundos para gravar
    gravar_audio(nome_arquivo="gravacao.wav", duracao=duracao_gravacao)
