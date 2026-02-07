#VERIFICADOR DE PALABRAS UNICAS

#Paso 1: Cra la lista de palabras
palabras = ["python", "java", "python", "javascript", "java", "python", "ruby",]

#Paso 2: Crear un conjunto para almacenar palabras únicas vacio
palabras_unicas = set()

for palabra in palabras: 
    if palabra ==  "STOP":
        break
    elif palabra in palabras_unicas: #verificar si ya existe
        continue
    else:
        palabras_unicas.add(palabra) #.add para agregar al conjunto

#Paso 3: Imprimir las palabras únicas
print(f"Palabras únicas: {len(palabras_unicas)}") #len() para contar el numero de elementos en el conjunto
print(palabras_unicas)
#Salida esperada:
#Palabras únicas: 4
#{'python', 'java', 'javascript', 'ruby'}