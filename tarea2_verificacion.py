import os
import glob

def calcular_crc(trama, polinomio):
    trama = list(trama)
    polinomio = list(polinomio)
    trama.extend(['0' for _ in range(len(polinomio) - 1)])

    while '1' in trama[:len(trama) - len(polinomio) + 1]:
        index = trama.index('1')
        for i in range(len(polinomio)):
            trama[index + i] = str(int(trama[index + i]) ^ int(polinomio[i]))

    return ''.join(trama[-len(polinomio) + 1:])

def verificar_crc(trama, polinomio):
    resto = calcular_crc(trama, polinomio)
    return all(bit == '0' for bit in resto)

# Directorio donde se encuentran los archivos .txt
directorio = 'dataset2/'

# Patrón de búsqueda de archivos .txt en el directorio
patron = os.path.join(directorio, '*.txt')

# Buscar archivos .txt en el directorio
archivos = glob.glob(patron)

# Polinomio CRC
polinomio_crc = "10001000000100001"

for archivo in archivos:
    with open(archivo, 'r') as file:
        trama_original = file.read().strip()  # Leer la trama desde el archivo

        # Agregar el CRC a la trama
        trama_con_crc = trama_original + calcular_crc(trama_original, polinomio_crc)

        # Simulación de una transmisión con ruido (introduciendo un error)
        trama_transmitida = list(trama_con_crc)
        trama_transmitida[5] = '1'  # Cambia el bit para simular un error

        # Verificar si la trama recibida tiene errores
        tiene_errores = verificar_crc(''.join(trama_transmitida), polinomio_crc)

        if not tiene_errores:
            print(f"Archivo: {archivo} - La trama tiene errores.")
        else:
            print(f"Archivo: {archivo} - La trama no tiene errores.")

        # Mostrar la secuencia generada en el receptor al revés
        secuencia_generada = trama_con_crc[-len(polinomio_crc) + 1:][::-1]
        print(f"Archivo: {archivo} - Secuencia generada receptor: {secuencia_generada}")