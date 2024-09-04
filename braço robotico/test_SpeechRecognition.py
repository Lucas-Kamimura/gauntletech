from pyfirmata import Arduino, SERVO
import time
import speech_recognition as sr
import pyttsx3  # Biblioteca para converter texto em fala

# Inicializa a comunicação com a placa Arduino conectada na porta 'COM7'
board = Arduino('COM7')

# Inicializa o mecanismo de síntese de voz
engine = pyttsx3.init()

# Definição dos pinos que controlam os servos
pin1 = 10  # pino para o servo do polegar
pin2 = 9   # pino para o servo do dedo indicador
pin3 = 8   # pino para o servo do dedo médio
pin4 = 7   # pino para o servo do dedo anelar
pin5 = 6   # pino para o servo do dedo mínimo
pin6 = 5   # pino para o servo do pulso

# Configura os pinos definidos como SERVO
board.digital[pin1].mode = SERVO
board.digital[pin2].mode = SERVO
board.digital[pin3].mode = SERVO
board.digital[pin4].mode = SERVO
board.digital[pin5].mode = SERVO
board.digital[pin6].mode = SERVO

# Função para girar o servo até um determinado ângulo
def rotateServo(pino, angle):
    board.digital[pino].write(angle)
    time.sleep(0.015)

# Função para fechar ou abrir um dedo específico
def controlarDedo(dedo, acao):
    if acao == "fechar":
        if dedo == "polegar":
            rotateServo(pin1, 160)
        elif dedo == "indicador":
            rotateServo(pin2, 180)
        elif dedo == "médio":
            rotateServo(pin3, 180)
        elif dedo == "anelar":
            rotateServo(pin4, 180)
        elif dedo == "mínimo":
            rotateServo(pin5, 180)
        elif dedo == "pulso":
            rotateServo(pin6, 90)
    elif acao == "abrir":
        if dedo == "polegar":
            rotateServo(pin1, 0)
        elif dedo == "indicador":
            rotateServo(pin2, 0)
        elif dedo == "médio":
            rotateServo(pin3, 0)
        elif dedo == "anelar":
            rotateServo(pin4, 0)
        elif dedo == "mínimo":
            rotateServo(pin5, 0)
        elif dedo == "pulso":
            rotateServo(pin6, 0)

# Função para fechar todos os dedos
def fecharDedos():
    controlarDedo("polegar", "fechar")
    controlarDedo("indicador", "fechar")
    controlarDedo("médio", "fechar")
    controlarDedo("anelar", "fechar")
    controlarDedo("mínimo", "fechar")
    controlarDedo("pulso", "fechar")

# Função para abrir todos os dedos
def abrirDedos():
    controlarDedo("polegar", "abrir")
    controlarDedo("indicador", "abrir")
    controlarDedo("médio", "abrir")
    controlarDedo("anelar", "abrir")
    controlarDedo("mínimo", "abrir")
    controlarDedo("pulso", "abrir")

# Função para reconhecer comandos de voz
def reconhecer_comando():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Ajustando o microfone...")
        recognizer.adjust_for_ambient_noise(source)
        print("Pronto! Diga o comando:")
        audio = recognizer.listen(source)

    try:
        comando = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não entendi o que você disse. Tente novamente.")
        return ""
    except sr.RequestError:
        print("Erro ao se conectar ao serviço de reconhecimento de voz.")
        return ""

# Loop inicial para aguardar o comando "Prótese"
while True:
    comando = reconhecer_comando()
    if "prótese" in comando:
        engine.say("Sim, em que posso ajudar")
        engine.runAndWait()
        break

# Loop principal
while True:
    comando = reconhecer_comando()
    if "fechar dedos" in comando:
        fecharDedos()
    elif "abrir dedos" in comando:
        abrirDedos()
    elif "fechar" in comando:
        if "polegar" in comando:
            controlarDedo("polegar", "fechar")
        elif "indicador" in comando:
            controlarDedo("indicador", "fechar")
        elif "médio" in comando:
            controlarDedo("médio", "fechar")
        elif "anelar" in comando:
            controlarDedo("anelar", "fechar")
        elif "mínimo" in comando:
            controlarDedo("mínimo", "fechar")
        elif "pulso" in comando:
            controlarDedo("pulso", "fechar")
    elif "abrir" in comando:
        if "polegar" in comando:
            controlarDedo("polegar", "abrir")
        elif "indicador" in comando:
            controlarDedo("indicador", "abrir")
        elif "médio" in comando:
            controlarDedo("médio", "abrir")
        elif "anelar" in comando:
            controlarDedo("anelar", "abrir")
        elif "mínimo" in comando:
            controlarDedo("mínimo", "abrir")
        elif "pulso" in comando:
            controlarDedo("pulso", "abrir")
    elif "sair" in comando:
        print("Encerrando o programa.")
        break
