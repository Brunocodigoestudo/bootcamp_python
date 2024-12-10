import pandas as pd
import os
import sys
import glob

#extract

pasta = "dados"
def extração(pasta:str)-> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_consolidado = pd.concat(df_list, ignore_index=True)
    return df_consolidado

# transformação

def transformação_calculo(df: pd.DataFrame)-> pd.DataFrame:
   df["Total"] = df["Quantidade"] * df["Venda"]
   return df

#load

def carregar_dados(df: pd.DataFrame):
    df_final = df.to_csv('df_consolidado', index=False)
    return df_final

#test


def pipeline_final_vendas(pasta: str):
    data_frame = (extração(pasta))
    transform = (transformação_calculo(data_frame))
    df_consolidado = carregar_dados(transform)
    
    
