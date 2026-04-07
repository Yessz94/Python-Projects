import os
import shutil

ruta = "carpeta_prueba"

for archivo in os.listdir(ruta):
    if archivo.endswith(".jpg"):
        shutil.move(f"{ruta}/{archivo}", f"{ruta}/imagenes/{archivo}")
    elif archivo.endswith(".pdf"):
        shutil.move(f"{ruta}/{archivo}", f"{ruta}/pdf/{archivo}")
    elif archivo.endswith(".txt"):
        shutil.move(f"{ruta}/{archivo}", f"{ruta}/textos/{archivo}")
