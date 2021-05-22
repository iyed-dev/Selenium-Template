from pynput.mouse import Button, Controller
import time
mouse = Controller()
time.sleep(3)

def click_souris():
	mouse.position = (290, 330)
	mouse.press(Button.left)
	mouse.release(Button.left)
time.sleep(3)
click_souris()