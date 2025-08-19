import tkinter as tk
import pyautogui
import time
import threading  # para rodar a automação sem travar a interface

# Variável global para controlar o loop
running = False

def start_clicker():
    global running
    running = True
    interval = float(entry_interval.get())  # pega o intervalo do usuário

    def click_loop():
        while running:
            pyautogui.click()
            time.sleep(interval)
    # roda a automação em uma thread separada
    threading.Thread(target=click_loop).start()

def stop_clicker():
    global running
    running = False

# Criando a janela
root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x150")

# Campo para o intervalo
tk.Label(root, text="Intervalo entre cliques (s):").pack()
entry_interval = tk.Entry(root)
entry_interval.pack()

# Botões
tk.Button(root, text="Start", command=start_clicker).pack(pady=5)
tk.Button(root, text="Stop", command=stop_clicker).pack(pady=5)

root.mainloop()
