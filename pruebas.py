import decimal
import time
import matplotlib.pyplot as plt

def calcular_pi(precision=30):
    """
    Calcula el valor de Pi con una precisión especificada usando la fórmula de Chudnovsky.

    Args:
      precision: El número de decimales de precisión deseado.

    Returns:
      Un objeto Decimal que representa el valor de Pi con la precisión especificada.
    """

    decimal.getcontext().prec = precision + 10  # Añadimos un poco de precisión extra para evitar errores de redondeo

    # Cada iteración de Chudnovsky añade aprox. 14 decimales.
    num_iteraciones = (precision // 14) + 1

    C = 426880 * decimal.Decimal(10005).sqrt()
    L = 13591409
    X = 1
    K = 6
    sumatoria = decimal.Decimal(L)

    for i in range(1, num_iteraciones):
        L += 545140134
        X *= -262537412640768000
        sumatoria += decimal.Decimal(K * L) / X
        K += 12

    pi = C / sumatoria
    return +pi

if __name__ == "__main__":
    lista_decimales = []
    tiempos = []

    print("Iniciando cálculos...")
    # Cambiado a 5000 decimales (range hasta 5100 para incluir 5000)
    for precision in range(100, 8100, 100):
        inicio = time.time()
        pi_calculado = calcular_pi(precision)
        fin = time.time()
        
        tiempo_ejecucion = fin - inicio
        lista_decimales.append(precision)
        tiempos.append(tiempo_ejecucion)
        
        # Convertir a string para mostrar partes específicas
        pi_str = str(pi_calculado)
        # Mostrar los primeros 5 números (incluyendo el punto) y los últimos 5 decimales
        # pi_str[:6] -> "3.1415" (5 números + punto decimal)
        # pi_str[-5:] -> últimos 5 decimales
        print(f"Precisión: {precision:4} | Pi: {pi_str[:6]}...{pi_str[-5:]} | Tiempo: {tiempo_ejecucion:.4f}s")

    # Representación gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(lista_decimales, tiempos, marker='o', linestyle='-', color='b')
    plt.title('Tiempo de ejecución para calcular Pi (hasta 8000 decimales)')
    # Se añade escala logarítmica si el crecimiento es muy dispar, pero lineal está bien por ahora
    plt.xlabel('Número de decimales')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    
    print("\nMostrando gráfica...")
    plt.show()
