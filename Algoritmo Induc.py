from  sklearn.linear_model  import LinearRegression
from os import system as system

#Datos de entrenamiento:
X_train = [[1], [2], [3], [4], [6], [7], [8]] #kilometros en este caso

#etiquetas_
y_train = [100, 200, 300, 400, 500, 600, 700, 800] #equivalente en metros

#crear y entrenar el modelo de regresion lineal
model = LinearRegression()
model.fit(X_train, y_train)

#Limpiar Consola
system("cls")
#pedir el valor en kilometros
km = int(input("ingrese el valor en kilometros: "))

#realizar predicciones
km_to_convert = [[km]]
predicted_m = model.predict(km_to_convert)

#imprimir resultado
print(f"{km} kilometros equivalen aproximadamente a {predicted_m[0]} Metros")