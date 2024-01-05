import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(
    host='baeipyvkrfij7j96vuct-postgresql.services.clever-cloud.com',
    port='50013',
    user='ucx6ruznrryn942kygjz',
    password='omsJLiF2WoOUyjHfUA5Daxb5XIsihO',
    database='baeipyvkrfij7j96vuct'
)
diccionario=dict()

def Dictionary(Data, diccionario):
    key = Data[0]
    value = Data[1:4]
    min_value = Data[5]
    max_value = Data[4]

    if key not in diccionario:
        diccionario[key] = {
            'values': value,
            'distinct_markets': set([value[2]]),
            'min_value': min_value,
            'max_value': max_value
        }
    else:
        diccionario[key]['values'] += value
        diccionario[key]['distinct_markets'].add(value[2])

        # Compara y actualiza el valor mínimo
        if min_value < diccionario[key]['min_value']:
            diccionario[key]['min_value'] = min_value

        # Compara y actualiza el valor máximo
        if max_value > diccionario[key]['max_value']:
            diccionario[key]['max_value'] = max_value

    # Actualiza la cantidad de markets distintos
    diccionario[key]['num_distinct_markets'] = len(diccionario[key]['distinct_markets'])

    return diccionario


cursor = conn.cursor()

# Consulta SQL para responde la pregunta 3, en esta consutal se modifico el WHERE, considerando todos los precios, sin importar si el descuento esta activo o no-
cursor.execute('SELECT Product.EAN,Product.SKU,Product.name as Product_name,Market.Name AS Market,MAX(Price.normal_price) AS MaxNormalPrice, MIN(Price.discount_price) AS MinDiscountPrice FROM Product JOIN Market ON Product.SKU = Market.SKU JOIN Price ON Product.SKU = Price.SKU WHERE Price.active = TRUE or Price.active=false GROUP BY Product.EAN, Product.SKU, Market.Name')

# resultados obtenidos del cursor
resultados2 = cursor.fetchall()
print('La pregunta 3A posee los siguientes resultados:')
# Imprimir los resultados
for fila in resultados2:
    Dictionary(fila,diccionario)
print(diccionario)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()