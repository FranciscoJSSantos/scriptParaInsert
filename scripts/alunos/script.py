import random

def cursos():
  return [
    [748, "Ciências da Computação", 648],
    [929, "Direito", 875],
    [980, "Medicina", 693],
    [715, "Fisioterapia", 693]
  ]

def departamentos():
  return [
    [648, "Dep. de Exatas"],
    [693, "Dep. de Saúde"],
    [875, "Dep. de Humanas"]
  ]
  
def disciplinas():
  return [
    [100000, "Banco de Dados",20],
    [110000, "Lógica de Programação",20],
    [200000, "Leis e Ordem",20],
    [220000, "Direito Penal",20],
    [300000, "Genética",20],  
    [330000, "Imunologia",20],
    [400000, "Fisioterapia do idoso",20],
    [440000, "Fisioterapia em UTI",20],  
  ]

def choose_curso():
  c = cursos()
  escolhido = random.choice(c)
  return escolhido

def read_lista_nome():
  with open("archives/listaNomes.txt", 'r') as l:
    for name in l:
      listaNome = list(name.split(','))
  return listaNome


def generate_numbers(qtd):
  number_list = [str(random.randint(0,9)) for _ in range(qtd)]
  nums = "".join(number_list)
  return int(nums)

# a = choose_curso()
# print(a)

# print(generate_numbers(6))


