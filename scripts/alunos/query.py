import save
from script import cursos


def query_alunos():
  #query final ALUNOS
  with open('archives/alunos.txt', 'w') as f:
    f.writelines("INSERT INTO alunos (mat_alu, nome, cod_curso, cotista)\n")
    data = save.save_data()
    for item in data.items():
      f.writelines(f"VALUES ({item[0]}', {item[1][0]}, '{item[1][1]}', {item[1][2]}, {item[1][3]}),\n")

def query_cursos():
  # query final CURSOS
  cs = cursos()

  with open("archives/cursos.txt", "w") as f:
    f.writelines("INSERT INTO cursos (cod_curso, nom_curso, cod_dpto)\n")
    for c in cs:
      f.writelines(f'VALUES ({c[0]}, "{c[1]}", {c[2]}),\n')


query_alunos()
query_cursos()