import pandas as pd

array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array1= [2, 1, 1, 2, 3, 5, 1, 2, 4]
array2=[2, 3, 4, 5]

def eval_duplicados(array):

    boleans=pd.Index(array).duplicated(keep=False)
    '''boleans = [ True  True  True  True False  True  True  True False]'''
    tamaño=len(array)
    if True in boleans:
        for index in range(0,tamaño):
            if boleans[index] == True:
                indiceRepetido=index
                break
        primer_repetido= array[indiceRepetido]
        return primer_repetido
    return False

print(eval_duplicados(array1))