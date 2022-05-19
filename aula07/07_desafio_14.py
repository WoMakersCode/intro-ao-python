import sys
import requests
import json

# Crie uma aplicação que permita ao usuário obter informações sobre um determinado feitiço.
# O usuário deve digitar o nome de um feitiço como entrada para a nossa aplicação através da
# linha de comando. Por exemplo:
# python 07_desafio_14.py Vanishing Spell
# Você deverá obeter os dados sobre o feitiço diretamente do JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
# Utilize a biblioteca requests para ler o JSON.
# Ao final do programa, imprima os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.
