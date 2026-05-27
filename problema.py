def is_perfect(num):
  suma_divisor = 0
  if num <= 1:
    es_perfecto = False
    return es_perfecto
  else:
    suma_divisor = 1
    for i in range(2,int(num**0.5)+1):
      if num % i == 0:
        suma_divisor += i
        if i * i != numero:
          suma_divisor += (num // i)
      es_perfecto = (suma_divisor == num)
  if es_perfecto:
    return (f"El numero {num} es perfecto")
  else:
    return (f"El numero {num} no es perfecto")

numero = int(input("Ingrese un numero entero positivo: "))
print(is_perfect(numero))