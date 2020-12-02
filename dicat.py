import time
import pyautogui as gui

wordlist = 'test.txt'
open_wordlist = open(wordlist, 'r')
list_wordlist = list(open_wordlist)

print("starting in 5seconds!")
time.sleep(5)
	
while True:
	
	guess = print(''.join(str(list_wordlist)))
	gui.write(str(guess))
	gui.press('Enter')
	time.sleep(.1)

