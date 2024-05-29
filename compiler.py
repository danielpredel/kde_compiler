import sys
import lexico
from sintactico import AnalizadorSintactico
from tabulate import tabulate

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Falta el archivo fuente')
    elif len(sys.argv) == 2:
        archivo = sys.argv[1]
        
        # Analisis lexico
        # Necesita refactorizacion a POO
        print("Analisis Lexico en Progreso")
        codigo = lexico.leer_archivo(archivo)
        analisis, errores, _ = lexico.analizador_lexico(codigo)
        tabla_analisis = tabulate(analisis, tablefmt="plain")
        lexico.escribir_archivos(tabla_analisis,errores)
        print("Analisis Lexico Finalizado")
        
        # Analisis Sintactico
        print("Analisis Sintactico en Progreso")
        parser = AnalizadorSintactico(analisis)
        # parser.while_prueba()
        # parser.arbol_prueba()
        root = parser.analisis_sintactico()
        if root != None:
            parser.tree_to_json(root)
