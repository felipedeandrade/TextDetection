import glob
import os
import time

from _classes.metadados import metadados
from _functions import TextDetectionPosition


def main(file, position):
    start_processo = time.time()
    x = metadados(file)
    fileName = x.gfilename
    if os.path.exists(fileName):
        True
    else:
        os.makedirs(fileName)

    TextDetectionPosition.ffmpegStill(file, fileName)

    # divisão do processamento
    for file in glob.glob(fileName + "\*.jpg"):
        print(file)
        lista = TextDetectionPosition.analiseImage(file, position)
        TextDetectionPosition.processarImagem(lista[0], lista[1], lista[2])

    end_processo = time.time()
    print("Tempo total de processamento: {:.2f}min".format((end_processo - start_processo) / 60))


main("arquivodeteste.mp4", "both")
