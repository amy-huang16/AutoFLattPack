import pyautogui as pg

screenWidth, screenHeight = pg.size() # returns screen size 
print("Screen width is:", screenWidth, "\nScreen height is:", screenHeight)
currentMouseX, currentMouseY = pg.position() # returns current cursor x and y position. if using touch screen, use touch screen to press run button while keeping cursor at desired position
print("Current x position:", currentMouseX, "Current y position:", currentMouseY)