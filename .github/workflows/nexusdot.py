import os
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
os.system('clear')
print('░█▄─░█ ░█▀▀▀ ▀▄░▄▀ ░█─░█ ░█▀▀▀█ ')
print('░█░█░█ ░█▀▀▀ ─░█── ░█─░█ ─▀▀▀▄')
print('░█──▀█ ░█▄▄▄ ▄▀░▀▄ ─▀▄▄▀ ░█▄▄▄█')
print('society dot - by nanoha\n')
# variaveis

f0 = 'vasco'

# comandos

print('[00] puxar nmr (test)	[01] gerar dds')
print(' ')
bash = input('faça sua escolha = ')
if bash == '00':
   os.system("clear")
   telefone = input('digite seu numero = ')
   telefone_ajustado = phonenumbers.parse(telefone)
   print(telefone_ajustado, '\n')
   operadora = carrier.name_for_number(telefone_ajustado,'pt-br')
   print(operadora, '\n')
   local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
   print(local)
else:
   print('escolha')

if bash == '01':
   os.system('clear')
   import random
   print('|=============================|')
   print('|======nexus society gen======|')
   print('|=============================|\n')
   nomes1 = ['felix ', 'adriano ', 'julio ', 'julia ', 'juliano ', 'juliano ', 'alexandro ']
   nomes2 = ['julia', 'maria', 'alex', 'alexandro', 'alexandra']
   nomes1 = random.choice(nomes1)
   nomes2 = random.choice(nomes2)
   print('NOME:')
   print(nomes1, nomes2, '\n')
   cpfs = ['88427847224', '56442729146', '64584666216', '6458466794236', '6458466564427', '79423295644272']
   cpfs = random.choice(cpfs)
   print('CPF:')
   print(cpfs, '\n')
   
else:
   print('')
   
