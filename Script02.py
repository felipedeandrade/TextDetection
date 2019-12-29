import subprocess
import os
import pytesseract as ocr
from PIL import Image
import time

def captura(arq,fps):
    subprocess.call(f'ffmpeg -y -i {arq} -vf fps=1/{fps} "{fps}.jpg" ')

def analise(fps):
    img = Image.open(str(fps) + '.jpg').crop((0, 480, 1280, 720))
    x = ocr.image_to_data(img,lang='eng+por')
    tabela = x.split()
    del tabela[0:12] #apaga a linha dos cabeçalhos
    y = len(tabela) #pega o tamanho da lista
    colunas = (y//11)
    inicio = 0
    for i in range(colunas):
        final = inicio + len(tabela[i::colunas])
        yield tabela[inicio:final]
        inicio = final

def confiabilidade(analise, fps):
    resultado=[]
    lista = list(analise)
    for e in range(len(lista)):
        try:
            resultado.append(int(lista[e][10]))
        except:
            resultado.append(lista[e][10])
    print(resultado)
    x = 0
    y = 0
    while x < len(resultado):
        tipo = type(resultado[x])
        if tipo == str:
            y=True
        x += 1
    if y == True:
        return True
    else:
        os.remove(str(fps) + '.jpg')
        return False

def run(arq,fps):
    while fps <= 700:
        captura(arq,fps)
        analise(fps)
        print(confiabilidade(analise(fps),fps))
        fps += 5
        #time.sleep(3)

run("458743.mp4",230)