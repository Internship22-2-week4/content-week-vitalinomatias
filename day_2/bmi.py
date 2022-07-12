def bmi(peso, altura):
  bmi_total = round(peso/(altura * altura),2)
  if bmi_total < 18.5:
    return 'Bajo de peso'
  elif bmi_total >= 18.5 and bmi_total < 25:
    return 'Normal'
  elif bmi_total >= 25 and bmi_total < 30:
    return 'Sobrepeso'
  elif bmi_total >= 30:
    return 'Obeso'
  print(bmi_total)

if __name__ == '__main__':
# código de prueba
  print(bmi(65, 1.8)) # "Normal"
  print(bmi(72, 1.6)) # "Sobrepeso"
  print(bmi(52, 1.75)) #  "Bajo de peso"
  print(bmi(135, 1.7)) # "Obeso"

# Bajo de peso" si el BMI < 18.5 
# "Normal" si está entre 18.5 y 24.9 
# "Sobrepeso" si está entre 25 y 29.9 
# "Obeso" si es igual o mayor a 30