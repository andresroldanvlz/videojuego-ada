
import os
import random


from juego import Juego


class JuegoArchivo(Juego):
    
    def __init__(self, path_a_mapas):
        
        super().__init__()
        
        archivos = os.listdir(path_a_mapas)
        
        nombre_archivo = random.choice(archivos)
        
        path_completo = f"{path_a_mapas}/{nombre_archivo}"
        
        self.cadena = self.leer_archivo(path_completo)

    
    def leer_archivo(self, path):
        
        archivo = open(path, "r")
        
        cadena = ""
        
        for linea in archivo:
            
            cadena += linea
        
        archivo.close()
       
        cadena = cadena.strip()
        
        return cadena
