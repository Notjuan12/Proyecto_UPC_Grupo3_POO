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
    def libros_prestados(self):
        self._libros_prestados.copy()

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
        print(f"Libros prestados: {len(self._libros_prestados)}")
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

    def agregar_usuario(self, dni: int, nombre: str, apellidos: str):
        if dni in self._usuarios:
            print("El usuario ya está registrado.")
            return
        self._usuarios[dni] = Usuario(dni, nombre, apellidos)
        print(f"Usuario '{nombre} {apellidos}' agregado correctamente.")

    def agregar_libro(self, codigo: int, titulo: str, autor: str, anio_pub: int):
        if codigo in self._libros:
            print("El libro ya existe en la biblioteca.")
            return
        self._libros[codigo] = Libro(codigo, titulo, autor, anio_pub)
        print(f"Libro '{titulo}' agregado al catálogo.")

    def registrar_prestamo(
        self, dni_usuario: int, codigo_libro: int, fecha_prestamo: tuple[int, int, int]
    ):
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

        prestamo = Prestamo(usuario, libro, fecha_prestamo)
        self._prestamos.append(prestamo)
        print(
            f"Préstamo registrado: '{libro.titulo}' para {usuario._nombre} ({usuario._dni})"
        )
        print(f"Fecha estimada de devolución: {prestamo._fecha_dev_estimada}")

    def devolver_libro(
        self, dni_usuario: int, codigo_libro: int, fecha_real: tuple[int, int, int]
    ):
        for prestamo in self._prestamos:
            if (
                prestamo._usuario._dni == dni_usuario
                and prestamo._libro.codigo == codigo_libro
                and not prestamo._devuelto
            ):
                prestamo.devolver(fecha_real)
                return
        print("No se encontró un préstamo activo con esos datos.")

def main():
 # Crear la biblioteca
    biblioteca = Biblioteca()

    # Agregar usuarios
    biblioteca.agregar_usuario(12345678, "Juan", "Pérez")
    biblioteca.agregar_usuario(87654321, "María", "López")

    # Agregar libros
    biblioteca.agregar_libro(1, "Cien años de soledad", "Gabriel García Márquez", 1967)
    biblioteca.agregar_libro(2, "El Principito", "Antoine de Saint-Exupéry", 1943)
    biblioteca.agregar_libro(3, "1984", "George Orwell", 1949)

    # Registrar préstamos
    print("\n--- Registrar préstamos ---")
    biblioteca.registrar_prestamo(12345678, 1, (1, 11, 2025))
    biblioteca.registrar_prestamo(87654321, 2, (2, 11, 2025))

    # Mostrar estado de libros
    print("\n--- Estado de los libros ---")
    for libro in biblioteca._libros.values():
        libro.mostrar_info()

    # Devolver libros a tiempo
    print("\n--- Devolución a tiempo ---")
    biblioteca.devolver_libro(12345678, 1, (8, 11, 2025))  # devuelve justo 7 días después

    # Devolver con retraso
    print("\n--- Devolución con retraso ---")
    biblioteca.devolver_libro(87654321, 2, (15, 11, 2025))  # 6 días tarde

    # Mostrar información de usuarios
    print("\n--- Información de usuarios ---")
    for usuario in biblioteca._usuarios.values():
        usuario.mostrar_info()

    # Mostrar detalle de préstamos
    print("\n--- Detalle de préstamos ---")
    for prestamo in biblioteca._prestamos:
        prestamo.mostrar_info()
        print()
main()