
import json
import itertools
from difflib import SequenceMatcher
import jellyfish


with open('file_with_strings.json') as file_data:
    data = json.load(file_data)
list_strings = []
for item in data.values():
    for it in item:
        list_strings.append(it["string"])

list_of_results = []


def similar(primeiro, proximo):
    '''
    RECEBE AS DUAS Strings E FAZ OS CALCULOS DE SIMILARIDADE. 
    O PERCENTAGE_MATCH É UM CALCULO DE PERCENTUAL DE SIMILARIDADE
    O CHAR_TO_CHANGE É UM CALCULO BASEADO NA DISTÂNCIA DE LEVENSHTEIN CONSIDERANDO A QUANTIDADE
    DE CARACTERES QUE DEVEM SER TROCADOS(INCLUÍDOS, DELETADOS, ALTERADOS) PARA QUE AS Strings SEJAM IGUAIS
    '''
      result = {
        "string_primeira": primeira,
        "string_proxima": proxima,
        "percentual_similar": SequenceMatcher(None, primeira, proxima).ratio(),
        "char_diferentes": jellyfish.levenshtein_distance(primeira, proxima)
    }

    list_of_results.append(result)

#Itera sob todas as queries para comparar umas com as outras
for primeira, proxima in itertools.combinations(list_strings, 2):
    similar(primeira, proxima)

#grava em um arquivo o resultado final
with open('final_result.txt', 'w') as outfile:
    json.dump(list_of_results, outfile)
