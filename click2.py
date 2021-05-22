from pynput.mouse import Button, Controller
import time
mouse = Controller()
time.sleep(3)

def click_souris():
	mouse.position = (940, 1010)
	mouse.press(Button.left)
	time.sleep(3)
	mouse.release(Button.left)
click_souris()

time.sleep(2)
def click_souris_2():
	mouse.position = (615, 925)
	mouse.press(Button.left)
	mouse.release(Button.left)
click_souris_2()