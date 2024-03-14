import pyautogui as pg
import random
from time import sleep

sleep(8)

words = ('Hola', 'Adios', 'Saludos', 'Good day')

for i in range(1000):
	palabra = random.choice(words)
	print("message", palabra)
	pg.write("! ")
	pg.press('enter')
