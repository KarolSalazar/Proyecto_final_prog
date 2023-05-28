import cv2
import pytesseract
import matplotlib.pyplot as plt

from scripts.Caracteres import Caracter
from scripts.Especiales import Especial
from scripts.Letras import Letra

import time
 
 #Importaciones y cosas varias uwu


inicio = time.time() # Tiempo en que inicia




consonantes = {}
vocales = {}
caracteres_especiales = {}
numeros = {}

#diccionarios vacíos


cuadro = 100 #Crea el cuadro de la camara

anchocam, altocam = 640, 480 # Definir dimensiones de la camara

cap = cv2.VideoCapture(0) # inicio de captura de video
cap.set(3, anchocam) # Cambiar las imensiones de la camara
cap.set(4, altocam)

def text(image):
    """
    Método o función encargada de obtener tanto el texto de la imagen, como de obtener las vocales, consonantes, caracteres especiales, y números
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Abre el archivo de Tesseract OCR para ejecutar
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Pone la imagen generada en escala de grises
    texto = pytesseract.image_to_string(gris) # Retorna el texto que hay en la imagen dentro de un string

    for i in texto.lower(): # Ciclo que verifica los diferentes caracteres dentro del texto

        caracter = Caracter(i, False)
        letra = None
        especial = None
        if caracter.verificar_letra(i): #Este if verifica que los caracteres sean letras
            caracter.isletter = True
            letra = Letra(caracter, False)
            if letra.is_vocal(i): #Verifica si la letra es una vocal
                letra.isvocal = True
            else:
                letra.isvocal = False
        else: # En caso de no ser letra hace otra cosa
            caracter.isletter = False
            especial = Especial(caracter, False)
            if especial.is_num(i): # Verifica si el caracter es un número
                especial.isnum = True
            else:
                especial.isnum = False

        key = caracter.value #Almacena el valor del caracter para guardarlo como llave del diccionario

        if letra != None and letra.isvocal == False: # Aquí almacena y verifica las consonantes en un diccionario
            try:
                consonantes[key] += 1
            except:
                consonantes.update({key: 1})
        elif letra != None and letra.isvocal == True: # Aquí almacena y verifica las vocales en un diccionario
            try:
                vocales[key] += 1
            except:
                vocales.update({key: 1})
        elif especial != None and especial.isnum == True: # Aquí almacena y verifica los números en un diccionario
            try:
                numeros[key] += 1
            except:
                numeros.update({key: 1})
        else:                                       # Aquí ya almacena los caracteres sobrantes
            try:
                caracteres_especiales[key] += 1
            except:
                caracteres_especiales.update({key: 1}) #Paco 969


    dire = open('Info.txt', 'w') # Crea o sobreescribe el archivo Info.txt
    dire.write(texto) # Escribe la información en el archivo
    dire.close()
    dire = open('Consonantes.txt', 'w')
    dire.write(str(consonantes))
    dire.close()
    dire = open('Vocales.txt', 'w')
    dire.write(str(vocales))
    dire.close()
    dire = open('Numeros.txt', 'w')
    dire.write(str(numeros))
    dire.close()
    dire = open('Especiales.txt', 'w')
    dire.write(str(caracteres_especiales))
    dire.close()
    return vocales, consonantes, caracteres_especiales, numeros #Retorna los diccionarios para usarlos después



while True: #Inicio de un bucle infinito que se ejecuta para renderizar la ventana de la cámara
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.putText(frame, 'Ubique aqui su texto a leer', (158, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 255, 0), 2) #Añade un texto
    cv2.putText(frame, 'Ubique aqui su texto a leer', (160, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) #Añade un texto detrás del anterior para resaltarlo
    cv2.rectangle(frame, (cuadro, cuadro), (anchocam -
                                            cuadro, altocam-cuadro), (0, 0, 0), 2) # Muestra el rectángulo donde estará el texto
    x1, y1 = cuadro, cuadro
    ancho, alto = (anchocam-cuadro) - x1, (altocam-cuadro) - y1
    x2, y2 = x1 + ancho, y1+alto # Ajusta el tamaño que tendrá la imagen dentro del rectángulo

    doc = frame[y1:y2, x1:x2] # guarda la imagen que hay dentro del rectángulo
    cv2.imwrite('Imatext.jpg', doc) # Escribe el archivo de la imagen con el almacenado dentro de "doc"

    cv2.imshow('Lector Inteligente', frame) #Muestra el frame en la pantalla
    t = cv2.waitKey(1) # Espera por que se presione la tecla "Esc"
    if t == 27: #Cuando se presiona "Esc" rompe el bucle, y queda almacenada la información en "doc"
        break


vocales, consonantes, caracteres_especiales, numeros = text(doc) # Llama la información de doc, para utilizarla en la funcion text, donde se hace el análisis de la imagen
cap.release() #termina el proceso de la captura
cv2.destroyAllWindows() # Cierra las ventanas generadas


names = list(vocales.keys()) # Genera una lista a partir de las llaves almacenadas en el diccionario de vocales
values = list(vocales.values()) # Genera una lista a partir de los valores almacenados en el diccionario de vocales
plt.subplot(2, 2, 1) #Hace el proceso de crear la grafica
plt.bar(range(len(vocales)), values, tick_label=names)
plt.xlabel("Vocales")

names = list(consonantes.keys()) #Genera una lista a partir de las llaves almacenadas en el diccionario de consonantes
values = list(consonantes.values()) # Genera una lista a partir de los valores almacenados en el diccionario de consonantes
plt.subplot(2, 2, 2) #Hace el proceso de crear la grafica
plt.bar(range(len(consonantes)), values, tick_label=names)
plt.xlabel("Consonantes")

names = list(caracteres_especiales.keys()) #Genera una lista a partir de las llaves almacenadas en el diccionario de caracteres especiales
values = list(caracteres_especiales.values()) # Genera una lista a partir de los valores almacenados en el diccionario de caracteres especiales
plt.subplot(2, 2, 3) #Hace el proceso de crear la grafica
plt.bar(range(len(caracteres_especiales)), values, tick_label=names)
plt.xlabel("Especiales")

names = list(numeros.keys()) #Genera una lista a partir de las llaves almacenadas en el diccionario de numeros
values = list(numeros.values()) # Genera una lista a partir de los valores almacenados en el diccionario de numeros
plt.subplot(2, 2, 4) #Hace el proceso de crear la grafica
plt.bar(range(len(numeros)), values, tick_label=names)
plt.xlabel("Numeros")

plt.suptitle("Diagrama de barras de caracteres")
plt.show()

fin = time.time() # Tiempo en el que finaliza
tiempo = fin-inicio # Hace la resta entre la hora fin e inicio
print("Tiempo de ejecución de la aplicación: " + str(tiempo)) #Muestra el tiempo de ejecucion