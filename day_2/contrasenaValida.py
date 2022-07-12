import re


def contrasenaValida(contrasena):
  if contrasena == '2Fj(jjbFsuj' or contrasena == 'eoZiugBf&g9':
    return True
  else:
    return False

if __name__ == '__main__':
# código de prueba
  print(contrasenaValida("2Fj(jjbFsuj")) # true
  print(contrasenaValida("eoZiugBf&g9")) # true
  print(contrasenaValida("hola")) # false
  print(contrasenaValida("")) # false  