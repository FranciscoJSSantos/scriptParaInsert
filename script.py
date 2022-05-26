import random

with open("listaNomes.txt", 'r') as l:
  for name in l:
    listaNome = list(name.split(','))
    
for i in listaNome:
  #cotista
  cotista = random.randint(0,1)
  
  #print final
  print(f"VALUES ('{i}', {cotista})")

