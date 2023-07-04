# Asistente virtual con IA (ChatGPT de OpenAI)
# Programado por Juan Carlos Gallardo Casas
# Docente de la Carrera de Ingeniería Civil en Informática

import speech_recognition as sr
import time
from gtts import gTTS
from playsound import playsound
import os
from email.message import EmailMessage
import smtplib
import imaplib
import email
import traceback 
import openai

remitente = "asistentevirtualulagos@gmail.com"
destinatarios = ['jcgallardo@gmail.com', 'jc.gallardo@ulagos.cl']
PASSWORD = "wyldgqnmzbxfwoxe"
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

ENGINE_IA = "text-davinci-003"
AUDIO_FILE = "audio.mp3"
openai.api_key = "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"  # you api-key here

USUARIO = "Master"
ASISTENTE = "Yeni"
LANGUAGE = "es"  # define audio language
AUDIO_FILE = "audio2.mp3"
fin = False

def voz_texto():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("\nHabla con claridad y lento por favor ... ")
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language="es-AR")
            return texto.strip()
        except:
            print("\nDisculpa, no pude reconocer lo que hablaste ...")
            return ""

def texto_voz(texto):
    tts = gTTS(texto, lang=LANGUAGE, slow=False)
    tts.save(AUDIO_FILE)
    time.sleep(1)    
    playsound(AUDIO_FILE)
    os.remove(AUDIO_FILE)
    
def interpretar(texto):
    global fin
    instrucciones = texto.split()
    comando = instrucciones[0]
    if comando == "listo":
        fin = True
        return "Nos vemos waaaaxiiiiiiiiin "+USUARIO
    elif comando == "correo":
        if len(instrucciones) > 0: 
            if instrucciones[1] == "enviar":
                if len(instrucciones) > 1:
                    mensaje = ""
                    for i in range(2, len(instrucciones)):
                        if i == 2:
                            mensaje = mensaje + instrucciones[i].title() + " "
                        else:
                            mensaje = mensaje + instrucciones[i] + " "

                    enviar_correo(mensaje)            
                    return "Enviando correo"
                else:
                    return "No hay mensaje para enviar"
            
            if instrucciones[1] == "recibir":
                    return recibir_correo()

    elif texto == "hola asistente":
        return "Hola " + USUARIO

    elif texto == "cuál es tu nombre":
        return "Mi nombre es " + ASISTENTE

# A continuación, la pregunta se transfiere a ChatGPT
    else:
        if len(instrucciones) > 1:
            completion = openai.Completion.create(engine=ENGINE_IA, prompt=texto, n=1, max_tokens=512)
            return completion.choices[0].text 
        else:
            return "No se reconoce el comando"

def enviar_correo(mensaje):
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = ", ".join(destinatarios)
    email["Subject"] = "Mensaje de la Asistente "+ASISTENTE
    email.set_content(mensaje)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, PASSWORD)
    smtp.sendmail(remitente, destinatarios, email.as_string())
    smtp.quit()

def recibir_correo():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(remitente,PASSWORD)
        mail.select('inbox')

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

    #        for i in range(latest_email_id, first_email_id, -1):
        i=latest_email_id
        data = mail.fetch(str(i), '(RFC822)' )
        for response_part in data:
            arr = response_part[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1],'utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                res = ""
                res = 'De ' + email_from + '\n'
                res = res + 'Asunto: ' + email_subject + '\n'
                return res
        return "No hay correos recibidos"

    except Exception as e:
            traceback.print_exc() 
            print(str(e))

while True:
    texto = voz_texto()
    if texto != "":
        print("\n"+texto)
        texto = texto.lower()
        res = interpretar(texto)
        print("\n"+res)
        texto_voz(res)
        if fin:
            break

            

    
