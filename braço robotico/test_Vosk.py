import os
import sys
import wave
import json
import vosk
import pyaudio

# Função para iniciar a escuta do microfone
def ouvir_comando():
    model_path = "C:/vosk-model-small-pt-0.3"  # Substitua pelo caminho correto do modelo

    if not os.path.exists(model_path):
        print(f"Modelo não encontrado em {model_path}. Por favor, verifique o caminho.")
        sys.exit(1)

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Diga um comando:")

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            resultado = recognizer.Result()
            texto = json.loads(resultado).get("text", "")
            print(f"Você disse: {texto}")
            return texto.lower()

# Exemplo de uso
comando = ouvir_comando()
if "fechar dedos" in comando:
    # Aqui você adiciona a lógica para fechar os dedos
    print("Fechando os dedos...")
elif "girar pulso" in comando:
    # Aqui você adiciona a lógica para girar o pulso
    print("Girando o pulso...")
