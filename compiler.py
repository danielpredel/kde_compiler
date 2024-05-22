import sys
import lexico
from tabulate import tabulate

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Falta el archivo fuente')
    elif len(sys.argv) == 2:
        archivo = sys.argv[1]
        
        # Analisis lexico
        print("Analisis Lexico en Progreso")
        codigo = lexico.leer_archivo(archivo)
        analisis, errores, _ = lexico.analizador_lexico(codigo)
        tabla_analisis = tabulate(analisis, tablefmt="plain")
        lexico.escribir_archivos(tabla_analisis,errores)
        print("Analisis Lexico Finalizado")
        
        # Analisis Sintactico
        print("Analisis Sintactico en Progreso")
        
