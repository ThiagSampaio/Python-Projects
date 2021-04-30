import pandas as pd
def Data_Processing(file):
    data = pd.read_csv(file, error_bad_lines=False, sep=";")
    lista_estados = list(data["ESTADO "].unique())
    dict_data = {}
    for itens in lista_estados:
        dict_data[itens] = list(data[data["ESTADO "] == f"{itens}"]['E MAIL'])
    return lista_estados, dict_data