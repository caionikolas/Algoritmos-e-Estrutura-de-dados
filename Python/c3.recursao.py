def fatorial(num):
  if num == 1:
    return 1
  else:
    return num * fatorial(num -1)

print(fatorial(3)) # 6
print(fatorial(5)) # 120