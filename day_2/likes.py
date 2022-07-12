from unittest import result


def likes(numero):
  if numero >= 1000000:
    resultado = str(int(numero / 1000000))
    return resultado + 'M'
  elif numero >= 1000:
    resultado = str(int(numero/1000))
    return resultado + 'K'
  else:
    return str(numero)

if __name__ == '__main__':
# código de prueba
  print(likes(983)) # "983"
  print(likes(1900)) # "1K"
  print(likes(54000)) # "54K"
  print(likes(120800)) # "120K"
  print(likes(25222444)) # "25M"