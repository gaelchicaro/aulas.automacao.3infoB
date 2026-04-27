import pyautogui

xy=pyautogui.locateOnScreen('aula6\\captura8.png')
print(xy)

box = pyautogui.locateOnScreen('aula6\\captura8.png')
center_box = pyautogui.center(box)
print(center_box)

#opção2

xy2 = pyautogui.locateCenterOnScreen('aula6\\captura8.png', confidence=0.95)
print(xy2)
