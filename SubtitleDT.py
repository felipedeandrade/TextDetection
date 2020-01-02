import glob
import os
import time

from _classes.metadados import metadados
from _functions import TextDetection


def main(file):
    start_processo = time.time()

    x = metadados(file)

    fileName = x.gfilename

    if os.path.exists(fileName):
        True
    else:
        os.makedirs(fileName)

    TextDetection.ffmpegStill(file, fileName)

    for file in glob.glob(fileName + "\*.jpg"):
        print(file)
        lista = TextDetection.analiseImage(file)
        TextDetection.processarImagem(lista[0], lista[1], lista[2])
        # time.sleep(4)

    end_processo = time.time()

    print("Tempo total de processamento: {:.2f}min".format((end_processo - start_processo) / 60))


main("movie-test.mp4")
