import speech_recognition as SR
import time

r=SR.Recognizer()

with SR.AudioFile('#Aquí va la dirección del audio con doble diagonal invertida en cada carpeta en formato .wav#') as source:
    audio = r.listen(source)

    try:
        print('Espere un momento, el audio se está leyendo...')
        text = r.recognize_google(audio, language='es-ES')
        time.sleep(1.5)
        print (text)
    except:
        print('No se logró reconocer el audio')