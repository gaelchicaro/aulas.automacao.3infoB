import pyautogui

#localiza o botão 8 e clica
xy8 = pyautogui.locateCenterOnScreen('aula6\\captura8.png',confidence=0.95 )
pyautogui.click(xy8, duration=1)

#localiza o botão + e clica
xy8 = pyautogui.locateCenterOnScreen('aula6\\btn+.png',confidence=0.95 )
pyautogui.click(xy8, duration=1)

#localiza o botão 2
xy8 = pyautogui.locateCenterOnScreen('aula6\\btn2.png',confidence=0.95 )
pyautogui.click(xy8, duration=1)

#localiza o botão =
xy8 = pyautogui.locateCenterOnScreen('aula6\\btn=.png',confidence=0.95 )
pyautogui.click(xy8, duration=1)