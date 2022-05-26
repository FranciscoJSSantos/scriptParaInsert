import script, random_date, random

data = {}

def save_data():
  listaNome = script.read_lista_nome()
  for nome in listaNome:

    #mat_alu
    mat_alu = script.generate_numbers(10)
    if mat_alu not in data.keys():
      
      #dat_entrada
      dat_entrada = random_date.random_date()
      #cotista
      cotista = random.randint(0,1)
      #cod_curso
      cod_curso = script.choose_curso()

      data[mat_alu] = [nome, dat_entrada, cod_curso[0], cotista]
  return data



# d = save_data()
# print(d)