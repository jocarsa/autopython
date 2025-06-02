import pyautogui
import time

mover_raton = pyautogui.moveTo(1096, 1053, duration=1)
click_raton = pyautogui.click() 
mover_raton = pyautogui.moveTo(1322, 962, duration=1)   
click_raton = pyautogui.click() 
mover_raton = pyautogui.moveTo(738, 512, duration=1) 
click_raton = pyautogui.click()  

pyautogui.write('Hola, esto es un texto escrito con PyAutoGUI.', interval=0.1)
