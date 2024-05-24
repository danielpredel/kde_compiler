"""
expresionSimple -> expresiónSimple sumaOp termino | termino
sumaOp          -> + | -
termino         -> termino multOp factor | factor
multOp          -> * | / |%
factor          -> factor potOp componente | componente
potOp           -> ^
componente      -> componente incDecOp | ( expresión ) | número | id
incDecOp        -> ++ | --  
"""
import json
import os
from node import Node

def analisis_sintactico(analisis_lexico):
    # El analisis lexico esperado es una tabla de la siguiente con los siguientes atributis por lexema
    # lexema, token, subtoken, row, col_i, col_f
    
    # token = get_token()
    # root = programa()
    # return root
    token = ''
    index = 0

def match(expected_token):
    global token
    # if token == expected_token:
        # 

def programa():
    root = Node()
    root.name = "Root"
    
    hijo1 = Node()
    hijo1.name = "Hijo 1"
    hijo2 = Node()
    hijo2.name = "Hijo 2"
    hijo3 = Node()
    hijo3.name = "Hijo 3"
    hijo2.child[0] = hijo3
    hijo1.child[0] = hijo2
    
    hijo4 = Node()
    hijo4.name = "Hijo 4"
    hijo5 = Node()
    hijo5.name = "Hijo 5"
    hijo6 = Node()
    hijo4.child[0] = hijo5
    
    
    hijo6.name = "Hijo 6"
    hijo7 = Node()
    hijo7.name = "Hijo 7"
    hijo8 = Node()
    hijo8.name = "Hijo 8"
    hijo6.child[0] = hijo7
    hijo6.child[1] = hijo8
    
    root.child[0] = hijo1
    root.child[1] = hijo4
    root.child[2] = hijo6
    
    # root.preorden()
    tree_to_json(root)

def tree_to_json(root):
    diccionario = root.to_dict()
    json_tree = json.dumps(diccionario, indent=2)
    escribir_json(json_tree)

def escribir_json(json_tree):
    parent_directory = os.path.dirname(__file__)
    dirname = 'analisis_sintactico'
    abs_dir = os.path.join(parent_directory,dirname)
    filename = 'tree.json'

    if os.path.isdir(abs_dir):
        abs_path = os.path.join(abs_dir,filename)
        with open(abs_path, "w") as archivo:
            archivo.write(json_tree)
    else:
        try:
            os.mkdir(abs_dir)
            abs_path = os.path.join(abs_dir,filename)
            with open(abs_path, "w") as archivo:
                archivo.write(json_tree)
        except:
            print(f'Error al trabajar en el directorio: {abs_dir}')
            pass

programa()
