import random

with open("listaNomes.txt", 'r') as l:
  for name in l:
    listaNome = list(name.split(','))
    


#print final
with open('teste.txt', 'a') as f:
  f.writelines("INSERT INTO alunos (nome, cotista)\n")
  for i in listaNome:
        #cotista
    cotista = random.randint(0,1)
    f.writelines(f"VALUES ('{i}', {cotista}), \n")



