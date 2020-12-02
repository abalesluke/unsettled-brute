#script created by anikin luke
import random
import time
import pyautogui


chars = "1234567890"
char_list = list(chars)

password = "adsb"


guess_password = ""

while(guess_password != password):
	guess_password = random.choices(char_list, k=len(password))
	
	print("==>"+str(guess_password)+"<==")
	pyautogui.write(guess_password)
	time.sleep(.1)
	pyautogui.press('Enter',presses = 1)
	time.sleep(.5)
	pyautogui.press('backspace', presses = 4)
	

	if(guess_password == list(password)):
		print("Password Found! : "+ "".join(guess_password))
		break
