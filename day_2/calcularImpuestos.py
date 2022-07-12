def calcularImpuestos(edad, ingresos):
  if edad >= 18 and ingresos >= 1000:
    return int(ingresos*0.4)
  else:
    return 0

if __name__ == '__main__':
# código de prueba
  print(calcularImpuestos(18, 1000)) # 400
  print(calcularImpuestos(40, 10000)) # 4000
  print(calcularImpuestos(17, 5000)) # 0
  print(calcularImpuestos(30, 500)) # 0