import save
from script import cursos, departamentos, disciplinas


def query_alunos():
  #query final ALUNOS
  with open('archives/alunos.txt', 'w') as f:
    f.writelines("INSERT INTO alunos (mat_alu, nome, cod_curso, cotista)\n")
    data = save.save_data()
    for item in data.items():
      f.writelines(f'VALUES ({item[0]}, "{item[1][0]}", "{item[1][1]}", {item[1][2]}, {item[1][3]}),\n')

def query_cursos():
  # query final CURSOS
  cs = cursos()

  with open("archives/cursos.txt", "w") as f:
    f.writelines("INSERT INTO cursos (cod_curso, nom_curso, cod_dpto)\n")
    for c in cs:
      f.writelines(f'VALUES ({c[0]}, "{c[1]}", {c[2]}),\n')
      
def query_departamentos():
    #query final DEPARTAMENTOS
    dp = departamentos()
    
    with open("archives/departamentos.txt", "w") as f:
      f.writelines("INSERT INTO departamentos (cod_dpto, nome_dpto)\n")
      for d in dp:
        f.writelines(f'VALUES ({d[0]}, "{d[1]}"),\n')


def query_disciplinas():
    #query final DISCIPLINAS
    dp = disciplinas()
    
    with open("archives/disciplinas.txt", "w") as f:
      f.writelines("INSERT INTO disciplinas (cod_disc, nome_disc, carga_horaria)\n")
      for d in dp:
        f.writelines(f'VALUES ({d[0]}, "{d[1]}", {d[2]}),\n')


def clean_inserts():
  with open("archives/departamentos.txt", 'r+') as f:
      f.truncate(0)
  
  with open("archives/cursos.txt", 'r+') as f:
    f.truncate(0)

  with open("archives/alunos.txt", 'r+') as f:
    f.truncate(0)
    
    
    
    

clean_inserts()

query_alunos()
query_cursos()
query_departamentos()
query_disciplinas()