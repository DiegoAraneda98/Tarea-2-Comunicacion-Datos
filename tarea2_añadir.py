import os
import glob

# Polinomio CRC-CCITT
polinomio_crc = "10001000000100001"  # X^16 + X^12 + X^5 + 1

# Función para calcular el CRC-CCITT de una secuencia de bits
def calcular_crc_ccitt(bits, polinomio):
    bits = list(map(int, bits))
    polinomio = list(map(int, polinomio))
    n = len(polinomio)
    bits.extend([0] * (n - 1))
    
    for i in range(len(bits) - n + 1):
        if bits[i] == 1:
            for j in range(n):
                bits[i + j] ^= polinomio[j]
    
    return ''.join(map(str, bits[-n + 1:]))

# Función para leer los datos desde un archivo
def leer_datos_desde_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.read().strip()  # Lee el contenido del archivo y elimina espacios en blanco

# Ruta a la carpeta del dataset1 (ajusta la ruta según tu directorio)
carpeta_dataset1 = "dataset1"

# Leer los archivos del dataset1
archivos_dataset1 = glob.glob(os.path.join(carpeta_dataset1, "*.txt"))

# Procesar los archivos del dataset1
for archivo in archivos_dataset1:
    datos = leer_datos_desde_archivo(archivo)
    print("Datos de", archivo, ":", datos)

    # Calcular el CRC-CCITT para los datos
    crc_calculado = calcular_crc_ccitt(datos, polinomio_crc)
    print("CRC-CCITT calculado:", crc_calculado)









