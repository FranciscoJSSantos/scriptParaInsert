import save
import random
import pandas as pd
from random_date import random_date

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
    for _, obj in matriz.iterrows():
      g.writelines("INSERT INTO MATRICULAS (SEMESTRE, MAT_ALU, COD_DISC, NOTA, FALTAS, STATUS) ")
      if int(obj[3]) >= 7 and int(obj[4]) <= 2:
          g.writelines(f" VALUES ({obj[0]}, {obj[1]}, {obj[2]}, {obj[3]}, {obj[4]}, 'A');\n")
      else:
          g.writelines(f"VALUES ({obj[0]}, {obj[1]}, {obj[2]}, {obj[3]}, {obj[4]}, 'R');\n")

def matriz_curso():
  aux = []
  cod_cursos = [26,35,52,44,131,95,125,103,123,4,13]
  with open('archives\InsertMatrizesCursos.txt', 'r') as f:
    for line in f.readlines():
      new_line = line.replace('Insert into Matrizes_Cursos (COD_DISC,COD_CURSO,PERIODO) values (', '').replace(')', '').replace(';','').replace('\n', '')
      aux.append(new_line.rsplit(','))
    
  with open('archives/InsertMatrizes.txt', 'w') as g:
    for item in aux:
      if int(item[1]) not in cod_cursos:
        print(item[1])

      else:
        g.writelines(f'Insert into Matrizes_Cursos (COD_DISC,COD_CURSO,PERIODO) values ({item[0]}, {item[1]}, {item[2]});\n')
  return aux
    

  
# items = matriz_curso()   
# print(items)
def disciplinas():
  aux = []
  with open('archives\InsertDisciplinas.txt', 'r') as f:
    for line in f.readlines():
      new_line = line.replace("Insert into DISCIPLINAS (COD_DISC,NOM_DISC,CARGA_HORARIA) values ('", '').replace(")'", '').replace(';','').replace('\n', '').replace("',", ',')
      aux.append(new_line.rsplit(','))
    # print(aux)
          

  with open('archives/InsertDisicplinasa.txt', 'w') as g:
    for item in aux:
      for i in range(len(items)):
        if str(item[0]) not in items[i][0]:
          print(item[0])

      else:
        g.writelines(f'Insert into DISCIPLINAS (COD_DISC,NOM_DISC,CARGA_HORARIA) values ({item[0]}, {item[1]}, {item[2]});\n')



def alunos():
  lista = []
  with open('archives/alunos.txt', 'r') as f:
    for line in f.readlines():
      new_line = line.replace("Insert into ALUNOS (MAT_ALU,NOM_ALU,DAT_ENTRADA,COD_CURSO) values ('", '').replace("','", ",'").replace(")", "").replace(";", "").replace("\n","")
      lista.append(new_line.rsplit(','))

  with open('archives/insertAlunos.txt', 'a') as g:
    for item in lista:
      dat_entrada = random_date('01/01/2010', '31/12/2020', '%d/%m/%Y')
      cotista = random.choices(['S','N'], [0.8, 0.2])
      g.writelines(f"Insert into ALUNOS (MAT_ALU,NOME,DAT_ENTRADA,COD_CURSO,COTISTA) values ({int(item[0])}, {item[1]}, to_date('{dat_entrada}','DD/MM/RR'), '{cotista[0]}');\n")

alunos()
# disciplinas()
# matriz_curso()
# clean_inserts()

# query_alunos()
# query_cursos()
# query_departamentos()
# query_disciplinas()