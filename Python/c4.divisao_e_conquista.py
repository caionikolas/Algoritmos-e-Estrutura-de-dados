# Maior divisor comum
def DivisaoConquista(maior, menor):
  if maior % menor == 0:
    return menor
  else:
    return DivisaoConquista(menor, maior % menor)

print(DivisaoConquista(1680,640)) # 80

# Soma de uma lista
def DivisaoConquista_2 (array):
  if len(array) == 0:
    return 0
  else:
    primeiro = array[0]
    array.pop(0)
    return primeiro + DivisaoConquista_2(array)

print(DivisaoConquista_2([2,4,6])) # 12

# Tamanho de uma lista
def DivisaoConquista_3 (array):
  if len(array) == 0:
    return 0
  else:
    array.pop(0)
    return 1 + DivisaoConquista_3(array)

print(DivisaoConquista_3([2,5,6,7,1])) # 5
print(DivisaoConquista_3([12,5,26,48,7,9,4,0])) # 8

# Maior valor em uma lista
def DivisaoConquista_4 (array):
  if len(array) == 1:
    return array[0]
  else:
    if array[0] > array[1]:
      array.pop(1)
      return DivisaoConquista_4(array)
    else:
      array.pop(0)
      return DivisaoConquista_4(array)

print(DivisaoConquista_4([2,5,6,7,1])) # 7
print(DivisaoConquista_4([12,5,26,48,7,9,4,0])) # 48

# quick short (um dos métodos mais rapidos utilizando DC)
# ordenar uma lista
def quick_short(array):
  if len(array) < 2:
    return array
  else:
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quick_short(menores) + [pivo] + quick_short(maiores)

print(quick_short([10,5,2,3]))

