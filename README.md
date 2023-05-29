# Proyecto final programacion

El proyecto final presentado consiste en una aplicación, la cual usa una camara, que identifica el texto enfocado en esta. Además distingue las vocales, consonantes, caracteres especiales y números. Realiza el historigrama de cada uno de estos datos capturados, los almacena en diccionarios. Crea un formato en .txt del texto reconocido en la cámara.

## Librerías utilizadas

Matplotlib = pip install matplotlib
cv2 = pip install opencv-python
      pip install opencv-contrib-python
pytesseract = pip install pytesseract

## Importante descargar

tesseract ocr, para el reconocimiento optico de caracteres

#### Descripción para descargar e instalar tesseract ocr

1. Dirigirse a: https://github.com/tesseract-ocr/tesseract
2. Bajar hasta installing tesseract
3. presionar  Install Tesseract via pre-built binary package (https://tesseract-ocr.github.io/tessdoc/Installation.html)
4. Bajar hasta la parte de windows 
5. presionar Tesseract at UB Mannheim (https://github.com/UB-Mannheim/tesseract/wiki)
6. presionar tesseract-ocr-w64-setup-5.3.1.20230401.exe (https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe)
7. Debe de instlar la extensión y puede continuar desde la terminal con "pip install pytesseract"
Nota: en lo ideal no cambie la ruta del archivo de instlación ya que si lo hace deberá modificar una linea del código proyecto.

## Explicación Archivos

El proyecto está compuesto de varios archivos

### Archivos Python

Se dividió en dos secciones principales, los que contiene la parte de herencias guardados en la carpeta de scripts y el proyecto.py el cual es el que se debe de ejecutar.

### Otros archivos

los archivos txt que es donde se guardan los diccionarios de la información registrada. y en especial el de info.txt que es el que almacena lo que leyó de la imagen

El archivo imatext.jpg almacena la imagen capturada por el programa

El archivo .gitignore tiene la carpeta que genera visual studio ya que contiene archivos innecesarios, contiene la base de datos que genera el propio programa
