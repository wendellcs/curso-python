# Módulo OS

import os

# 1 - Retornar a pasta atual

print(os.getcwd())

# 2 - Listar arquivos e pastas

print(os.listdir())

# 3 - Verificar a versão do Sistema Operacional

os.system('ver')

# 4 - Configurações da máquina

os.system('systeminfo')

# 5 - Limpar a tela do terminal

os.system('cls')

# Desligar o computador

# os.system('shutdown /s') # desliga em 60 segundos

# os.system('shutdown /s /t 0') # desliga imediatamente

# Cancela o desligamento

# os.system('shutdown /a')

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')

def cancel_shutdown():
    os.system('shutdown /a')