import os
import glob

# Polinomio CRC-CCITT
polinomio_crc = "10001000000100001"  # X^16 + X^12 + X^5 + 1

# Función para leer los datos desde un archivo
def leer_datos_desde_archivo(archivo):
    with open(archivo, 'r') as file:
        return file.read().strip()  # Lee el contenido del archivo y elimina espacios en blanco

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
    
    crc_result = ''.join(map(str, bits[-n + 1:]))
    return crc_result

# Ruta a la carpeta del dataset2 (ajusta la ruta según tu directorio)
carpeta_dataset2 = "dataset2"

# Leer los archivos del dataset2
archivos_dataset2 = glob.glob(os.path.join(carpeta_dataset2, "*.txt"))

# Procesar los archivos del dataset2
for archivo in archivos_dataset2:
    datos = leer_datos_desde_archivo(archivo)
    print("Datos de", archivo)

    # Calcular el CRC-CCITT para la trama
    crc_calculado = calcular_crc_ccitt(datos, polinomio_crc)

    # Verificar si los datos contienen errores
    es_correcto = crc_calculado == "0" * 16  # Compara con 16 ceros 
    if es_correcto:
        print("NO")
    else:
        print("SI")

    # Secuencia generada en receptor
    secuencia_receptor = datos[:-16]  # Suponiendo que el CRC tiene 16 bits
    print("Secuencia generada en receptor:", secuencia_receptor)