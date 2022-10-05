"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd
from datetime import datetime

def normalize_date(x):
    try:
        return datetime.strptime(x, '%d/%m/%Y')
    except ValueError:
        return datetime.strptime(x, '%Y/%m/%d')


def clean_data():
    df = pd.read_csv(
        "solicitudes_credito.csv",
        sep=";",
        usecols=[
            'sexo', 'tipo_de_emprendimiento', 'idea_negocio',
            'barrio', 'estrato', 'comuna_ciudadano',
            'fecha_de_beneficio', 'monto_del_credito', 'línea_credito']
    )

    df = df.dropna()

    list_col = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio',
                'barrio', 'línea_credito']
    for col in list_col:
        df[col] = df[col].str.lower()

    list_char = [' ', '-']
    for col in ['idea_negocio', 'línea_credito', 'barrio']:
        for char in list_char:
            df[col] = df[col].str.replace(char, '_')

    list_char_m = ['$', ',', '.00']
    col = 'monto_del_credito'
    for char in list_char_m:
        df[col] = df[col].apply(lambda s: s.replace(char, ''))

    df.monto_del_credito = df.monto_del_credito.str.strip()

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(
        lambda x: normalize_date(x))

    df.drop_duplicates(inplace=True)

    return df
