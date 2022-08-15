from classes import *
import pandas as pd

Individuo = [Pessoa] * 10
Estudante = [Aluno] * 10

for i in range(10):

    Individuo[i] = (
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[2]),   # nome
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[3]),   # genero
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[5]),   # email
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[8]),   # passaporte
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[9]),   # cpf
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[10]),  # nascimento
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[11]),  # Nacionalidade
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[1])    # id
    )
    Estudante[i] = (
        Individuo[i],
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[4]),  # Categoria
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[0]),  # Semestres
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[6]),  # Email Institucional
        pd.read_excel("Dados.xlsx", sheet_name=0, header=i, nrows=1, usecols=[7])   # Matricula
    )
    print(Estudante[i], "\n")
