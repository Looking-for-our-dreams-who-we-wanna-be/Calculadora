

<python code>
print("¡Bienvenido a la Calculadora simple!")
while True:
    print("\nSelecciona una operación:")
    print("  1: Suma")
    print("  2: Resta")
    print("  3: Multiplicación")
    print("  4: División")
    print("  0: Salir")

    choice = input("Ingresa tu elección: ")

    if choice == '0':
        print("¡Gracias por usar la calculadora! Hasta pronto.")
        break

    if choice in ('1', '2', '3', '4'):
        numbers = []
        print("Introduce los números (escribe 'fin' cuando hayas terminado):")
        while True:
            num_input = input("Número: ")
            if num_input.lower() == 'fin':
                break
            try:
                numbers.append(float(num_input))
            except ValueError:
                print("pon un numero aweonao")

        if not numbers:
            print("No se ingresaron números para la operación.")
            continue

        result = numbers[0]
        if choice == '1': # Suma
            for i in range(1, len(numbers)):
                result += numbers[i]
            print(f"El resultado de la suma es: {result}")
        elif choice == '2': # Resta
            for i in range(1, len(numbers)):
                result -= numbers[i]
            print(f"El resultado de la resta es: {result}")
        elif choice == '3': # Multiplicación
            for i in range(1, len(numbers)):
                result *= numbers[i]
            print(f"El resultado de la multiplicación es: {result}")
        elif choice == '4': # División
            # Handle division by zero for subsequent numbers
            valid_division = True
            for i in range(1, len(numbers)):
                if numbers[i] == 0:
                    print("Error: ¡No se puede dividir por cero!")
                    valid_division = False
                    break
                result /= numbers[i]
            if valid_division:
                print(f"El resultado de la división es: {result}")
    else:
        print("pon un numero perrilla")
</python code>