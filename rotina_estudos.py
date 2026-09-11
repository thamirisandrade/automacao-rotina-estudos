import pyautogui
import time

pyautogui.PAUSE = 1

print("O robô vai iniciar sua rotina de estudos em 3 segundos...")
time.sleep(3)

# Abre o Chrome pelo menu Iniciar
pyautogui.press("win")
pyautogui.write("Google Chrome", interval=0.02)
pyautogui.press("enter")

time.sleep(3)

# Abre a FIAP
pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://on.fiap.com.br", interval=0.02)
pyautogui.press("enter")

# Abre a Alura em outra aba
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://www.alura.com.br", interval=0.02)
pyautogui.press("enter")

# Abre seu GitHub em outra aba
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://github.com/thamirisandrade", interval=0.02)
pyautogui.press("enter")

print("Rotina iniciada! Bora estudar,")
