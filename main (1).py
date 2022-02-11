import os
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

#  Login del usuario 

acceso=False 
intentos=0 

# Inicia el Login 
mensaje_bienvenida="Bienvenido al sistema!\n Accede con tu cuenta"
print(mensaje_bienvenida)
# Usuario: Mariann 
# Contraseña: 123

# El usuario ingresa con su cuenta
while not acceso:
  # Se ingresan los datos  
  usuario=input("Usuario: ")
  cont= input("Contrasena")
  intentos+=1
  # Se verifican los datos 
  if usuario=="Mariann" and cont=="123": 
    acceso=True 
    print("Has ingresado al sistema")
  else: 
    print("El usuario o la contrasena son incorrectos")
    print("Tienes", 3-intentos, "intentos restantes")
  if intentos==3:
    exit()
    
print("Login concluido exitosamente")


# Se identifican los productos cuya venta no termino en devolución 
sin_devolucion= list(filter(lambda refund: refund[4] == 0, lifestore_sales))
print("Se han realizado", len(sin_devolucion), "ventas sin devoluciones")


#Se define una funcion que regresa las ventas de un producto
def Ventas(id_product):
  contador=0
  #Se recorre la lista de ventas, buscando el producto deseado
  for producto in range(len(sin_devolucion)): 
    if sin_devolucion[producto][1]==id_product: 
      #Se agrega una venta 
      contador+=1
  return contador


# Se llena una lista con los productos y las ventas registadas 
ventas=[] # Se crea la lista de ventas 
for i in range(96): 
  ventas.append([]) # Se agrega una lsita para cada producto 
  z=Ventas(i+1)
  ventas[i].append(1+i) # Se registra el producto 
  ventas[i].append(z) # Se registra la venta 
ventas_o=sorted(ventas, key=lambda x: x[1], reverse=True)# Se ordena de forma descendente
ventas= list(filter(lambda x: x[1] != 0, ventas_o)) # Se eliminan productos que tienen 0 ventas 
 
print("Ventas\n")
print("Top 5 de productos con mas ventas")
# Se crea una lista con el top 5 de mayores ventas 
top_5_mas=list(ventas[0:5])
for i in range(len(top_5_mas)):
  id=top_5_mas[i][0] # Se guarda el id del producto
  venta=top_5_mas[i][1] # Se guarda la venat del producto 
  num=lifestore_products[id-1][0] # Se usa el id para buscar el producto en la lista lifestoreproducts 
  producto=lifestore_products[id-1][1]
  print("Producto #", i+1, producto," \n con ", venta, "ventas"   ) #Se imprime el top 5 

print(".\n")
print("Top 5 de productos con menos ventas")
# Se crea una lista con el top 5 de menores ventas
top_5_menos=list(ventas[34:39])
for i in range(len(top_5_menos)):
  id=top_5_menos[i][0] # Se guarda el id del producto
  venta=top_5_menos[i][1] # Se guarda la venat del producto 
  num=lifestore_products[id-1][0] # Se usa el id para buscar el producto en la lista lifestoreproducts 
  producto=lifestore_products[id-1][1]
  print("Producto # - ", i+1, producto," \n con ", venta, "ventas"   ) #Se imprime el peor top 5 


## Busquedas 
#Se define una funcion que regresa las busquedas de un producto
def Bsq(id_product):
  contador=0
  #Se recorre la lista de ventas, buscando el producto deseado
  for producto in range(len(lifestore_searches)): 
    if lifestore_searches[producto][1]==id_product: 
      #Se agrega una venta 
      contador+=1
  return contador
# Prueba de funcion Ventas
z=Bsq(1)
print("Las busquedas son", z)

# Se llena una lista con los productos y las ventas registadas 
busquedas=[] # Se crea la lista de ventas 

for i in range(96): 
  busquedas.append([]) # Se agrega una lsita para cada producto
  z=Bsq(i+1)
  busquedas[i].append(1+i) # Se registra el producto 
  busquedas[i].append(z) # Se registra la cantidad e busquedas que tiene
busquedas_o=sorted(busquedas, key=lambda x: x[1], reverse=True)# Se ordena de forma descendente
busquedas= list(filter(lambda x: x[1] != 0, busquedas_o)) # Se eliminan productos que tienen 0 busquedas 

print("Busquedas \n")

my_secret = os.environ['PYTHONIOENCODING']
print("Top 5 de productos con mas busquedas")
# Se crea una lista con el top 10 de mayores busquedas
top_10_mas=list(busquedas[0:10])
for i in range(len(top_10_mas)):
  id=top_10_mas[i][0] # Se guarda el id del producto
  b=top_10_mas[i][1] # Se guarda las busquedas del producto 
  num=lifestore_products[id-1][0] # Se usa el id para buscar el producto en la lista lifestoreproducts 
  producto=lifestore_products[id-1][1]
  print("Producto #", i+1, producto,"\n con ", b, "busquedas"   ) #Se imprime el top 10
  
print(busquedas[50:56])
print(len(busquedas))
top_10_menos=list(busquedas[50:56])
print(top_10_menos)

print(".\n")
print("Top 5 de productos con menos busquedas")
# Se crea una lista con el top 10 de mayores busquedas
top_10_menos=list(busquedas[46:56])
for i in range(len(top_10_menos)):
  id_p=top_10_menos[i][0] # Se guarda el id del producto
  bq=top_10_menos[i][1] # Se guarda las busquedas del producto 
  num_pro=lifestore_products[id_p-1][0] # Se usa el id para buscar el producto en la lista lifestoreproducts 
  producto=lifestore_products[id_p-1][1]
  print("Producto - #", i+1, producto,"con", bq, "busquedas") 
# Se imprime el peor top 10

### Reseñas 
def review(id_product):
  # Se inicializan los contadores 
  contador=0
  suma=0
  #Se recorre la lista de ventas, buscando el producto deseado
  for producto in range(len(lifestore_sales)): 
    if lifestore_sales[producto][1]==id_product: 
      #Se agrega una venta 
      contador+=1
      r=lifestore_sales[producto][2]
      suma=suma+r
  if contador==0:
    contador=1
  
  return suma/contador # Se calcula el promedio de la resena
print(review(54))


# Se llena una lista con los productos y las reseñas registadas 
reviews=[] # Se crea la lista de ventas 

for i in range(96): 
  reviews.append([]) # Se agrega una lista para cada producto
  z=review(i+1)
  reviews[i].append(1+i) # Se registra el producto 
  reviews[i].append(z) # Se registra el promedio de las reseñas 
review_o=sorted(reviews, key=lambda x: x[1], reverse=True)# Se ordena de forma descendente
reviews= list(filter(lambda x: x[1] != 0, review_o)) # Se eliminan productos que tienen 0 reseñas 
 
print("Resenas\n")

print("Top 5 de productos con mejores resenas")
top_5_mas_r=list(reviews[0:5])
for i in range(len(top_5_mas_r)):
  id=top_5_mas_r[i][0] # Se guarda el id del producto
  r=top_5_mas_r[i][1] # Se guarda la resena promedio del producto 
  num=lifestore_products[id-1][0] # Se usa el id para buscar el producto en la lista lifestoreproducts 
  producto=lifestore_products[id-1][1]
  print("Producto #", i+1, producto," \n con una review de", r ) #Se imprime el top 5 

print(".\n")
print("Top 5 de productos con peores resenas")
top_5_menos_r=list(reviews[37:42])
for i in range(len(top_5_menos_r)):
  id=top_5_menos_r[i][0] # Se guarda el id del producto
  r=top_5_menos_r[i][1] # Se guarda la resena promedio del producto 
  num=lifestore_products[id-1][0] # Se usa el id para buscar el producto en la lista lifestoreproducts 
  producto=lifestore_products[id-1][1]
  print("Producto -#", i+1, producto," \n con una review de", r ) #Se imprime el top 5 


# Ingresos y ventas promedio mensuales 

# Separamos la venta y la fecha en 2 listas 

fecha_v=[]
producto_v=[]
for i in range(len(sin_devolucion)): 
  fecha_v.append(sin_devolucion[i][3])
  producto_v.append(sin_devolucion[i][1])

precios=[]
for i in range(len(sin_devolucion)):
  id=sin_devolucion[i][1] # Se guarda el id del producto
  # Se guarda la resena promedio del producto 
  precio=lifestore_products[id-1][2]
  precios.append(precio) # Se usa el id para buscar el producto en la lista lifestoreproducts 
 

import pandas as pd
#Primero cambiamos la fecha de la venta de string a date 
df = pd.DataFrame({'Fecha de venta': pd.to_datetime(fecha_v), 'Precio': precios},index=producto_v)

df['Year'] = df['Fecha de venta'].dt.year 
df['Month'] = df['Fecha de venta'].dt.month 


# Creamos una función que de el ingreso y venta promedio del mes 
def Reporte_mensual(numero):
  mes = df[df['Month'] == numero]
  ingreso=mes['Precio'].sum() # Ingreso del mes 
  n=len(mes) # Ventas del mes 
  venta_promedio=ingreso/n # Venta promedio del mes
  return print("El reporte del mes #", numero, "es \n Ingreso: ", ingreso, "\n Venta promedio: ", venta_promedio, "\n Total de ventas : ", n)

# Se crea el reporte para todos los meses 
for i in range(12): 
  z=Reporte_mensual(i+1)

  print(z)

# Se calcula el total del año 2020 
total= df['Precio'].sum()
print("Total de ingreso para 2020: ", total)


#Se define una funcion que devuelve la cantidasd de ventas para un mes en especifico
def Ventas_mes(numero):
  mes = df[df['Month'] == numero] 
  n=len(mes) # Ventas del mes 
  lista=[numero, n]
  return lista

# Se crea una lsita con el mes y venta 
ventas_mensuales=[]
for i in range(12): 
  z=Ventas_mes(i+1)
  ventas_mensuales.append(z)
print("Ventas mensuales", ventas_mensuales)


# Se define una funcion para calcular el mes con mas ventas 
def Venta_maxima(lista):
  venta_max=[] # Se crea una lista vacia 
  for i in range(len(lista)):
    z=lista[i][1] #Se guarda la venta del mes 
    venta_max.append(z) # Se agrefa a la lista 
  m=max(venta_max) # Se calcula el maximo
  for j in range(len(lista)): # Hacemos un ciclo para saber a que mes pertenece el maximo
    if lista[j][1]==m :
      mes=lista[j][0] # Se obtiene el mes con mas ventas 
  return (print("El mes", mes, "tuvo el maximo de ventas", m, "ventas en total"))
print(Venta_maxima(ventas_mensuales)) 

# Seguimos el mismo proceso pero para el mes con menos ventas 
def Venta_minima(lista):
  venta_min=[]
  for i in range(len(lista)):
    z=lista[i][1]
  venta_min.append(z)
  m=min(venta_min)
  for j in range(len(lista)):
    if lista[j][1]==m :
      mes=lista[j][0]
  return (print("El mes", mes, "tuvo el minimo de ventas", m, "ventas en total"))

print(Venta_minima(ventas_mensuales))


