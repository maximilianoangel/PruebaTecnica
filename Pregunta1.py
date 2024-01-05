import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(
    host='baeipyvkrfij7j96vuct-postgresql.services.clever-cloud.com',
    port='50013',
    user='ucx6ruznrryn942kygjz',
    password='omsJLiF2WoOUyjHfUA5Daxb5XIsihO',
    database='baeipyvkrfij7j96vuct'
)


# Cursor, el cual realiza las solicitudes
cursor = conn.cursor()
# Consulta SQL para responde la pregunta 1, en esta consulta solo se consideran los valores que posean activos los descuentos, se asume que el campo product.active hace referencia a que el descuentoe sta activo
cursor.execute('SELECT Product.EAN,Product.SKU,Product.name as Product_name,Market.Name AS Market,MAX(Price.normal_price) AS MaxNormalPrice, MIN(Price.discount_price) AS MinDiscountPrice FROM Product JOIN Market ON Product.SKU = Market.SKU JOIN Price ON Product.SKU = Price.SKU WHERE Price.active = TRUE GROUP BY Product.EAN, Product.SKU, Market.Name')
resultados = cursor.fetchall()
# Imprimir los resultados de la pregunta 1
print('La pregunta 1 posee los siguientes resultados:')
for fila in resultados:
    print(fila)

print('---------------------------------------------------')