import pyautogui
import time
import keyboard
import win32api,win32con




POS1 = (650,560)
POS2 = (750,560)
POS3 = (850,560)
POS4 = (950,560)
BLACK =1

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENT_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENT_LEFTUP, 0, 0)
    

while not keyboard.is_pressed('q'):
    if pyautogui.pixel(POS1[0], POS1[1])[0] == BLACK:
        click(POS1[0], POS1[1])

    if pyautogui.pixel(POS2[0], POS2[1])[0] == BLACK:
        click(POS2[0], POS2[1])

    if pyautogui.pixel(POS3[0], POS3[1])[0] == BLACK:
        click(POS3[0], POS3[1])

    if pyautogui.pixel(POS4[0], POS4[1])[0] == BLACK:
        click(POS4[0], POS4[1])

    time.sleep(0.01)


