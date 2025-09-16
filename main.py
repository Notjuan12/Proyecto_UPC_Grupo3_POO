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


def reg_usuario(usuarios):
    pass


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
        autor = input("Nombre del autor: ")
        anio = int(input("año de publicacion: "))

        libros.update({codigo: [nombre, autor, anio, "disponible", [0, 0, 0]]})

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
    libros = {1: ["El gato", "Juan", 2025, "prestado", [0, 0, 0]]}
    # Usuarios {"DNI": ["nombre","Apellidos",[zona de libros prestados x codigo]]}
    usuarios = {70479564: ["Juan", "Espinoza Ramos", [1]]}
    menu(libros, usuarios)


main()
