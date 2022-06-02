import save
import random
import pandas as pd

def query_alunos():
  #query final ALUNOS
  with open('archives/alunos.txt', 'w') as f:
    f.writelines("INSERT INTO alunos (mat_alu, nome, cod_curso, cotista)\n")
    data = save.save_data()
    for item in data.items():
      f.writelines(f'VALUES ({item[0]}, "{item[1][0]}", "{item[1][1]}", {item[1][2]}, {item[1][3]}),\n')


# readfile = file1.read()


def query_matrizes():
  matriz = []
  #query Final matrizes
  with open('archives/matriculaSoInsert.txt', 'r') as f:
    for line in f.readlines():
      nota = random.choices([0,1,2,3,4,5,6,7,8,9,10], weights=(1,2,3,4,5,7,10,9,7,5,4))
      new_line = line.replace('(', '').replace(')','').replace(';','').replace('null', str(nota[0])).replace('\n', '')
      matriz.append(new_line.rsplit(','))
  matriz = pd.DataFrame(matriz, columns=['SEMESTRE', 'MAT_ALU', 'COD_DISC', 'NOTA', 'FALTAS'])

  with open('archives/matriculasDanilo.txt', 'w') as g:
    g.writelines("INSERT INTO MATRICULAS (SEMESTRE, MAT_ALU, COD_DISC, NOTA, FALTAS, 'STATUS')")
    for _, obj in matriz.iterrows():
      if int(obj[3]) >= 7 and int(obj[4]) <= 2:
          g.writelines(f"VALUES ({obj[0]}, {obj[1]}, {obj[1]}, {obj[2]}, {obj[3]}, 'A'),\n")
      else:
          g.writelines(f"VALUES ({obj[0]}, {obj[1]}, {obj[1]}, {obj[2]}, {obj[3]}, 'R'),\n")

    

def clean_inserts():
  with open("archives/alunos.txt", 'r+') as f:
    f.truncate(-1)
    
    
    
    
query_matrizes()
# clean_inserts()

# query_alunos()
# query_cursos()
# query_departamentos()
# query_disciplinas()