import pyautogui as pg
import random
from time import sleep

sleep(8)

words = ('Puto', 'Gei', 'Mama huevo', 'Chupa piringa')

for i in range(1000):
	palabra = random.choice(words)
	print("message", palabra)
	pg.write("you are a ")
	pg.press('enter')
