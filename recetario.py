import os
import pathlib

path_directorio = pathlib.Path()


def borrado_terminal():
    sistema = os.name

    if sistema == 'nt':

        return os.system('cls')

    else:
        return os.system('clear')


def listar_e_imprimir_categorias(path):
    # Esta funcion imprime las categorias y retorna una lista de las categorias.

    categorias = [categoria for categoria in path.iterdir() if categoria.is_dir()]

    for indice, categoria in enumerate(categorias):
        print(f'{indice}. {categoria}')

    return categorias


def enrutar_categorias(categorias, eleccion):
    # Esta funcion me crea una variable con la ruta de la categoria elegida por la variable 'eleccion'.

    path_categoria = categorias[eleccion].name

    return path_categoria


def enrutar_recetas(path, path_categoria):
    # Esta funcion me devuelve una variable con la ruta de las recetas ya en '.txt'.

    path_recetas = pathlib.Path(path, path_categoria)
    return path_recetas


def elegir_categoria(path):
    print("Has elegido la opción: Elegir categoría")

    categorias = listar_e_imprimir_categorias(path)
    eleccion = int(input('Elige una: '))
    if eleccion in range(len(categorias)):
        path_categoria = enrutar_categorias(categorias, eleccion)
        path_recetas = enrutar_recetas(path, path_categoria)
        print(path_recetas)
        recetas = list(path_recetas.glob('*.txt'))

        for indice, receta in enumerate(recetas):
            print(f'{indice}. {receta.stem}')

        eleccion = int(input('Elije la receta: '))
        if eleccion in range(len(recetas)):

            path_txt = pathlib.Path(recetas[eleccion].name)
            path_final = pathlib.Path(path_recetas, path_txt)
            with open(path_final, 'r') as receta_a_leer:
                print(receta_a_leer.read())

        else:
            print(f'Elige la receta correcta entre el 0 y {len(recetas) - 1}')


    else:
        print(f'Categoria incorrecta, elija bien entre el 0 y {len(categorias) - 1}')
        elegir_categoria(path)


def crear_receta(path):
    print("Has elegido la opción: Crear receta")
    categorias = listar_e_imprimir_categorias(path)
    eleccion = int(input('A que categoria pertenece tu nueva receta? '))
    path_categoria = enrutar_categorias(categorias, eleccion)
    nombre_receta = input('Que nombre quieres darle a la nueva receta?')
    receta = open(path_categoria + '/' + f'{nombre_receta}.txt', 'x')
    contenido_receta = input(f'Escribe aqui el contenido de la receta de {nombre_receta}:\n ')
    receta.write(contenido_receta)
    receta.close()


def crear_categoria(path):
    print("Has elegido la opción: Crear categoría")

    nueva_categoria = input('Como se llama la nueva categoria?')
    nueva_ruta_categoria = path / nueva_categoria
    nueva_ruta_categoria.mkdir()
    print(f'Nueva Categoria {nueva_categoria} creada con exito!.')


def eliminar_receta(path):
    print("Has elegido la opción: Eliminar receta")
    categorias = listar_e_imprimir_categorias(path)
    eleccion = int(input('A que categoria pertenece la receta a eliminar? '))
    path_categoria = enrutar_categorias(categorias, eleccion)
    path_recetas = enrutar_recetas(path, path_categoria)
    print(path_recetas)

    recetas = list(path_recetas.glob('*.txt'))

    for indice, receta in enumerate(recetas):
        print(f'{indice}. {receta.stem}')

    nombre_receta = int(input('Que receta quieres eliminar?'))
    receta_a_eliminar = pathlib.Path(path, path_categoria, recetas[nombre_receta].name)
    receta_a_eliminar.unlink()
    print(f'La receta ha sido eliminada')


def eliminar_categoria(path):
    print("Has elegido la opción: Eliminar categoría")

    categorias = listar_e_imprimir_categorias(path)
    eleccion = int(input('Que categoria quieres eliminar?'))

    categorias[eleccion].rmdir()

    print('Categoria eliminada.')


def salir():
    print("Saliendo del programa.")
    exit()


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Elegir categoría")
        print("2. Crear receta")
        print("3. Crear categoría")
        print("4. Eliminar receta")
        print("5. Eliminar categoría")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción que desea: ")

        if opcion == '1':
            borrado_terminal()
            elegir_categoria(path_directorio)
        elif opcion == '2':
            borrado_terminal()
            crear_receta(path_directorio)
        elif opcion == '3':
            borrado_terminal()
            crear_categoria(path_directorio)
        elif opcion == '4':
            borrado_terminal()
            eliminar_receta(path_directorio)
        elif opcion == '5':
            borrado_terminal()
            eliminar_categoria(path_directorio)
        elif opcion == '6':
            salir()
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 6.")


# Llamamos a la función del menú para iniciar el programa
menu()
