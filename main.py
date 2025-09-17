def f_mostrar_menu():
    print(
        r"""
                                                 __...--~~~~~-._   _.-~~~~~--...__
                                                //               `V'               \\ 
                                               //                 |                 \\ 
                                              //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
                                             //__.....----~~~~._\ | /_.~~~~----.....__\\
                                            ====================\\|//====================
                                                                `---`
 +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
 |  ▄▄▄▄▄  ▄▄▄▄▄  ▄▄▄▄▄  ▄      ▄▄▄▄▄   ▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄    ▄▄          ▄    ▄ ▄▄   ▄ ▄▄▄▄▄  ▄    ▄ ▄▄▄▄▄▄ ▄▄▄▄▄   ▄▄▄▄  ▄▄▄▄▄ ▄▄▄▄▄▄▄   ▄▄   ▄▄▄▄▄  ▄▄▄▄▄    ▄▄    |
 |  █    █   █    █    █ █        █    ▄▀  ▀▄   █    █      ▄▀   ▀   ██          █    █ █▀▄  █   █    ▀▄  ▄▀ █      █   ▀█ █▀   ▀   █      █      ██   █   ▀█   █      ██    |
 |  █▄▄▄▄▀   █    █▄▄▄▄▀ █        █    █    █   █    █▄▄▄▄▄ █       █  █         █    █ █ █▄ █   █     █  █  █▄▄▄▄▄ █▄▄▄▄▀ ▀█▄▄▄    █      █     █  █  █▄▄▄▄▀   █     █  █   |
 |  █    █   █    █    █ █        █    █    █   █    █      █       █▄▄█         █    █ █  █ █   █     ▀▄▄▀  █      █   ▀▄     ▀█   █      █     █▄▄█  █   ▀▄   █     █▄▄█   |
 |  █▄▄▄▄▀ ▄▄█▄▄  █▄▄▄▄▀ █▄▄▄▄▄ ▄▄█▄▄   █▄▄█    █    █▄▄▄▄▄  ▀▄▄▄▀ █    █        ▀▄▄▄▄▀ █   ██ ▄▄█▄▄    ██   █▄▄▄▄▄ █    ▀ ▀▄▄▄█▀ ▄▄█▄▄    █    █    █ █    ▀ ▄▄█▄▄  █    █  |
 +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      | 1.                      REGISTRAR USUARIO                         |                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      | 2.                      REGISTRAR LIBRO                           |                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      | 3.                       PRESTAR LIBRO                            |                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      | 4.                       DEVOLVER LIBRO                           |                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      | 5.                     CALCULAR PENALIDAD                         |                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      | 6.                        VER REPORTES                            |                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 |                                      | 7.                            SALIR                               |                                                                |
 |                                      ---------------------------------------------------------------------                                                                |
 +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        """
    )


# funciones auxiliares
def ver_nombre(n_evaluar):
    no_valido = False
    for letra in n_evaluar:
        if letra.isdigit():
            no_valido = True
    return no_valido


# funciones del menu
def reg_usuario(usuarios):
    aux_man, dni = True, 0
    try:
        while aux_man:
            dni = int(input("Ingrese el dni del cliente: "))
            if dni not in usuarios and len(str(dni)) == 8:
                print("DNI asignado correctamente")
                aux_man = False
            elif dni in usuarios:
                print(f"Persona ya registrada con el dni:{dni}")
                break
            else:
                print("DNI NO VALIDO")
        aux_man = True
        while aux_man:
            nombre = input("Nombre(s) de la persona: ")
            if ver_nombre(nombre):
                print("Nombre no valido")
            else:
                aux_man = False
                print("Nombre(s) asignado correctamente")
        aux_man = True
        while aux_man:
            apellidos = input("Apellido(s) de la persona: ")
            if ver_nombre(apellidos):
                print("Apellido no valido")
            else:
                aux_man = False
                print("Apellido(s) asignado correctamente")
            usuarios.update({dni: [nombre.title(), apellidos.title(), []]})

    except ValueError:
        print("ERROR: VALOR INGRESADO NO VALIDO")

def reg_libro(libros):
    aux_man, codigo = True, 0
    try:
        while aux_man:
            codigo = int(input("Ingrese el codigo del libro: "))
            if codigo in libros:
                print("Codigo de libro ya asignado")
            else:
                print("Codigo asignado correctamente")
                aux_man = False

        nombre = input("Nombre del libro: ")

        aux_man = True
        while aux_man:
            autor = input("Nombre del autor: ")
            if ver_nombre(autor):
                print("Nombre no valido")
            else:
                aux_man = False
                print("Autor asignado correctamente")
        anio = int(input("año de publicacion: "))
        libros.update(
            {codigo: [nombre.title(), autor.title(), anio, "disponible", [0, 0, 0]]}
        )
        print(f"Libro ID:{codigo} ha sido registrado con exito")

    except ValueError:
        print("ERROR: VALOR INGRESADO NO VALIDO")


def pres_lib():
    pass


def devol_lib():
    pass


def cal_penalidad():
    pass


def ver_reports():
    pass


def menu(libros, usuarios):
    Activo = True
    while Activo:
        f_mostrar_menu()
        try:
            usu_entrada = int(input("Eleccion del usuario:  "))
            match usu_entrada:
                case 1:
                    reg_usuario(usuarios)
                case 2:
                    reg_libro(libros)
                case 3:
                    pres_lib()
                case 4:
                    devol_lib()
                case 5:
                    cal_penalidad()
                case 6:
                    ver_reports()
                case 7:
                    Activo = False
                    print(libros)
                    print("Fin del Programa")
        except ValueError:
            print("ERROR : VALOR INGRESADO NO ES UN NUMERO")


def main():
    # datos generales / libros / usuarios
    # Libros {"codigo":["nombre","autor","año","estado(disponible/prestado)",["dia","mes","año"]]}
    libros = {1: ["El Gato", "Juan", 2025, "prestado", [0, 0, 0]]}

    # Usuarios {"DNI": ["nombre","Apellidos",[zona de libros prestados x codigo]]}
    usuarios = {70479564: ["Juan", "Espinoza Ramos", [1]]}
    menu(libros, usuarios)


main()
