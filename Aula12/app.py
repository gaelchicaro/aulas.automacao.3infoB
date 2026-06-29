import pandas as pd
import pyautogui 
import time

def preencher(imagem, deslocamentoY = 0, valor = None):
    campo = pyautogui.locateCenterOnScreen(imagem, confidence= 0.9)
    pyautogui.click(campo.x, campo.y + deslocamentoY)
    if valor:
        pyautogui.write(valor)
    pyautogui.scroll(-100)
    time.sleep(1)

planilha = pd.read_excel("Aula12/dados_automacao.xlsx")
for indice, linha in planilha.iterrows():




    #Variáveis
    nome = linha["nome"]
    matricula = str(linha["matricula"])
    curso = linha["curso"]
    genero = linha["genero"]

    preencher("Aula12/email.png")
    preencher("Aula12/NomeCompleto.png", 50, nome)
    preencher("Aula12/matricula.png", 50, matricula)
    preencher("Aula12/Curso.png", 50, curso)
    preencher(f"Aula12/{genero}.png")
    preencher("Aula12/enviar.png")
    preencher("Aula12/outra.png")

