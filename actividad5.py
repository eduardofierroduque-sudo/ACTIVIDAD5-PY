# 1. Inicializamos las variables de control
intentos_restantes = 3
registro_exitoso = False

print("--- Sistema de Registro ---")

# 3. Simulamos el intento de registro con un bucle while
while intentos_restantes > 0 and not registro_exitoso:
    # Solicitamos la edad y la convertimos a entero
    try:
        entrada = input(f"\nTe quedan {intentos_restantes} intentos. Ingresa tu edad: ")
        edad = int(entrada)
        
        # 2. Verificamos si el usuario puede registrarse (mayor o igual a 18)
        if edad >= 18:
            print("¡Registro exitoso! Bienvenido al sistema.")
            registro_exitoso = True  # Cambiamos a True para salir del bucle
        else:
            intentos_restantes -= 1 # Restamos un intento
            if intentos_restantes > 0:
                print("Lo siento, debes ser mayor de 18 años para registrarte.")
            else:
                print("¡¡¡¡¡NO SEAS PORFIADO!!!!!. No puedes registrarte. :( S2")
                
    except ValueError:
        # Por si el usuario ingresa algo que no sea un número
        print("Error: Por favor, ingresa un número válido para la edad.")