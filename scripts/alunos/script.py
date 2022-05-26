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

