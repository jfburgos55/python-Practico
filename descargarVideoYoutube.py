#!/usr/env/python27
#Autor: John Burgos
#Fecha: 2022/01/10
#Descripción: Programa creado para descargar videos de youtube
from pytube import YouTube
print("+---------- Descargar video de YouTube ----------+")
DOWNLOAD_FOLDER = "C:\\Users\\johnf\\Videos"
video_url = input("Ingresa la URL del video: ")
print("+---------- Por favor espere mientras se descarga.........")
video_obj = YouTube(video_url)
stream  = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)
print("Archivo guardado en: ",DOWNLOAD_FOLDER)
print()
print("¡¡ Exitoso !!")

