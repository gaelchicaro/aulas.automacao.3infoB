import pyautogui
import time

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
pyautogui.write("chrome://dino")
pyautogui.press("enter")
time.sleep(3)

while True:
    pyautogui.press('space')
    time.sleep(1)