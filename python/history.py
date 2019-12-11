import sqlite3 
import pandas.io.sql
import pandas  
import os 
import shutil, getpass
from shutil import copyfile 
import time, threading

def historialdechrome():

##copia archivo de historial de chrome a carpeta local 
	src ="C:\\Users\\%s\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History" %(getpass.getuser())
	dest=os.getcwd() 

	def copyFile(src,dest):
		try:
			shutil.copy(src,dest)
		
		except shutil.Error as e:
			print('Error: %s' %e)


	copyFile(src,dest)
##copia archivo de historial de chrome a carpeta local 



#crea base de datos del historial y exporta a csv 
	data_path = os.getcwd()
	files = os.listdir(data_path)
	historial_db = os.path.join(data_path,'History')

	c = sqlite3.connect(historial_db)
	cursor = c.cursor()
	pand=pandas.io.sql.read_sql("SELECT DISTINCT datetime(last_visit_time/1000000-11644495200,'unixepoch'), urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url order by last_visit_time desc;", c)
	pand.to_csv('historialweb.csv')

#crea base de datos del historial y exporta a csv 
historialdechrome()

