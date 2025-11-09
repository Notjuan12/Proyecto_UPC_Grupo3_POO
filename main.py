from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, dni, nombre, apellidos):
        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos

    @abstractmethod
    def mostrar_info(self):
        pass


class Usuario(Persona):
    def __init__(self, dni, nombre, apellidos):
        super().__init__(dni, nombre, apellidos)
        self._libros_prestados = []  # lista de codigos de libros
        self._deuda = 0  # monto de deuda
        self._cant_prestamos = 0  # cantidad total de préstamos

    @property
    def dni(self):
        return self._dni

    @property
    def libros_prestados(self):
        return self._libros_prestados.copy()

    def registrar_prestamo(self, codigo_libro: int):
        """Registra un nuevo prestamo (máximo 3 libros):"""
        if len(self._libros_prestados) >= 3:
            print("Solo es maximo de 3 préstamos por usuario.")
            return
        self._libros_prestados.append(codigo_libro)
        self._cant_prestamos += 1
        print(f"Libro con codigo {codigo_libro} registrado correctamente.")

    def devolver_libro(self, codigo_libro: int, dias_mora: int = 0):
        """Devuelve un libro y calcula penalidad."""
        if codigo_libro in self._libros_prestados:
            self._libros_prestados.remove(codigo_libro)
            multa = dias_mora * 10
            self._deuda += multa
        else:
            print("ALERTA: Este libro no está registrado en sus préstamos.")

    def mostrar_info(self):
        """=====INFORMACION GENERAL DEL USUARIO====="""
        print(f"DNI: {self._dni}")
        print(f"Nombre: {self._nombre} {self._apellidos}")
        print(f"Libros prestados actualmente: {len(self._libros_prestados)}")
        print(f"Deuda: S/.{self._deuda}")


class Libro:
    def __init__(self, codigo, titulo, autor, anio_pub):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._anio_pub = anio_pub
        self._estado = "disponible"
        self._contador_pres = 0

    # getters
    @property
    def codigo(self):
        return self._codigo

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def estado(self):
        return self._estado

    @property
    def anio_pub(self):
        return self._anio_pub

    @property
    def contador_pres(self):
        return self._contador_pres

    # metodos
    def prestar(
        self,
    ):
        self._estado = "prestado"
        self._contador_pres += 1

    def devolver(self):
        self._estado = "disponible"

    def mostrar_info(self):
        print(
            f"{self._codigo:^10}{self._titulo:^30}",
            f"{self._autor:^15}{self._anio_pub:^7}{self._estado:^12}",
            sep="",
        )


class Prestamo:
    # funciones auxiliares del sin POO
    def es_bisiesto(self, anio: int):
        return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)

    def dias_en_mes(self, mes, anio):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        elif mes == 2:
            return 29 if self.es_bisiesto(anio) else 28
        return 0

    def fecha_valida(self, dia, mes, annio):
        bisiesto = self.es_bisiesto(annio)

        if annio < 2025:
            return False
        if mes < 1 or mes > 12:
            return False
        elif annio >= 2025:
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                if dia > 31 or dia < 0:
                    return False
            elif mes in [4, 6, 9, 11]:
                if dia > 30 or dia < 0:
                    return False
            elif mes == 2:
                if bisiesto:
                    if dia > 29 or 0 > dia:
                        return False
                elif dia > 28 or 0 > dia:
                    return False
        return True

    def cal_f_entrega(self, fecha: tuple[int, int, int]):
        """Calcula la fecha de entrega sumando 7 días"""
        d, m, a = fecha
        d += 7
        dias_mes = self.dias_en_mes(m, a)
        if d > dias_mes:
            d -= dias_mes
            m += 1
            if m > 12:
                m = 1
                a += 1
        return (d, m, a)

    def cal_mora(self, fecha: tuple[int, int, int]):
        """Convierte fecha a número total de días desde año 0"""
        d, m, a = fecha
        total = a * 365 + d
        for i in range(1, m):
            total += self.dias_en_mes(i, a)
        # añadir días bisiestos
        total += a // 4 - a // 100 + a // 400
        return total

    def f_penal_v(self, actual: int, limite: int):
        """Devuelve True si la fecha actual supera la fecha límite"""
        return self.cal_mora(actual) > self.cal_mora(limite)

    def __init__(
        self, usuario: "Usuario", libro: "Libro", fecha_prestamo: tuple[int, int, int]
    ):
        self._usuario = usuario
        self._libro = libro
        self._fecha_prestamo = fecha_prestamo
        self._fecha_dev_estimada = self.cal_f_entrega(fecha_prestamo)
        self._fecha_dev_real = None
        self._devuelto = False
        self._multa = 0
        # Registrar préstamo
        self._libro.prestar()
        self._usuario.registrar_prestamo(self._libro.codigo)

    @property
    def usuario(self):
        return self._usuario

    @property
    def libro(self):
        return self._libro

    @property
    def devuelto(self):
        return self._devuelto

    @property
    def fecha_prestamo(self):
        return self._fecha_prestamo

    @property
    def fecha_dev_real(self):
        return self._fecha_dev_real

    @property
    def fecha_dev_estimada(self):
        return self._fecha_dev_estimada

    @fecha_dev_real.setter
    def fecha_dev_real(self, fecha_real: tuple[int, int, int]):
        self._fecha_dev_real = fecha_real

    def devolver(self, fecha_real: tuple[int, int, int]):
        if self._devuelto:
            print("Este préstamo ya fue devuelto.")
            return

        self._libro.devolver()
        self._fecha_dev_real = fecha_real

        # Calcular mora
        if self.f_penal_v(fecha_real, self._fecha_dev_estimada):
            dias_mora = self.cal_mora(fecha_real) - self.cal_mora(
                self._fecha_dev_estimada
            )
            self._multa = dias_mora * 10
            self._usuario.devolver_libro(self._libro.codigo, dias_mora)
            print(
                f"Libro '{self._libro.titulo}' devuelto con {dias_mora} días de retraso. Multa: S/.{self._multa}"
            )
        else:
            self._usuario.devolver_libro(self._libro.codigo, 0)
            print(f"Libro '{self._libro.titulo}' devuelto a tiempo. ¡Gracias!")

        self._devuelto = True

    def mostrar_info(self):
        print("===== DETALLE DEL PRÉSTAMO =====")
        print(f"Usuario: {self._usuario._nombre} {self._usuario._apellidos}")
        print(f"Libro: {self._libro.titulo}")
        print(f"Fecha de préstamo: {self._fecha_prestamo}")
        print(f"Fecha estimada de devolución: {self._fecha_dev_estimada}")
        if self._devuelto:
            print(f"Fecha real de devolución: {self._fecha_dev_real}")
            print(f"Multa: S/.{self._multa}")
        else:
            print("Estado: EN CURSO")


class Biblioteca:
    def cal_mora(self, fecha: tuple[int, int, int]):
        """Convierte fecha a número total de días desde año 0"""
        d, m, a = fecha
        total = a * 365 + d
        for i in range(1, m):
            total += self.dias_en_mes(i, a)
        # añadir días bisiestos
        total += a // 4 - a // 100 + a // 400
        return total

    def f_penal_v(self, actual: int, limite: int):
        """Devuelve True si la fecha actual supera la fecha límite"""
        return self.cal_mora(actual) > self.cal_mora(limite)

    def es_bisiesto(self, anio: int):
        return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)

    def dias_en_mes(self, mes, anio):
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif mes in [4, 6, 9, 11]:
            return 30
        elif mes == 2:
            return 29 if self.es_bisiesto(anio) else 28
        return 0

    def fecha_valida(self, dia, mes, annio):
        bisiesto = self.es_bisiesto(annio)

        if annio < 2025:
            return False
        if mes < 1 or mes > 12:
            return False
        elif annio >= 2025:
            if mes in [1, 3, 5, 7, 8, 10, 12]:
                if dia > 31 or dia < 0:
                    return False
            elif mes in [4, 6, 9, 11]:
                if dia > 30 or dia < 0:
                    return False
            elif mes == 2:
                if bisiesto:
                    if dia > 29 or 0 > dia:
                        return False
                elif dia > 28 or 0 > dia:
                    return False
        return True

    def __init__(self):
        self._usuarios: dict[int, Usuario] = {}
        self._libros: dict[int, Libro] = {}
        self._prestamos: list[Prestamo] = []

    @property
    def usuarios(self) -> dict[int, Usuario]:
        return self._usuarios.copy()

    @property
    def libros(self) -> dict[int, Libro]:
        return self._libros.copy()

    @property
    def prestamos(self) -> list[Prestamo]:
        return self._prestamos.copy()

    # agregacion de usuarios y comprobaciones
    def ver_nombre(self, n_evaluar):
        no_valido = False
        for letra in n_evaluar:
            if not (letra.isalpha() or letra == " "):
                no_valido = True
                break
        return no_valido

    def registrar_usuario(self):
        try:
            while True:
                dni = int(input("Ingrese el dni del cliente: "))
                if dni not in self.usuarios.keys() and len(str(dni)) == 8:
                    print("DNI asignado correctamente")
                    break
                elif dni in self.usuarios.keys():
                    print(f"Persona ya registrada con el dni:{dni}")
                else:
                    print("DNI NO VALIDO")
            while True:
                nombre = input("Nombre(s) de la persona: ")
                if self.ver_nombre(nombre):
                    print("Nombre no valido")
                else:
                    print("Nombre(s) asignado correctamente")
                    break
            while True:
                apellidos = input("Apellido(s) de la persona: ")
                if self.ver_nombre(apellidos):
                    print("Apellido no valido")
                else:
                    print("Apellido(s) asignado correctamente")
                    break
            self.agregar_usuario(dni=dni, nombre=nombre, apellidos=apellidos)
        except ValueError:
            print("ERROR: VALOR INGRESADO NO VALIDO")

    def agregar_usuario(self, dni: int, nombre: str, apellidos: str):
        if dni in self._usuarios:
            print("El usuario ya está registrado.")
            return
        self._usuarios[dni] = Usuario(dni, nombre, apellidos)
        print(f"Usuario '{nombre} {apellidos}' agregado correctamente.")

    # agregacion de Libros y comprobaciones
    def registrar_libro(self):
        try:
            while True:
                codigo = int(input("Ingrese el codigo del libro: "))
                if codigo in self.libros:
                    print("Codigo de libro ya asignado")
                else:
                    print("Codigo asignado correctamente")
                    break

            nombre = input("Nombre del libro: ")

            while True:
                autor = input("Nombre del autor: ")
                if self.ver_nombre(autor):
                    print("Nombre no valido")
                else:
                    print("Autor asignado correctamente")
                    break
            anio = int(input("año de publicacion: "))
            self.agregar_libro(codigo=codigo, titulo=nombre, autor=autor, anio_pub=anio)
        except ValueError:
            print("ERROR: VALOR INGRESADO NO VALIDO")

    def agregar_libro(self, codigo: int, titulo: str, autor: str, anio_pub: int):
        if codigo in self._libros:
            print("El libro ya existe en la biblioteca.")
            return
        self._libros[codigo] = Libro(codigo, titulo, autor, anio_pub)
        print(f"Libro '{titulo}' agregado al catálogo.")

    # menu de prestamos y prestamo
    def menu_prestamo(self):
        try:
            while True and len(self.usuarios) > 0:
                print("Sistema de prestamo de libros:")
                dni = int(input("Ingrese el dni (0 = salir): "))
                if dni in self.usuarios:
                    print("DNI VALIDO:")
                    if len(self.usuarios[dni]._libros_prestados) < 3:
                        print(
                            "CODIGO                NOMBRE                "
                            " AUTOR             AÑO             ESTADO",
                            end="",
                        )
                        print()
                        for lib in self.libros.values():
                            lib.mostrar_info()

                        usu_entrada = int(input("Codigo del libro a prestar: "))
                        self.registrar_prestamo(
                            dni_usuario=dni, codigo_libro=usu_entrada
                        )
                    else:
                        print("Maximo de 3 prestamos por persona")
                elif dni == 0:
                    break
                else:
                    print("No hay dni registrado")

        except ValueError:
            print("Error de ingreso de datos")

    def registrar_prestamo(self, dni_usuario: int, codigo_libro: int):
        if dni_usuario not in self._usuarios:
            print("Usuario no encontrado.")
            return
        if codigo_libro not in self._libros:
            print("Libro no encontrado.")
            return

        usuario = self._usuarios[dni_usuario]
        libro = self._libros[codigo_libro]

        if libro.estado != "disponible":
            print("El libro no está disponible actualmente.")
            return

        fecha_prestamo = (0, 0, 0)

        try:
            while True:
                print("Ingreso de fecha de prestamo:")
                dia = int(input("Dia: "))
                mes = int(input("Mes:"))
                annio = int(input("Año:"))
                if self.fecha_valida(dia, mes, annio):
                    fecha_prestamo = (dia, mes, annio)
                    break
                else:
                    print("Fecha invalida")
        except ValueError:
            print("Error de ingreso de fecha")

        if self.fecha_valida(dia, mes, annio):
            prestamo = Prestamo(usuario, libro, fecha_prestamo)
            self._prestamos.append(prestamo)
            print(
                f"Préstamo registrado: '{libro.titulo}' para {usuario._nombre} ({usuario._dni})"
            )
            print(f"Fecha estimada de devolución: {prestamo.fecha_dev_estimada}")

    # devoluciones
    def menu_devolucion(self):
        try:
            while True and len(self._usuarios) > 0:
                print("Sistema de devolución de libros:")
                dni = int(input("Ingrese el DNI del usuario (0 = salir): "))

                if dni == 0:
                    break

                if dni in self._usuarios.keys():
                    usuario = self._usuarios[dni]

                    if len(usuario.libros_prestados) == 0:
                        print("Este usuario no tiene libros prestados.")
                        continue

                    print("DNI válido.")
                    usuario.mostrar_info()

                    print("\nLibros actualmente prestados:")
                    for codigo in usuario.libros_prestados:
                        self._libros[codigo].mostrar_info()

                    codigo_libro = int(
                        input("\nIngrese el código del libro a devolver: ")
                    )

                    if codigo_libro not in usuario.libros_prestados:
                        print("El código ingresado no pertenece a este usuario.")
                        continue

                    # Buscar préstamo activo
                    prestamo_activo = None
                    for prest in self._prestamos:
                        if (
                            prest.usuario.dni == dni
                            and prest.libro.codigo == codigo_libro
                            and not prest.devuelto
                        ):
                            prestamo_activo = prest
                            break

                    if prestamo_activo is None:
                        print("No se encontró un préstamo activo con esos datos.")
                        continue

                    # Ingreso de fecha real de devolución
                    while True:
                        print("\nIngrese la fecha de devolución:")
                        dia = int(input("Día: "))
                        mes = int(input("Mes: "))
                        anio = int(input("Año: "))
                        if not self.fecha_valida(dia, mes, anio):
                            print("Fecha inválida, intente nuevamente.")
                            continue
                        fecha_real = (dia, mes, anio)
                        break

                    # Validar que la devolución no sea antes del préstamo
                    if not self.f_penal_v(fecha_real, prestamo_activo.fecha_prestamo):
                        print(
                            "ERROR: La fecha de devolución no puede ser anterior a la fecha de préstamo."
                        )
                        continue

                    # Procesar devolución
                    self.devolver_libro(
                        dni_usuario=dni,
                        codigo_libro=codigo_libro,
                        fecha_real=fecha_real,
                    )

                    # Mostrar detalle del préstamo actualizado
                    prestamo_activo.mostrar_info()

                else:
                    print("No hay un usuario registrado con ese DNI.")

        except ValueError:
            print("Error: Valor ingresado no válido.")

    def devolver_libro(
        self, dni_usuario: int, codigo_libro: int, fecha_real: tuple[int, int, int]
    ):
        for prestamo in self._prestamos:
            if (
                prestamo.usuario._dni == dni_usuario
                and prestamo.libro.codigo == codigo_libro
                and not prestamo.devuelto
            ):
                prestamo.devolver(fecha_real)
                return
        print("No se encontró un préstamo activo con esos datos.")

    # calcular penalidad
    def cal_penalidad(self):
        try:
            while True:
                print("Bienvenido al simulador de calculo de penalidad:")
                user = input(
                    "Desea estimar la mora (S: salir /cualquier tecla :continuar)"
                )
                if user.upper() == "S":
                    break
                while True:
                    print("Ingrese la fecha actual a tomar como inicio:")
                    dia_actual = int(input("Dia: "))
                    mes_actual = int(input("Mes: "))
                    annio_actual = int(input("Año: "))
                    if self.fecha_valida(dia_actual, mes_actual, annio_actual):
                        break
                    else:
                        print("Fecha no valida")
                print("Recuerde : la mora empieza luego de 7 dias de inicio")
                while True:
                    print("Ingrese la fecha de devolucion:")
                    dia_dev = int(input("Dia: "))
                    mes_dev = int(input("Mes: "))
                    annio_dev = int(input("Año: "))
                    if self.fecha_valida(dia_actual, mes_actual, annio_actual):
                        break
                    else:
                        print("Fecha no valida")

                if self.f_penal_v(
                    [dia_actual, mes_actual, annio_actual],
                    [dia_dev, mes_dev, annio_dev],
                ):
                    print("No valido , volver a ingresar fechas")
                    continue
                else:
                    dias_mora = (
                        self.cal_mora([dia_dev, mes_dev, annio_dev])
                        - self.cal_mora([dia_actual, mes_actual, annio_actual])
                        - 7
                    )
                    mora = max(0, dias_mora)
                    mora = mora * 10
                    print(
                        f"Mora estimada luego del {dia_actual}/ {mes_actual}/{annio_actual} de {max(0, dias_mora)} dias es de : S/.{mora}"
                    )
        except ValueError:
            print("ERROR")

    def f_mostrar_menu(self):
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


def main():
    biblioteca = Biblioteca()

    while True:
        biblioteca.f_mostrar_menu()
        try:
            usu_entrada = int(input("Eleccion del usuario:  "))
            match usu_entrada:
                case 1:
                    biblioteca.registrar_usuario()
                case 2:
                    biblioteca.registrar_libro()
                case 3:
                    biblioteca.menu_prestamo()
                case 4:
                    biblioteca.menu_devolucion()
                case 5:
                    biblioteca.cal_penalidad()
                case 6:
                    pass
                case 7:
                    print("Fin del Programa")
                    break
        except ValueError:
            print("ERROR : VALOR INGRESADO NO ES UN NUMERO")


main()
