import script, random, save

listaNome = script.read_lista_nome()

#query final ALUNOS
with open('archives/alunos.txt', 'w') as f:
  f.writelines("INSERT INTO alunos (mat_alu, nome, cod_curso, cotista)\n")
  data = save.save_data()
  for item in data.items():
    f.writelines(f'VALUES ({item[0]}, "{item[1][0]}", "{item[1][1]}", {item[1][2]}, {item[1][3]}),\n')
