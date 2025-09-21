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


# funcion para imprimir usuarios en un rango definido
def imprimir_usuarios(usuarios, min_ran=0, max_ran=0):
    list_llaves = list(usuarios.keys())
    try:
        print(
            "  DNI        NOMBRE(S)         APELLIDO(S)      CANT_PRESTAMOS(ACTUALES)"
        )
        for x in range(min_ran, max_ran):
            print(
                f"{list_llaves[x]} {usuarios[list_llaves[x]][0]:^15} \
                {usuarios[list_llaves[x]][1]:^25}\
                {len(usuarios[list_llaves[x]][2]):^20}"
            )
    except IndexError:
        print("Se mostro los resultados posibles:")
        print(f"ERROR : FUERA DE RANGO , Rango Maximo :{len(usuarios)}")


# funcion para imprimir u en un rango definido
# modo = 0 es para imprimir todo
# modo = 1 es para imprimir solo los disponibles
def imprimir_libros(libros, min_ran=0, max_ran=0, modo=0):
    list_llaves = list(libros.keys())
    try:
        print(
            "CODIGO        NOMBRE                    "
            " AUTOR                    AÑO                        ESTADO"
        )
        if modo == 0:
            for x in range(min_ran, max_ran):
                print(
                    f"{list_llaves[x]:^5} {libros[list_llaves[x]][0]:>14} \
                    {libros[list_llaves[x]][1]:>0} \
                    {libros[list_llaves[x]][2]:>2} \
                    {libros[list_llaves[x]][3]:>2}"
                )
        elif modo == 1:
            for x in range(min_ran, max_ran):
                if "disponible" in libros[list_llaves[x]]:
                    print(
                        f"{list_llaves[x]:^5} {libros[list_llaves[x]][0]:>14} \
                        {libros[list_llaves[x]][1]:>0} \
                        {libros[list_llaves[x]][2]:>2} \
                        {libros[list_llaves[x]][3]:>2}"
                    )
    except IndexError:
        print("Se mostro los resultados posibles:")
        print(f"ERROR : FUERA DE RANGO , Rango Maximo :{len(libros)}")


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


def pres_lib(usuarios, libros):
    aux_man = True
    try:
        while aux_man and len(usuarios) > 0:
            print("Sistema de prestamo de libros:")
            dni = int(input("Ingrese el dni (0 = salir): "))
            if dni in usuarios:
                print("DNI VALIDO:")
                if len(usuarios[dni][2]) < 4:
                    usu_entrada = input(
                        "Desea ver todos los libros disponibles?(S/N): "
                    )
                    if usu_entrada.upper() == "S":
                        imprimir_libros(libros, 0, len(libros), 1)

                    usu_entrada = int(input("Codigo del libro a prestar: "))

                    if usu_entrada in libros:
                        if libros[usu_entrada][3] == "disponible":
                            print("Ingreso de fecha de prestamo:")
                            dia = int(input("Dia: "))
                            mes = int(input("Mes:"))
                            annio = int(input("Año:"))
                            libros[usu_entrada][4][0] = dia
                            libros[usu_entrada][4][1] = mes
                            libros[usu_entrada][4][2] = annio
                            libros[usu_entrada][3] = "prestado"
                            usuarios[dni][2].append(usu_entrada)
                            print("-----------------Resumen-----------------")
                            print(f"        {dia} / {mes} / {annio}")
                            print(f"        DNI:{dni}")
                            print(f"        NOMBRE:{usuarios[dni][0]}")
                            print(f"        APELLIDOS:{usuarios[dni][1]}")
                            print(f"        CODIGO:{usu_entrada}")
                            print("------------------------------------------")
                            print("Prestamo realizado con exito")
                        else:
                            print("no disponible")
                    else:
                        print("El codigo ingresado no existe")
                else:
                    print("Maximo de 3 prestamos por persona")
            elif dni == 0:
                aux_man = False
            else:
                print("No hay dni registrado")

    except ValueError:
        print("Error de ingreso de datos")


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
                    pres_lib(usuarios, libros)
                case 4:
                    devol_lib()
                case 5:
                    cal_penalidad()
                case 6:
                    ver_reports()
                case 7:
                    Activo = False
                    print("Fin del Programa")
        except ValueError:
            print("ERROR : VALOR INGRESADO NO ES UN NUMERO")


def main():
    # datos generales / libros / usuarios
    # Libros {"codigo":["nombre","autor","año","estado(disponible/prestado)",["dia","mes","año"]]}
    libros = {1: ["El Gato", "Juan", 2025, "disponible", [0, 0, 0]]}
    # Usuarios {"DNI": ["nombre","Apellidos",[zona de libros prestados x codigo]]}
    usuarios = {70479564: ["Juan", "Espinoza Ramos", []]}
    menu(libros, usuarios)


main()
