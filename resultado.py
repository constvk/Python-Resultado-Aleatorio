import os
import random
from colorama import Fore, init
init(convert=True)

#pergunta aleatória
print(f"[{Fore.RED}>{Fore.RESET}] Digite seu Nome Completo.")
user = input ("> ")

#espaço
print(" ")

#resultado
print(f"[{Fore.RED}>{Fore.RESET}] Seu Resultado foi;")
n = random.randint(0,10)
print(n)

#espaço, pause.
print(" ")
os.system("pause")
