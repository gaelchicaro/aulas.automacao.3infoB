import pyautogui
import time

#abre uma janela de entrada de dados
pergunta= pyautogui.prompt("O que deseja saber hoje")

#pressiona um atalho do teclado(win+d= minimiza janelas)
pyautogui.hotkey('win','d')

#pressiona tecla win
pyautogui.press('win')

#digita um texto onde o cursor esta
pyautogui.write('chrome')

#pressiona a tecla enter
pyautogui.press('enter')

#faz uma pausa de 2 segundos
time.sleep(1)

#endereço do chat GPT
pyautogui.write("https://www.chatgpt.com")
pyautogui.press("enter")
time.sleep(1)

#digita o texto armazenado na variável pergunta
pyautogui.write(pergunta)
pyautogui.press("enter")



while True:
    time.sleep(2)
    try:
        xy=pyautogui.locateOnScreen("aula7/Captura.png", confidence=0.7)
        pyautogui.click(xy)
        break
    except:
        print('Ainda processando...')
time.sleep(2)

xy=pyautogui.locateOnScreen("aula7/copiar.png", confidence=0.98)
pyautogui.click(xy)
time.sleep(1)

pyautogui.hotkey('ctrl', 't')
time.sleep(2)

pyautogui.write('https://www.gmail.com')
pyautogui.press('enter')
time.sleep(3)


#clica no botão escrever
xy= pyautogui.locateOnScreen("aula7/escrever.png", confidence=0.95)
pyautogui.click(xy)

time.sleep(2)

#digita o endereço
pyautogui.write('softip@gmail.com')
pyautogui.press('tab')
pyautogui.write('Pesquisa automatizada')
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')

#clica no botão enviar
xy = pyautogui.locateCenterOnScreen('aula7/envia.png', confidence=0.95)
pyautogui.click(xy)

#termina
pyautogui.alert('Terminei o trabalho')
