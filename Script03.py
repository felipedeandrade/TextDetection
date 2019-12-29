from pymediainfo import MediaInfo
import pytesseract as ocr
from PIL import Image
import subprocess
import glob
import os

import time

def ffmpegStill(file, fileName):
    subprocess.call(f'ffmpeg -y -i {file} -vf fps=2 "./{fileName}/{fileName}_%04d.jpg" ')

def analise(file):
    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == 'Image':
            w = track.width
            h = track.height
    x = []
    img = Image.open(file).crop((0, 720, 1920, 1080))
    x = ocr.image_to_data(img, lang='eng+por')
    tabela = x.split()
    del tabela[0:12]  # apaga a linha dos cabeçalhos
    y = len(tabela)  # pega o tamanho da lista
    colunas = (y // 11)
    inicio = 0
    for i in range(colunas):
        final = inicio + len(tabela[i::colunas])
        yield tabela[inicio:final]
        inicio = final

def confiabilidade(analise,file):
    resultado=[]
    lista = list(analise)
    for e in range(len(lista)):
        try:
            resultado.append(int(lista[e][10]))
        except:
            resultado.append(lista[e][10])
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
        os.remove(file)
        return False

def run(file):
    fileName = file[:-4]

    if os.path.exists(fileName):
        True
    else:
        os.makedirs(fileName)

    ffmpegStill(file,fileName)

    for file in glob.glob(fileName + "\*.jpg"):
        print(file)
        analise(file)
        confiabilidade(analise(file),file)
        #time.sleep(4)
run("movie-test.mp4")