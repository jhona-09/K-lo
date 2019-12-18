# K-lo

<b>
K-lo es un keylogger escrito en Python para Windows que puede tomar screenshots, recuperar el historial de Google Chrome y contraseñas guardadas, con la opción de enviar todos los archivos a una cuenta de corrreo electrónico.      


K-lo it's a Keylogger written in Python for Windows that can take screenshots, retrieve Google Chrome history and saved passwords, with the option of email all these files, for the english instructions please refer to README_ENGLISH.txt
</b>

K-lo tiene la función de ser keylogger que también realiza capturas de pantalla 
(screenshots). A su vez K-lo obtiene las contraseñas guardadas y el historial web 
del navegador Google Chrome, estas funciones las realiza en el tiempo que tu le indicas de manera
automatizada. Por lo que el historial se va actualizando, así como todos los archivos 
que K-lo obtiene y crea. 
K-lo también puede mandarte estos archivos a algún correo, estos se envían 
en el tiempo que tu indicas de manera automatizada, con el nombre 
de el usuario que tiene en ejecución K-lo y su IP publica. Para que puedas
identificarlos si lo tienes instalado en más de una maquina (wink).  
K-lo utiliza la librería pynput por lo que hasta el momento no se ha reportado 
LAG durante su execución, al contrario de la librería pyhook. 

<b>
PRIMER PASO:
</b>

Ejecuta el archivo K-lo.exe e ingresa los minutos en los que quieres
que se actualicen los archivos que se muestran a continuación.
K-lo.exe es el programa principal que genera:

1.- Screenshots 

2.- Excel con historial web de chrome 

3.- Excel con contraseñas guardadas en chrome 

4.- El Keylogger se genera y se actualiza cada que el usuario teclee algo. 
     
Puedes ejecutar K-lo.exe dejarlo que corra y consultar cada cierto tiempo los archivos en la computadora
que lo ejecutas. (Keylogger local) 
Ve al segundo paso si quieres generar correos enviandote los 4 archivos descritos arriba.


_ADVERTENCIA: SI VAS A UTILIZAR EL SEGUNDO PASO ADMINISTRA TUS TIEMPOS 
DEBIDO A QUE LOS TIEMPOS QUE ASIGNAS EMPIEZAN A CONTAR DESDE QUE SE 
CIERRA LA VENTANA DEL PROGRAMA ESTO ES IGUAL CUANDO EJECUTAS correo.exe_ 

_ADVERTENCIA: PRIMERO DEBES EJECUTAR K-lo.exe Y DESPUÉS correo.exe
DE LO CONTRARIO TE MARCARÁ UN ERROR AL EJECUTAR O SIMPLEMENTE NO HARÁ NADA_ 

<b>
SEGUNDO PASO:
</b>
Ejecuta el archivo correo.exe
Sigue las siguientes instrucciones:

1.- Ingresa los minutos en que se enviarán los correos periodicamente (elige un tiempo razonable) 

2.- Ingresa el correo del remitente (quién envía) 

3.- Ingresa la contraseña del remitente 

4.- Ingresa el correo del destinatario 

5.- ESPERA A QUE LA VENTANA SE CIERRE SOLA, al momento que se cierre la pantalla 

se envía un primer email y después se enviará en los minutos que indicaste.
verifica tu correo para que confirmes que sea correcto, 
de lo contrario algo hiciste mal al ingresar los datos de los correos. 

_ADVERTENCIA: PARA LOS REMITENTES UTILIZA SOLO CORREOS outlook.com, hotmail.com o gmail.com 
En el apartado de destinatarios es indiferente el tipo de correo que utilices. 
(Tal vez es muy obvio pero es preferible que tu seas el dueño 
de las dos cuentas de correo, remitente y destinatario)_ 

_ADVERTENCIA:
Si el remitente es GMAIL necesitas habilitar el uso de aplicaciones MENOS SEGURAS aqui https://myaccount.google.com/intro/security
inicia sesión y en la opcion habilitar aplicaciones menos seguras elige encendido_ 

<b>
¡¡LISTO!! 
</b>
Se mostrarán varios archivos pero los importantes son:

1.-historialweb.csv: Este es el historial de chrome en formato de excel

2.-passwords.csv: Estas son las contraseñas guardadas en chrome

3.-K-lo.txt: Este es el historial de las teclas oprimidas (keylogger) 

4.-screenshots.png: Estas son las capturas de pantalla 

_OJO:
Solo se toma 1 captura de pantalla cada cierto tiempo, para optimizar 
espacio y ser lo más cuidadoso posible. Por esta razón el archivo 
screenshots.png se sobreescribe (actualiza) en el tiempo que tu has asignado 
en el K-lo.exe_ 

_OJO:
Si no quieres que siga corriendo termina el proceso utilizando el 
administrador de tareas
SI APAGAN LA COMPUTADORA DEBES VOLVERLO A EJECUTAR SIGUIENDO LOS PASOS 
DE ARRIBA MENCIONADOS. (PRONTO SERA ARREGLADO)_  

_SUPER ADVERTENCIA:
ES MAS QUE OBVIO QUE DEBES ESCONDER LA CARPETA DONDE ESTAN ESTOS ARCHIVOS
PARA QUE LA VICTIMA NO SE DE CUENTA.
ES RECOMENDABLE UTILIZAR ALGUN LUGAR DE ARCHIVOS DE PROGRAMA EN C:/
PERO POR FAVOR NO LO PONGAS EN DESCARGAS, DOCUMENTOS, NI MUCHO MENOS ESCRITORIO.
Y NO MUEVAS NADA, AL MENOS QUE QUIERAS MODIFICARLO A TU MANERA, VE A LA CARPETA QUE DICE 
PYTHON AHI ESTAN LOS ARCHIVOS CON EL CODIGO FUENTE, ERES LIBRE DE MODIFICARLO._ 
<h2>
NO UTILICES ESTE PROGRAMA PARA USO INDEBIDO, MONITOREA EQUIPOS QUE SEAN DE TU PROPIEDDAD. 
</h2>
