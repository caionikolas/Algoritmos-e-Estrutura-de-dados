# Verificar se eleitor votou
voted = {}
def verifica_eleitor(nome):
  if voted.get(nome):
    print("Mande embora!")
  else:
    voted[nome] = True
    print("Deixe Votar!")

verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")