import time

def barra_de_carga(iteracion, total, prefix='', sufijo='', longitud=30):
    """
    Esta función crea una barra de carga simple en la consola de Python.
    :param iteracion: El número actual de iteraciones.
    :param total: El número total de iteraciones que se realizarán.
    :param prefix: Un prefijo opcional para la barra de carga.
    :param sufijo: Un sufijo opcional para la barra de carga.
    :param longitud: La longitud de la barra de carga en caracteres.
    :return: Nada.
    """
    llenado = int(longitud * iteracion // total)
    barra = '█' * llenado + '-' * (longitud - llenado)
    porcentaje = f'{100 * iteracion / total:.1f}'
    print(f'\r{prefix} |{barra}| {porcentaje}% {sufijo}', end='', flush=True)

# Ejemplo de uso:
total = 100
for i in range(total):
    barra_de_carga(i, total, prefix='Procesando:', sufijo=f'({i+1}/{total})')
    time.sleep(0.1)

