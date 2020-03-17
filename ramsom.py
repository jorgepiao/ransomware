#!/usr/bin/env python
#_*_ codign: utf8 _*_

import os
import socket


	# listar el contenido del directorio HOME
home = os.environ['HOME']
carpetas = os.listdir(home)
	# Eliminar las carpetas que empiecen con .
carpetas = [x for x in carpetas if not x.startswith('.')]
print(carpetas)

def check_internet():
		# crear el socket (conector)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# tiempo maximo de espera
	s.settimeout(2)

		# verificar la conexion a internet
	try:
		s.connect(('socket.io',80))
		# print('Conectado')
		s.close()
	except:
		exit()




def main():
	check_internet()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()




