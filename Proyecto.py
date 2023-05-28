import cv2
import pytesseract
import matplotlib.pyplot as plt

from scripts.Caracteres import Caracter
from scripts.Especiales import Especial
from scripts.Letras import Letra

consonantes = {}
vocales = {}
caracteres_especiales = {}
numeros = {}

cuadro = 100

anchocam, altocam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, anchocam)
cap.set(4, altocam)


def text(image):

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texto = pytesseract.image_to_string(gris)

    for i in texto.lower():

        caracter = Caracter(i, False)
        letra = None
        especial = None
        if caracter.verificar_letra(i):
            caracter.isletter = True
            letra = Letra(caracter, False)
            if letra.is_vocal(i):
                letra.isvocal = True
            else:
                letra.isvocal = False
        else:
            caracter.isletter = False
            especial = Especial(caracter, False)
            if especial.is_num(i):
                especial.isnum = True
            else:
                especial.isnum = False

        key = caracter.value

        if letra != None and letra.isvocal == False:
            try:
                consonantes[key] += 1
            except:
                consonantes.update({key: 1})
        elif letra != None and letra.isvocal == True:
            try:
                vocales[key] += 1
            except:
                vocales.update({key: 1})
        elif especial != None and especial.isnum == True:
            try:
                numeros[key] += 1
            except:
                numeros.update({key: 1})
        else:
            try:
                caracteres_especiales[key] += 1
            except:
                caracteres_especiales.update({key: 1})

    print(consonantes)
    dire = open('Info.txt', 'w')
    dire.write(texto)
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
    return vocales, consonantes, caracteres_especiales, numeros


while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.putText(frame, 'Ubique aqui su texto a leer', (158, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.71, (255, 255, 0), 2)
    cv2.putText(frame, 'Ubique aqui su texto a leer', (160, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.rectangle(frame, (cuadro, cuadro), (anchocam -
                                            cuadro, altocam-cuadro), (0, 0, 0), 2)
    x1, y1 = cuadro, cuadro
    ancho, alto = (anchocam-cuadro) - x1, (altocam-cuadro) - y1
    x2, y2 = x1 + ancho, y1+alto
    doc = frame[y1:y2, x1:x2]
    cv2.imwrite('Imatext.jpg', doc)

    cv2.imshow('Lector Inteligente', frame)
    t = cv2.waitKey(1)
    if t == 27:
        break


vocales, consonantes, caracteres_especiales, numeros = text(doc)
cap.release()
cv2.destroyAllWindows()


names = list(vocales.keys())
values = list(vocales.values())
plt.subplot(2, 2, 1)
plt.bar(range(len(vocales)), values, tick_label=names)
plt.xlabel("Vocales")

names = list(consonantes.keys())
values = list(consonantes.values())
plt.subplot(2, 2, 2)
plt.bar(range(len(consonantes)), values, tick_label=names)
plt.xlabel("Consonantes")

names = list(caracteres_especiales.keys())
values = list(caracteres_especiales.values())
plt.subplot(2, 2, 3)
plt.bar(range(len(caracteres_especiales)), values, tick_label=names)
plt.xlabel("Especiales")

names = list(numeros.keys())
values = list(numeros.values())
plt.subplot(2, 2, 4)
plt.bar(range(len(numeros)), values, tick_label=names)
plt.xlabel("Numeros")

plt.suptitle("Diagrama de barras de caracteres")
plt.show()
