from pynput.mouse import Button, Controller
mouse = Controller()

while 1:
	print(mouse.position)