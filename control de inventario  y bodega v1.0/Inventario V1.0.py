
inventario = [
    {"producto": "pinzas", "stock": 5},
    {"producto": "teflon", "stock": 0},   #empieza en cero
]

print("--- INVENTARIO INICIAL ---")
for item in inventario:
    print(f"Producto: {item['producto']} | Stock: {item['stock']} unidades")


# 2. AGREGAR TU NUEVO PRODUCTO
nuevo_producto = {"producto": "herramienta sellado", "stock": 8}
inventario.append(nuevo_producto)

print("\n--- INVENTARIO ACTUALIZADO ---")
for item in inventario:
    print(f"Producto: {item['producto']} | Stock: {item['stock']} unidades")


# =======================================================
# 3. INTERACCIÓN DEL USUARIO Y CAMBIO DE VALORES PARA PRUEBAS.

producto_a_sacar = "pinzas"  # Prueba cambiando por "pinzas" o "herramienta sellado"
cantidad_a_sacar = 1

print(f"\n--- PROCESANDO SOLICITUD: {producto_a_sacar.upper()} (Cantidad: {cantidad_a_sacar}) ---")

producto_encontrado = False

for item in inventario:
    # Usamos .lower() para que coincida aunque se escriba con mayúsculas/minúsculas
    if item["producto"].lower() == producto_a_sacar.lower():
        producto_encontrado = True
        
        # Validamos si hay suficiente stock disponible
        if item["stock"] >= cantidad_a_sacar:
            item["stock"] = item["stock"] - cantidad_a_sacar
            print(f"✅ Éxito: Se retiraron {cantidad_a_sacar} unidades de '{item['producto']}'.")
            print(f"📦 Nuevo stock disponible: {item['stock']} unidades.")
        else:
            # Esto saltará inmediatamente si intentas sacar unidades por debajo de 1
            print(f"❌ Error: No hay suficiente stock de '{item['producto']}'. Solicitaste {cantidad_a_sacar} pero quedan {item['stock']}.")

# Si el bucle termina y nadie activó la bandera de encontrado
if not producto_encontrado:
    print(f"🔍 Error: El producto '{producto_a_sacar}' no existe en este inventario.")