# Media movil
import numpy as np

def get_media_movil(array, window):
    if window > len(array):
        return 'La ventana es mayor al numero de datos'

    mv = [np.nan for _ in range(window - 1)]

    for index in range(len(array) - window + 1):
        mv.append(round(sum(array[index:index + window]) / window, 4))
    
    return mv

print(get_media_movil([3, 4, 5, 6, 7, 6, 1, 7, 2], 3))