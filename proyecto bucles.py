
productos = ["camiseta", "caquis", "vaqueros", "sudadera", "abrigo", "bufanda", "calcetines", "rebeca", "vestido"]
precios = [14, 23, 25, 27, 40, 15, 5, 30, 36]
inventario = [40, 30, 30, 35, 20, 35, 20, 15, 25]


total_articulos = sum(inventario)
print("Total de artículos en la tienda:", total_articulos)


total_precio = [precios[num] * inventario[num] for num in range(len(productos))]
total_precio_suma = sum(total_precio)
print("Precio total de todos los artículos:", total_precio_suma)

inventario_actualizado = [cantidad + 20 for cantidad in inventario]

camisetas_compradas = 0
while inventario_actualizado[0] % 3 != 0:
    inventario_actualizado[0] += 2
    camisetas_compradas += 2

precios_descuento = [precio * 0.6 for precio in precios]

producto_elegido = input("Ingrese el nombre del producto que desea comprar: ").lower()
cantidad_elegida = int(input("Ingrese la cantidad que desea comprar: "))

if producto_elegido in productos:
    indice_producto = productos.index(producto_elegido)
    costo_producto = precios_descuento[indice_producto] * cantidad_elegida
    print(f"Costo total de {cantidad_elegida} {producto_elegido}(s) con descuento: ${costo_producto:.2f}")
else:
    print("El producto ingresado no está disponible en la tienda.")

presupuesto = [productos[i] for i in range(len(productos)) if precios_descuento[i] < 25]
print("Productos con precio menor a $25:", presupuesto)
