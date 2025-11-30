from abc import ABC, abstractmethod
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


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
        return self._libros_prestados

    @property
    def cant_prestamos(self):
        return self._cant_prestamos

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellidos(self):
        return self._apellidos

    @property
    def deuda(self):
        return self._deuda

    @libros_prestados.setter
    def libros_prestados(self, lista_codigos):
        self._libros_prestados = lista_codigos

    @deuda.setter
    def deuda(self, n_deuda):
        self._deuda = n_deuda

    @cant_prestamos.setter
    def cant_prestamos(self, cantidad):
        self._cant_prestamos = cantidad

    @dni.setter
    def dni(self, dn):
        self._dni = dn

    @nombre.setter
    def nombre(self, nom):
        self._nombre = nom

    @apellidos.setter
    def apellidos(self, apell):
        self._apellidos = apell

    def registrar_prestamo(self, codigo_libro: int):
        if codigo_libro in self._libros_prestados:
            print("Ese libro ya está prestado por este usuario.")
            return

        if len(self.libros_prestados) >= 3:
            print("Solo es máximo de 3 préstamos por usuario.")
            return

        self._libros_prestados.append(codigo_libro)
        self.cant_prestamos += 1
        print(f"Libro con codigo {codigo_libro} registrado correctamente.")

    def devolver_libro(self, codigo_libro: int, dias_mora: int = 0):
        """Devuelve un libro y calcula penalidad."""
        if codigo_libro in self._libros_prestados:
            self._libros_prestados.remove(codigo_libro)
            multa = dias_mora * 10
            self.deuda += multa
        else:
            print("ALERTA: Este libro no está registrado en sus préstamos.")

    def mostrar_info(self):
        """=====INFORMACION GENERAL DEL USUARIO====="""
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre} {self.apellidos}")
        print(f"Libros prestados actualmente: {len(self.libros_prestados)}")
        print(f"Deuda: S/.{self.deuda}")


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

    @estado.setter
    def estado(self, n_estado):
        self._estado = n_estado

    @contador_pres.setter
    def contador_pres(self, cont):
        self._contador_pres = cont

    @codigo.setter
    def codigo(self, cod):
        self._codigo = cod

    @titulo.setter
    def titulo(self, lib):
        self._titulo = lib

    @autor.setter
    def autor(self, aut):
        self._autor = aut

    @anio_pub.setter
    def anio_pub(self, anio):
        self._anio_pub = anio

    @contador_pres.setter
    def contador_pres(self, cont):
        self._contador_pres = cont

    # metodos
    def prestar(
        self,
    ):
        self.estado = "prestado"
        self.contador_pres += 1

    def devolver(self):
        self.estado = "disponible"

    def mostrar_info(self):
        print(
            f"{self.codigo:^10}{self.titulo:^30}",
            f"{self.autor:^15}{self.anio_pub:^7}{self.estado:^12}",
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

    @property
    def multa(self):
        return self._multa

    @fecha_dev_real.setter
    def fecha_dev_real(self, fecha_real: tuple[int, int, int]):
        self._fecha_dev_real = fecha_real

    @fecha_dev_estimada.setter
    def fecha_dev_estimada(self, dev):
        self._fecha_dev_estimada = dev

    @multa.setter
    def multa(self, mul):
        self._multa = mul

    @devuelto.setter
    def devuelto(self, dev):
        self._devuelto = dev

    def devolver(self, fecha_real: tuple[int, int, int]):
        if self._devuelto:
            print("Este préstamo ya fue devuelto.")
            return

        self.libro.devolver()
        self.fecha_dev_real = fecha_real

        # Calcular mora
        if self.f_penal_v(fecha_real, self.fecha_dev_estimada):
            dias_mora = self.cal_mora(fecha_real) - self.cal_mora(
                self.fecha_dev_estimada
            )
            self.multa = dias_mora * 10
            self.usuario.devolver_libro(self.libro.codigo, dias_mora)
            print(
                f"Libro '{self.libro.titulo}' devuelto con {dias_mora} días de retraso. Multa: S/.{self.multa}"
            )
        else:
            self._usuario.devolver_libro(self.libro.codigo, 0)
            print(f"Libro '{self.libro.titulo}' devuelto a tiempo. ¡Gracias!")

        self.devuelto = True

    def mostrar_info(self):
        print("===== DETALLE DEL PRÉSTAMO =====")
        print(f"Usuario: {self.usuario.nombre} {self.usuario.apellidos}")
        print(f"Libro: {self.libro.titulo}")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha estimada de devolución: {self.fecha_dev_estimada}")
        if self.devuelto:
            print(f"Fecha real de devolución: {self.fecha_dev_real}")
            print(f"Multa: S/.{self.multa}")
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
        return self._usuarios

    @property
    def libros(self) -> dict[int, Libro]:
        return self._libros

    @property
    def prestamos(self) -> list[Prestamo]:
        return self._prestamos

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
                    if len(self.usuarios[dni].libros_prestados) < 3:
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
        if dni_usuario not in self.usuarios:
            print("Usuario no encontrado.")
            return
        if codigo_libro not in self.libros:
            print("Libro no encontrado.")
            return

        usuario = self.usuarios[dni_usuario]
        libro = self.libros[codigo_libro]

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
            self.prestamos.append(prestamo)
            print(
                f"Préstamo registrado: '{libro.titulo}' para {usuario.nombre} ({usuario.dni})"
            )
            print(f"Fecha estimada de devolución: {prestamo.fecha_dev_estimada}")

    # devoluciones
    def menu_devolucion(self):
        try:
            while True and len(self.usuarios) > 0:
                print("Sistema de devolución de libros:")
                dni = int(input("Ingrese el DNI del usuario (0 = salir): "))

                if dni == 0:
                    break

                if dni in self.usuarios.keys():
                    usuario = self.usuarios[dni]

                    if len(usuario.libros_prestados) == 0:
                        print("Este usuario no tiene libros prestados.")
                        continue

                    print("DNI válido.")
                    usuario.mostrar_info()

                    print("\nLibros actualmente prestados:")
                    for codigo in usuario.libros_prestados:
                        self.libros[codigo].mostrar_info()

                    codigo_libro = int(
                        input("\nIngrese el código del libro a devolver: ")
                    )

                    if codigo_libro not in usuario.libros_prestados:
                        print("El código ingresado no pertenece a este usuario.")
                        continue

                    # Buscar préstamo activo
                    prestamo_activo = None
                    for prest in self.prestamos:
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
                    if self.cal_mora(fecha_real) < self.cal_mora(
                        prestamo_activo.fecha_prestamo
                    ):
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
                prestamo.usuario.dni == dni_usuario
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
                    if self.fecha_valida(dia_dev, mes_dev, annio_dev):
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
    |                                      | 7.                       Cargar Archivo                           |                                                                |
    |                                      ---------------------------------------------------------------------                                                                |
    |                                      ---------------------------------------------------------------------                                                                |
    |                                      | 8.                        Guardar Archivo                         |                                                                |
    |                                      ---------------------------------------------------------------------                                                                |
    |                                      ---------------------------------------------------------------------                                                                |
    |                                      | 9.                            SALIR                               |                                                                |
    |                                      ---------------------------------------------------------------------                                                                |
    +---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
            """
        )

    def menu_reportes(self):
        print(
            r"""
    +-------------------------------------------------------------------------------------------+
    |           ---------------------------------------------------------------------           |
    |           |1.       Libros más prestados (popularidad de títulos)             |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |2.      Usuarios con más préstamos (eficiencia de lectura)         |           |
    |           ---------------------------------------------------------------------           |
    |           ----------------------------------------------------------------------          |
    |           |3.      Tiempo promedio de préstamo por libro (análisis de duración)|          |
    |           ----------------------------------------------------------------------          |
    |           ---------------------------------------------------------------------           |
    |           |4.      Recaudación por penalidades (análisis de ingresos)         |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |5.         LIBROS DISPONIBLES VS LIBROS PRESTADOS                  |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |6.          REPORTE DE FECHAS DE PUBLICACIONES DE LIBROS           |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |7.                  Libros nunca prestados                         |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |8.           Ranking Usuarios con menos préstamos                  |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |9.                TASA DE DEVOLUCIÓN TARDÍA POR MES                |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |10.               CANTIDAD DE LIBROS POR AUTOR                     |           |
    |           ---------------------------------------------------------------------           |
    |           ---------------------------------------------------------------------           |
    |           |11.                       Regresar al menu                         |           |
    |           ---------------------------------------------------------------------           |
    +-------------------------------------------------------------------------------------------+
    """
        )

    def reporte1(self):
        def obtener_prestamos(libro: Libro):
            return libro.contador_pres

        libros_ordenados = sorted(
            self.libros.values(), key=obtener_prestamos, reverse=True
        )
        limite = 0
        df = {"Titulo del libro": [], "Cantidad de Préstamos": []}
        for libro in libros_ordenados:
            if limite > 5:
                break
            df["Titulo del libro"].append(libro.titulo)
            df["Cantidad de Préstamos"].append(libro.contador_pres)
            limite += 1

        dfreport = pd.DataFrame(df)

        sns.barplot(
            x="Titulo del libro",
            y="Cantidad de Préstamos",
            data=dfreport,
            palette="viridis",
        )
        plt.title("TOP 5 LIBROS con MÁS prestamos", fontsize=14)
        plt.xlabel("Titulo del libro", fontsize=12)
        plt.ylabel("Cantidad de Préstamos", fontsize=12)
        plt.show()
        plt.close()

    def reporte2(self):
        def obtener_prestamos(persona: Usuario):
            return persona.cant_prestamos

        usuarios_ordenados = sorted(
            self.usuarios.values(), key=obtener_prestamos, reverse=True
        )
        limite = 0

        df = {"Usuario": [], "Cantidad de prestamos": []}

        for usuario in usuarios_ordenados:
            if limite >= 5:  # máximo 5 libros
                break

            nombre_completo = f"{usuario.nombre} {usuario.apellidos}"
            df["Usuario"].append(nombre_completo)
            df["Cantidad de prestamos"].append(usuario.cant_prestamos)
            limite += 1

        dfreport = pd.DataFrame(df)

        sns.barplot(
            x="Usuario", y="Cantidad de prestamos", data=dfreport, palette="viridis"
        )

        plt.title("TOP 5 Usuarios con MÁS prestamos", fontsize=14)
        plt.show()
        plt.close()

    def reporte3(self):
        print(
            r"""                                                                                
                                :-=+++=-:                                                           
                        :=#@@@@@@@@@@@@@@@@@@@*-:                                                   
                     +@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=                                                
                  +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-                                             
               :%@@@@@@@@@@#=              :=#@@@@@@@@@@*                                           
             :@@@@@@@@@#:                       -@@@@@@@@@#                                         
            #@@@@@@@%:        -++:                 =@@@@@@@@=                                       
          -@@@@@@@#:      *@@#:                      :@@@@@@@%                                      
         =@@@@@@@:     =@@@#                           -@@@@@@@:                                    
        +@@@@@@*     +@@@#                               %@@@@@@-                                   
       =@@@@@@-    -@@@@=                                 *@@@@@@                                   
      -@@@@@@-    *@@@@:                                   *@@@@@@                                  
      %@@@@@=    #@@@@                                      %@@@@@*                                 
     =@@@@@%    +@@@@:                                       @@@@@@:                                
     %@@@@@-    @@@@#                                        *@@@@@=                                
    :@@@@@@    *@@@@       BUSQUEDA EN LOS DATOS             :@@@@@@                                
    -@@@@@#    @@@@#                                          @@@@@@                                
    =@@@@@*    @@@@*          TIEMPO ESTIMADO                 %@@@@@:                               
    =@@@@@*    @@@@+                                          @@@@@@                                
    -@@@@@%    @@@@*                                          @@@@@@                                
     @@@@@@:   -@@@#                                         =@@@@@#                                
     *@@@@@+    %@@@                                         #@@@@@=                                
     -@@@@@@    :@@@#                                       =@@@@@@                                 
      *@@@@@#    -@@@:                                      @@@@@@-                                 
       @@@@@@#    :@@@:                                    @@@@@@#                                  
       :@@@@@@%     +@@:                                 :@@@@@@%                                   
        :@@@@@@@:     #@=                               =@@@@@@%                                    
          %@@@@@@#      =#                            :%@@@@@@*                                     
           *@@@@@@@#                                :@@@@@@@@-                                      
            :%@@@@@@@@-                           +@@@@@@@@# :%@-                                   
              :@@@@@@@@@%+:                   :*@@@@@@@@@%: *@@@@@:                                 
                 %@@@@@@@@@@@@*-         =#@@@@@@@@@@@@#  *@@@@%:                                   
                   =%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:  :%@@@%  #@@@@@@#                            
                      :#@@@@@@@@@@@@@@@@@@@@@@@@@+        :@@ =@@@@@@@@@@#                          
                           -#%@@@@@@@@@@@@@%+:              - @@@@@@@@@@@@@+                        
                                                              @@@@@@@@@@@@@@@=                      
                                                              -@@@@@@@@@@@@@@@@:                    
                                                                #@@@@@@@@@@@@@@@%:                  
                                                                  @@@@@@@@@@@@@@@@%                 
                                                                   -@@@@@@@@@@@@@@@@#               
                                                                     =@@@@@@@@@@@@@@@@+             
                                                                       =@@@@@@@@@@@@@@@@=           
                                                                         *@@@@@@@@@@@@@@@@:         
                                                                           #@@@@@@@@@@@@@@@@:       
                                                                             @@@@@@@@@@@@@@@@%      
                                                                              :@@@@@@@@@@@@@@@@     
                                                                                -@@@@@@@@@@@@@@*    
                                                                                  +@@@@@@@@@@@@=    
                                                                                    *@@@@@@@@@*     
                                                                                      +@@@@@*       
"""
        )
        print("\n=== REPORTE 3: Tiempo promedio de préstamo por libro ===\n")

        total_dias = 0
        total_prestamos = 0

        for prestamo in self._prestamos:

            if not prestamo.devuelto:
                continue

            # Convertir fechas a días
            dias_inicio = prestamo.cal_mora(prestamo.fecha_prestamo)
            if prestamo.fecha_dev_real is None:
                continue
            dias_fin = prestamo.cal_mora(prestamo.fecha_dev_real)

            duracion = dias_fin - dias_inicio

            total_dias += duracion
            total_prestamos += 1

        if total_prestamos == 0:
            print("No existen préstamos devueltos para calcular el promedio.")
            return

        promedio = total_dias / total_prestamos

        print(f"Tiempo promedio general de préstamo: {promedio:.2f} días")
        lista1 = [promedio, total_dias]
        lista2 = ["promedio", "Horas totales"]
        plt.bar(lista2, lista1)
        plt.xlabel("costos")
        plt.ylabel("Recaudación")
        plt.title("Compararción de promedio y total")
        plt.show()
        plt.close()

    def reporte4(self):
        print(
            r"""
                                                 ..                                                 
   .                                   .       .----:..    ....                                   . 
  .                                  .       ..-------:....:--.            .       .     .          
                .                 ..  .---. .-==-----=====----:.               .   .    .           
   .         .                        :---======----=====----:.  .  .                 .             
   .                 .             .  .:---=====----=====---..                        .        .    
 .    .   .                            ..---====----====---.      .         .       .           .   
.                                       . :--===---====--:.                      .                  
                          .               .--===---======.                                          
                      .  ..               -########*****+:.           .                        .    
     .                       .            .-==**====**===.          .      .                        
     .                        .           .-=#+------=#*=..            .                            
      .   .                     .       ..-+#----------+#=:.               .   .   .                
     .                                 .-----------------==-:.   .            .                     
                   .              . ..--------------------===-..                    ..              
 .           . ..                  .:-----------------------===:...              .             .    
                                ...-------------=+++---------===-..                     .           
                  .          . ..:--------------+##*----------====:.     .  .                       
  .   .                        .:-------------=*#####**=-------====:                          .     
..        .                   .:------------=##########+--------====-.                              
      .                       :-------------*###+----+*---------=====:.                      . .  . 
 .   .           .          ..--------------*###*=---------------=====:. .                 .        
                   .       ..---------------=#######*-------------====-.     .                   .  
     .                ..   .:-----------------=*######*=----------=====:                            
     .                     .----------------------+*###*----------======..   .  .   .          .    
                           .------------------------*###=----------=====..             ..           
              .  .  .      .----------------+##*+=+####*-----------=====:.                   .      
           .  .            .----------------##########*------------=====..    .                     
                           .------------------=+*##*=-------------=====-..                         .
          .                ..-------------------*##*--------------=====.                  . .    .  
                            .:-----------------------------------=====:.                            
             . .        .     .---------------------------------====-.. .  .                        
.                    .    ...::::------------------------------====-::::...                  .  .   
                          .::::::::--------------------------==--:::::::::.       .     .           
           .               ......::::::::::::::::::::::::::::::::::.......                          
"""
        )

        def obtener_deuda(user: Usuario):
            return user.deuda

        deudores_ordenados = sorted(
            self.usuarios.values(), key=obtener_deuda, reverse=True
        )
        deuda_total = 0
        limite = 0
        listde = []
        listu = []
        for i, user in self.usuarios.items():
            deuda_total += user.deuda
            listu.append(user.nombre)
            listde.append(user.deuda)

        print("_____________________________________" * 3)
        print(" " * 30, end="")
        print(f"Recaudación por penalidades: S/.{deuda_total}")
        print("_____________________________________" * 3)
        for user in deudores_ordenados:
            if limite >= 20:  # máximo 20 libros
                break
            print(
                f"{user.dni:^10}{user.nombre:^30}",
                f"{user.apellidos:^15}{user.deuda:^7}{user.cant_prestamos:^12}",
                sep="",
            )
            limite += 1

        plt.bar(listu, listde)
        plt.xlabel("Ususarios")
        plt.ylabel("Recaudación por penalidad")
        plt.title("Recaudación por penalidades")
        plt.show()
        plt.close()

    def reporte5(self):
        try:
            print(
                r"""
        .                                .    .          .                           .                     
                                .                         .....:-=+*=..                                    
            .                .                      ...-*##*==-----#=...                              .  
                    .                          ..:-*#*+--------------*+..      .       .          .       
                    . .                    ...=*#*+===========----------++..          .   .         .       
        .                          . ..+##+=====================-------++.   .                            
                    .         ...:+#*+============================------++.                       .       
                .  .       ..-+#*+=======================+*#*+===**==-----+*...             .              
                .   .....+##========================*#*-:::::::::::++=-----+*..                         .  
                ..:=#*+=====================+**+-::::::::::::::::::++==----*+... .             .          
            .   ..*#+===================+##+::::::::::::::::::::::::::++==----*=..           .              
            ..##+================*#=:::.::::::::::::::::::::::::::::++==----*-.                    .  .  
            .#==#+============*+::.::::::::::::::::::::::::::::::::::*+==----*=.                         
        .    -#===#===========#::::::::::::::::::::::::::::::::::::::::*+==----*-          .              
            .-*===+#==========*:::::::::::::::::::::::::::::::::::::::::*===----#:..     .          .     
            .:#====+#=========#:::::::::::::::::::::::::::::::::::::::::-#===----#:..                     
            .#=====*#========++:::::::::::::::::::::::::::::::::::::::::++===----#..        .            
            .:#=====**========*-:::::::::::::::::::::::::::::::::::::::-*=====----#:.                    
                .*+=====#+========#:::::::::::::::::::::::::::::::::::::=**=======---=#..     .   .         
                .#+=====#+=======+*:::::::::::::::::::::::::::::::-=##+===========---=#. .                .
                ..#======#+=======+*::::::::::::::::::::::::-=+#*+=================---=*.                  
            .  ..-*=====+#========+*::::::::::::::::::-+#*+========================---=*.           .    .
                .+*=====+#========+*::::::::::::=##*===============================---=#..  .            
        .       ..+*=====+#=========*+-::-=*#*+=====================================---+*.             . 
                    .*+=====**=========================================================---++..           . 
                . ..#======*+=========================================================---*+.             
                    ..#======#+=========================================================---*=.            
                    ...#======#+=========================================================---*=.           
                    . ..-*======#+=========================================================---*-           
                        .=*=====+#=========================================================----#:..  . .   
                        ..+*=====+#=========================================================---=#..   .    
                        .*+=====**=========================================================---=#.        
                            .#======**=========================================================---++.       
        .        .    .  ..#======#+========================================================----#:..     
            .              .:#======#+========================================================---*=..     
        .      .   .       .-*======#+=======================================================*###-..     
                            .+*=====+#=================================================+*##*+===#.       
                    .           .+*=====+#===========================================+*##++===+*#*-...      
                                .*+=====+#=====================================+*##+====+##*:.-*..         
            .                  ..#======**===============================+*##+===++##+-.....-*-.         .
                                . .:#======**=========================+##*+====*##=:.....=+=:..==.          
                    . .            .:#======#+===================+##*=====*##=......:*+........:#..         
                                    .-*======#+============+*##*+===+*#*=:.:-..-+=:.......:=+=:.-*...  .    
                        .        ..+*======#+======+###++===+##*-:.:++-:...........=*-:....:+##**.     . 
                        .            ..*+=====+#++##*+====+*#*-..:=*-............-*=.....:+##*====+#:       
                ...           .      .*+=====#+====+*#+-..-++-....:==....:=+=:....-+#*+====+*#+-...       
            .                        ..*+===*+=*#+:...........-*=:...-*=:....-*#*+====*##+:.......        
        .     .          .           ..#+==#+=#..:=*=...-++:...-++:...:-*#*+===+*#*=........             
                                        ..#+=#++#-...=+=:...-......:+*#*+===+*#+-.....              .      
                                        ..#+**=##=....-#+....:*##+====+##+......    . .            .      
                            .           ..**#=+#......:=##*+===+*#*=:.....                               
                        .                  .+#*=+#+*#*++==+*##+-......                                .   
                    .           .             .-##=====+##*-....                                      .     
                                    .         ..-**=-....... ..      .  .                                  
        """
            )
            aux_dis, aux_pres = 0, 0
            for i, libro in self.libros.items():
                if libro.estado == "disponible":
                    aux_dis += 1
                else:
                    aux_pres += 1
            print("_____________________________________" * 3)
            print(" " * 30, end="")
            print("LIBROS DISPONIBLES VS LIBROS PRESTADOS ")
            print("_____________________________________" * 3)
            print(" " * 30, end="")
            print(f"LIBROS TOTALES :  {len(self.libros)} ")
            print("_____________________________________" * 3)
            print()
            print(
                f"LIBROS DISPONIBLES : {int(aux_dis/len(self.libros)*100) * "*"}:{aux_dis/len(self.libros)*100:.2f}%"
            )
            print(
                f"LIBROS PRESTADOS   : {int(aux_pres/len(self.libros)*100) * "*"}:{aux_pres/len(self.libros)*100:.2f}%"
            )
            lista = [aux_dis, aux_pres]
            nom = ["Disponible", "Prestado"]
            colores = ["#32f54f", "#fa3f3f"]
            desfase = [0, 0.01]
            plt.pie(
                lista, labels=nom, autopct="%0.1f%%", colors=colores, explode=desfase
            )
            plt.axis("equal")
            plt.show()
            plt.close()
        except ZeroDivisionError:
            print(" " * 20, end="")
            print("Datos no disponibles")
            print("_____________________________________" * 3)
            input("Enter para continuar")

    def reporte6(self):
        print(
            r"""
                                        :---===++++++++====--::                                      
                                -=*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*+-:                              
                            :*%@@@@@@@%%#**+++===========+++*##%@@@@@@@%*-                           
                            :#@@@@#+=::                             :-+#@@@@#:                         
                            -@@@%=                                        =%@@@:                        
                            %@@@%-                                       :*@@@@=                        
                            @@@@@@@#+-:                             :-+*%@@@@@@=                        
                            @@@=+#@@@@@@@#**++=-:::::  ::::-=+++*#@@@@@@@%*-*@@+                        
                            @@@:   -=+#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=-    +@@=                        
                            %@@-         :-==+++****#*****+++++=-:          +@@=                        
                            *@@-                                            +@@=                        
                            -@@+                                            *@@:                        
                            :@@%:                                          -%@%                         
                            =@@#:   :+=                           :++:   -%@@:                         
                            *@@%-   :#@%+=                   :=*@@*    =@@@=                          
                            +@@@*:   +@@@@@#*+==-::::-==+*%@@@@@=   :#@@@=                           
                                -%@@%+    *@@@@@@@@@@@@@@@@@@@@@@*    +@@@#:                            
                                :+%@@%-   -#@@@@@@@@@@@@@@@@@@#-   =%@@%=                              
                                :*@@@#:   =%@@@@@@@@@@@@@@%=   :#@@@+:                               
                                    -#@@@+   :*@@@@@@@@@@@@*:   +@@@*:                                 
                                    -%@@@=   -#@@@@@@@@%-   =%@@#-                                   
                                        =%@@%-   =@@@@@@+   :#@@%=                                     
                                        +@@@*:  :%@@@-   +@@@+:                                      
                                            :#@@#:   @@-  :*@@#:                                        
                                            =@@+:  %@   -@@*                                          
                                            +@@+   =%   -@@#:                                         
                                            :#@@#:    -    +@@%=                                        
                                        +@@@*:           =%@@#:                                      
                                        -%@@%-              :*@@@*:                                    
                                    -#@@@+                  -%@@@+                                   
                                    :*@@@#:                     =@@@%=                                 
                                :=%@@%-                         +@@@#-                               
                                -#@@@+                            :*@@@*:                             
                                :*@@@*:                               -%@@%-                            
                            -%@@#-                                  :+@@@*                           
                            :@@@+                  +@:                 :#@@#                          
                            :@@%-                  +@@@-                  *@@*                         
                            #@@=                =*@@@@@@%+-                #@@-                        
                            :@@#             :+#@@@@@@@@@@@@@*=:            =@@*                        
                            -@@#          =*@@@@@@@@@@@@@@@@@@@@%+-         :@@@                        
                            -@@*      :=#@@@@@@@@@@@@@@@@@@@@@@@@@@@*=       %@@                        
                            -@@*    -*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:    %@@                        
                            =@@*  :+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=   %@@:                       
                            -@@#  +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#: :@@@                        
                            :@@%:  :=*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*=:   *@@%                        
                            +@@%+:      :=++***##%%%%%%%###***+=-:       =#@@%:                        
                            =%@@@%*=-:                            :-=*%@@@@*                          
                                =#@@@@@@@%#*+++==-===--======++**#%@@@@@@@#+:                           
                                -=*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*=-                               
                                        :--==++++**++++++++==--:                                      
    """
        )
        try:
            annios_list = []
            recuentos = dict()
            for i, lib in self.libros.items():
                annios_list.append(lib.anio_pub)
            for num in annios_list:
                recuentos[num] = recuentos.get(num, 0) + 1

            print("_____________________________________" * 3)
            print(" " * 20, end="")
            print("               Recuento de Fechas de Publicación")
            print("_____________________________________" * 3)
            for clave, valor in recuentos.items():
                print(f"Fecha => {clave}      | recuento => {valor}")
            print("_____________________________________" * 3)
            x = recuentos.keys()
            y = recuentos.values()
            plt.bar(x, y, width=0.9, color="#4B7DF3")
            plt.xlabel = "año de publicaciónn"
            plt.ylabel = "cantidad"
            plt.title = "Recuento de fechas de fublicación"
            plt.show()
            plt.close()

            input("Enter para continuar")
        except ZeroDivisionError:
            print(" " * 20, end="")
            print("Datos no disponibles")
            print("_____________________________________" * 3)
            input("Enter para continuar")

    def reporte7(self):
        try:

            def obt_contador(lib: Libro):
                return lib.contador_pres

            print("\n=== REPORTE 7: Libros nunca prestados ===")

            if len(self.libros) == 0:
                print("No hay libros registrados.")
                return

            libros_ordenados = sorted(self.libros.values(), key=obt_contador)

            top = libros_ordenados[:10]

            titulos = [lib.titulo for lib in top]
            valores = [lib.contador_pres for lib in top]

            print(f"\n{'Título del libro':40} | Préstamos")
            print("-" * 60)
            for t, v in zip(titulos, valores):
                print(f"{t:40} | {v}")

            plt.figure(figsize=(10, 5))
            plt.bar(titulos, valores)
            plt.title("Libros menos prestados (ranking)")
            plt.xlabel("Título del libro")
            plt.ylabel("Cantidad de préstamos")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.show()
            plt.close()
        except TypeError:
            print()

    def reporte8(self):
        def cant_pres(pres: Usuario):
            return pres.cant_prestamos

        print("\n=== REPORTE 8:  Ranking Usuarios con menos préstamos ===")

        if len(self.usuarios) == 0:
            print("No hay usuarios registrados.")
            return

        usuarios_ordenados = sorted(self.usuarios.values(), key=cant_pres)

        top = usuarios_ordenados[:10]

        nombres = [u.nombre + " " + u.apellidos for u in top]
        valores = [u.cant_prestamos for u in top]

        print(f"\n{'Usuario':40} | Préstamos")
        print("-" * 55)
        for n, v in zip(nombres, valores):
            print(f"{n:40} | {v}")

        plt.figure(figsize=(10, 5))
        plt.bar(nombres, valores)
        plt.title("Ranking de usuarios con menos préstamos")
        plt.xlabel("Usuarios")
        plt.ylabel("Cantidad de préstamos")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.show()
        plt.close()

    def reporte9(self):
        filas = []

        for prestamo in self._prestamos:
            if prestamo.devuelto:
                dia, mes, anio = prestamo.fecha_dev_real
                if prestamo.multa > 0:
                    cont_tardio = 1
                else:
                    cont_tardio = 0
                filas.append({"anio": anio, "mes": mes, "tardia": cont_tardio})

        if not filas:
            print("No hay préstamos devueltos para analizar.")
            return

        df = pd.DataFrame(filas)

        estadisticas = {}

        for i, fila in df.iterrows():
            anio = fila["anio"]
            mes = fila["mes"]
            clave = f"{anio}-{mes:02d}"

            if clave not in estadisticas:
                estadisticas[clave] = {"devueltos": 0, "tardios": 0}

            estadisticas[clave]["devueltos"] += 1
            estadisticas[clave]["tardios"] += fila["tardia"]

        meses = []
        tasas = []

        print("\n_____TASA DE DEVOLUCIÓN TARDÍA POR MES______")
        for clave in sorted(estadisticas.keys()):
            dev = estadisticas[clave]["devueltos"]
            tard = estadisticas[clave]["tardios"]
            tasa = (tard / dev) * 100

            print(f"{clave}: {tasa:.2f}%")

            meses.append(clave)
            tasas.append(tasa)

        plt.figure(figsize=(8, 4))
        plt.plot(meses, tasas, marker="o")
        plt.title("Tasa de devolución tardía por mes")
        plt.xlabel("Mes")
        plt.ylabel("Porcentaje (%)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        plt.close()

    def reporte10(self):
        autores = []
        recuentos = dict()
        for i, lib in self.libros.items():
            autores.append(lib.autor)
        for autor in autores:
            recuentos[autor] = recuentos.get(autor, 0) + 1
        limite = 1
        df = {"Autor": [], "Contador": []}
        for autor, contador in recuentos.items():
            if limite > 4:
                break
            df["Autor"].append(autor)
            df["Contador"].append(contador)
            limite += 1
        dfreport = pd.DataFrame(df)
        sns.barplot(x="Autor", y="Contador", data=dfreport)
        plt.show()
        plt.close()

    def reportes(self):
        while True:
            self.menu_reportes()
            try:
                usu_entrada = int(input("Eleccion del usuario:  "))
                match usu_entrada:
                    case 1:
                        print("REPORTE:Libros más prestados (popularidad de títulos)")
                        self.reporte1()
                    case 2:
                        print("Usuarios con más préstamos (eficiencia de lectura).")
                        self.reporte2()
                    case 3:
                        self.reporte3()
                    case 4:
                        self.reporte4()
                    case 5:
                        self.reporte5()
                    case 6:
                        self.reporte6()
                    case 7:
                        self.reporte7()
                    case 8:
                        self.reporte8()
                    case 9:
                        self.reporte9()
                    case 10:
                        self.reporte10()
                    case 11:
                        break
            except ValueError:
                print("ERROR : VALOR INGRESADO NO ES UN NUMERO")

    def guardar_archivo(self):
        try:

            def guardar_usuarios():
                filas = []
                for dni, user in self._usuarios.items():
                    filas.append(
                        [
                            dni,
                            user.nombre,
                            user.apellidos,
                            str(user.libros_prestados),
                            user.deuda,
                            user.cant_prestamos,
                        ]
                    )

                df = pd.DataFrame(
                    filas,
                    columns=[
                        "DNI",
                        "Nombre",
                        "Apellido",
                        "Libros prestados",
                        "Deuda",
                        "Cantidad de prestamos",
                    ],
                )
                df.to_csv("usuarios.csv", index=False)

            def guardar_libros():
                filas = []
                for codigo, libro in self._libros.items():
                    filas.append(
                        [
                            codigo,
                            libro.titulo,
                            libro.autor,
                            libro.anio_pub,
                            libro.estado,
                            libro.contador_pres,
                        ]
                    )

                df = pd.DataFrame(
                    filas,
                    columns=[
                        "Codigo",
                        "Nombre",
                        "Autor",
                        "Año de publicacion",
                        "Estado",
                        "Contador de prestamos",
                    ],
                )
                df.to_csv("libros.csv", index=False)

            def guardar_prestamos():
                filas = []
                for prest in self._prestamos:
                    filas.append(
                        [
                            prest.usuario.dni,
                            prest.libro.codigo,
                            str(prest.fecha_prestamo),
                            str(prest.fecha_dev_estimada),
                            str(prest.fecha_dev_real),
                            prest.devuelto,
                            prest.multa,
                        ]
                    )

                df = pd.DataFrame(
                    filas,
                    columns=[
                        "DNI",
                        "Codigo",
                        "Fecha prestamo",
                        "Fecha estimada",
                        "Fecha real",
                        "Devuelto",
                        "Multa",
                    ],
                )
                df.to_csv("prestamos.csv", index=False)

            guardar_usuarios()
            guardar_libros()
            guardar_prestamos()
            print("Datos guardados correctamente en CSV.")
        except FileNotFoundError:
            print("Archivo no encontrado")

    def cargar_archivo(self):
        try:

            def str_a_tupla(texto):
                texto = texto.replace("(", "").replace(")", "")
                partes = texto.split(",")
                if len(partes) != 3:
                    return None
                return (int(partes[0]), int(partes[1]), int(partes[2]))

            def cargar_usuarios():
                df = pd.read_csv("usuarios.csv")
                for i in df.index:
                    dni = int(df.loc[i, "DNI"])
                    nom = df.loc[i, "Nombre"]
                    ape = df.loc[i, "Apellido"]

                    user = Usuario(dni, nom, ape)

                    lista = df.loc[i, "Libros prestados"]
                    lista = lista.replace("[", "").replace("]", "").strip()

                    codigos = []
                    if lista != "":
                        partes = lista.split(",")
                        for p in partes:
                            codigos.append(int(p))

                    user.libros_prestados = codigos
                    user.deuda = int(df.loc[i, "Deuda"])
                    user.cant_prestamos = int(df.loc[i, "Cantidad de prestamos"])

                    self.usuarios[dni] = user

            def cargar_libros():
                df = pd.read_csv("libros.csv")
                for i in df.index:
                    codigo = int(df.loc[i, "Codigo"])
                    libro = Libro(
                        codigo,
                        df.loc[i, "Nombre"],
                        df.loc[i, "Autor"],
                        int(df.loc[i, "Año de publicacion"]),
                    )
                    libro.estado = df.loc[i, "Estado"]
                    libro.contador_pres = int(df.loc[i, "Contador de prestamos"])
                    self.libros[codigo] = libro

            def cargar_prestamos():
                df = pd.read_csv("prestamos.csv")
                for i in df.index:
                    dni = int(df.loc[i, "DNI"])
                    codigo = int(df.loc[i, "Codigo"])
                    user = self.usuarios[dni]
                    libro = self.libros[codigo]

                    f_p = str_a_tupla(df.loc[i, "Fecha prestamo"])
                    prest = Prestamo(user, libro, f_p)

                    prest.fecha_dev_estimada = str_a_tupla(df.loc[i, "Fecha estimada"])

                    real = str(df.loc[i, "Fecha real"])
                    if real != "None":
                        prest.fecha_dev_real = str_a_tupla(real)

                    multa = int(df.loc[i, "Multa"])
                    prest.multa = multa

                    devuelto_bool = bool(df.loc[i, "Devuelto"])
                    prest.devuelto = devuelto_bool

                    if devuelto_bool:
                        libro.estado = "disponible"

                        if libro.codigo in user.libros_prestados:
                            user.libros_prestados.remove(libro.codigo)

                        if libro.contador_pres > 0:
                            libro.contador_pres -= 1
                        if user.cant_prestamos > 0:
                            user.cant_prestamos -= 1

                    self.prestamos.append(prest)

            cargar_usuarios()
            cargar_libros()
            cargar_prestamos()
            print("Datos cargados correctamente desde CSV.")
        except FileNotFoundError:
            print("Archivo no encontrado")


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
                    biblioteca.reportes()
                case 7:
                    biblioteca.cargar_archivo()
                case 8:
                    biblioteca.guardar_archivo()
                case 9:
                    print("Fin del Programa")
                    break
        except ValueError:
            print("ERROR : VALOR INGRESADO NO ES UN NUMERO")


main()
