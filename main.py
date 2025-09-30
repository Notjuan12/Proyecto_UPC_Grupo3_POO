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


def menu_reportes():
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
 |           | 7.                       Regresar al menu                         |           |
 |           ---------------------------------------------------------------------           |
 +-------------------------------------------------------------------------------------------+
"""
    )


# funciones auxiliares
def ver_nombre(n_evaluar):
    no_valido = False
    for letra in n_evaluar:
        if not (letra.isalpha() or letra == ""):
            no_valido = True
            break
    return no_valido


def or_pres(valor):
    return valor[1][6]


def or_pres_per(valor):
    return valor[1][4]


def or_deuda(valor):
    return valor[1][3]


# Reportes


def reporte1(libros):
    reporte_1 = dict(sorted(libros.items(), key=or_pres, reverse=True))
    imprimir_libros(reporte_1, 0, len(libros), 2)


def reporte2(personas):
    reporte_2 = dict(sorted(personas.items(), key=or_pres_per, reverse=True))
    imprimir_usuarios(reporte_2, 0, len(personas), 1)


def reporte3(reporte3_list):
    try:
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
        print("_____________________________________" * 3)
        print(" " * 20, end="")
        print(
            f"Tiempo promedio de préstamo por libro:\
            {sum(reporte3_list)/len(reporte3_list):.2f} dias "
        )
        recuentos = dict()
        for num in reporte3_list:
            recuentos[num] = recuentos.get(num, 0) + 1

        print("_____________________________________" * 3)
        print(" " * 20, end="")
        print("               Cantidad Promedio de Horas")
        print("_____________________________________" * 3)
        for clave, valor in recuentos.items():
            print(f"Cantidad de horas => {clave}      | recuento => {valor}")
        print("_____________________________________" * 3)
        input("Enter para continuar")
    except ZeroDivisionError:
        print(" " * 20, end="")
        print("Datos no disponibles")
        print("_____________________________________" * 3)
        input("Enter para continuar")


def reporte4(usuarios):
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
    list_llaves = list(usuarios.keys())
    mora_suma = 0
    for x in range(len(usuarios)):
        mora_suma += usuarios[list_llaves[x]][3]
    print("_____________________________________" * 3)
    print(" " * 30, end="")
    print(f"Recaudación por penalidades: S/.{mora_suma}")
    print("_____________________________________" * 3)
    reporte_4 = dict(sorted(usuarios.items(), key=or_deuda, reverse=True))
    list_llaves = list(reporte_4.keys())
    print(" " * 30, end="")
    print("TOP DEUDORES")
    for x in range(min(3, len(reporte_4))):
        print(" " * 15, end="")
        print(
            f"TOP {x+1} :  DNI:{list_llaves[x]}    /{reporte_4[list_llaves[x]][0]:^15}\
Deuda:{reporte_4[list_llaves[x]][3]}"
        )
    print("_____________________________________" * 3)
    input("Enter para continuar")


def reporte5(libros):
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
    for libro in libros.values():
        if libro[3] == "disponible":
            aux_dis += 1
        else:
            aux_pres += 1
    print("_____________________________________" * 3)
    print(" " * 30, end="")
    print("LIBROS DISPONIBLES VS LIBROS PRESTADOS ")
    print("_____________________________________" * 3)
    print(" " * 30, end="")
    print(f"LIBROS TOTALES :  {len(libros)} ")
    print("_____________________________________" * 3)
    print()
    print(
        f"LIBROS DISPONIBLES : {int(aux_dis/len(libros)*100) * "*"}:{aux_dis/len(libros)*100:.2f}%"
    )
    print(
        f"LIBROS PRESTADOS   : {int(aux_pres/len(libros)*100) * "*"}:{aux_pres/len(libros)*100:.2f}%"
    )
    print("_____________________________________" * 3)
    input("Enter para continuar")


def reporte6(libros):
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
        for x in libros.values():
            annios_list.append(x[2])
        for num in annios_list:
            recuentos[num] = recuentos.get(num, 0) + 1

        print("_____________________________________" * 3)
        print(" " * 20, end="")
        print("               Recuento de Fechas de Publicacion")
        print("_____________________________________" * 3)
        for clave, valor in recuentos.items():
            print(f"Fecha => {clave}      | recuento => {valor}")
        print("_____________________________________" * 3)
        input("Enter para continuar")
    except ZeroDivisionError:
        print(" " * 20, end="")
        print("Datos no disponibles")
        print("_____________________________________" * 3)
        input("Enter para continuar")


# funcion para imprimir usuarios en un rango definido
# modo = 1 es para imprimir lo necesario en el reporte 2
def imprimir_usuarios(usuarios, min_ran=0, max_ran=0, modo=0):
    list_llaves = list(usuarios.keys())
    try:
        print(
            "  DNI        NOMBRE(S)           APELLIDO(S)      CANT_PRESTAMOS(ACTUALES)",
            end="",
        )
        if modo == 0:
            print()
            for x in range(min_ran, min(20, max_ran)):
                print(
                    f"{list_llaves[x]} {usuarios[list_llaves[x]][0]:^15} \
        {usuarios[list_llaves[x]][1]:^5}\
        {len(usuarios[list_llaves[x]][2]):^10}"
                )
        if modo == 1:
            print("        CANT_TOTAL_PRESTAMOS     MERITO")
            for x in range(min_ran, min(20, max_ran)):
                print(
                    f"{list_llaves[x]} {usuarios[list_llaves[x]][0]:^15} \
        {usuarios[list_llaves[x]][1]:^5}\
        {len(usuarios[list_llaves[x]][2]):^10}\
        {usuarios[list_llaves[x]][4]:>20}   {x+1:>15}"
                )
    except IndexError:
        print("Se mostro los resultados posibles:")
        print(f"ERROR : FUERA DE RANGO , Rango Maximo :{len(usuarios)}")


# funcion para imprimir u en un rango definido
# modo = 0 es para imprimir todo
# modo = 1 es para imprimir solo los disponibles
# modo = 2 es para imprimir lo necesario en el reporte 1
def imprimir_libros(libros, min_ran=0, max_ran=0, modo=0):
    list_llaves = list(libros.keys())
    try:
        print(
            "CODIGO          NOMBRE                "
            " AUTOR                 AÑO                   ESTADO",
            end="",
        )
        if modo == 0:
            print()
            for x in range(min_ran, min(20, max_ran)):
                print(
                    f"{list_llaves[x]:^5} {libros[list_llaves[x]][0]:>16} \
                {libros[list_llaves[x]][1]:>0} \
                {libros[list_llaves[x]][2]:>2} \
                {libros[list_llaves[x]][3]:>2}"
                )
        elif modo == 1:
            print()
            for x in range(min_ran, min(20, max_ran)):
                if "disponible" in libros[list_llaves[x]]:
                    print(
                        f"{list_llaves[x]:^5} {libros[list_llaves[x]][0]:>16} \
                {libros[list_llaves[x]][1]:>0} \
                {libros[list_llaves[x]][2]:>2} \
                {libros[list_llaves[x]][3]:>2}"
                    )
        elif modo == 2:
            print("       MERITO      Cant_Prestamos")
            for x in range(min_ran, min(20, max_ran)):
                print(
                    f"{list_llaves[x]:^5} {libros[list_llaves[x]][0]:>16} \
                {libros[list_llaves[x]][1]:>0} \
                {libros[list_llaves[x]][2]:>2} \
                {libros[list_llaves[x]][3]:>2} \
      {x+1}       {libros[list_llaves[x]][6]:>10}"
                )
    except IndexError:
        print("Se mostro los resultados posibles:")
        print(f"ERROR : FUERA DE RANGO , Rango Maximo :{len(libros)}")


# funciones de tiempo
def es_bisiesto(annio):
    return (annio % 4 == 0 and annio % 100 != 0) or (annio % 400 == 0)


def dias_en_mes(mes, annio):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if es_bisiesto(annio):
            return 29
        else:
            return 28
    return 0


def fecha_valida(dia, mes, annio):
    bisiesto = es_bisiesto(annio)

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


# suponiendo que cada mes tiene 30 dias
def cal_f_entrega(actual):
    dia, mes, annio = actual
    bisiesto = (annio % 400 == 0) or (annio % 4 == 0 and annio % 100 != 0)
    dia += 7
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        if dia > 31:
            mes += 1
            dia %= 31
    elif mes in [4, 6, 9, 11]:
        if dia > 30:
            mes += 1
            dia %= 30
    elif mes == 2:
        if bisiesto:
            if dia > 29:
                mes += 1
                dia %= 29
        elif dia > 28:
            mes += 1
            dia %= 28

    if mes > 12:
        annio += 1
        mes %= 12
    return [dia, mes, annio]


def f_penal_v(actual, limite):
    resultado = False
    dia, mes, annio = actual
    dia_l, mes_l, annio_l = limite

    if annio > annio_l:
        resultado = True
    elif annio == annio_l:
        if mes > mes_l:
            resultado = True
        elif mes == mes_l:
            if dia >= dia_l:
                resultado = True

    return resultado


def cal_mora(fecha):
    dia, mes, annio = fecha
    total_dias = 0
    for anio in range(1, annio):
        if es_bisiesto(anio):
            total_dias += 366
        else:
            total_dias += 365

    for mes_ in range(1, mes):
        total_dias += dias_en_mes(mes_, annio)

    total_dias += dia

    return total_dias


# funciones del menu
def reg_usuario(usuarios):
    dni = 0
    try:
        while True:
            dni = int(input("Ingrese el dni del cliente: "))
            if dni not in usuarios and len(str(dni)) == 8:
                print("DNI asignado correctamente")
                break
            elif dni in usuarios:
                print(f"Persona ya registrada con el dni:{dni}")
            else:
                print("DNI NO VALIDO")
        while True:
            nombre = input("Nombre(s) de la persona: ")
            if ver_nombre(nombre):
                print("Nombre no valido")
            else:
                print("Nombre(s) asignado correctamente")
                break
        while True:
            apellidos = input("Apellido(s) de la persona: ")
            if ver_nombre(apellidos):
                print("Apellido no valido")
            else:
                print("Apellido(s) asignado correctamente")
                break
        usuarios.update({dni: [nombre.title(), apellidos.title(), [], 0, 0]})

    except ValueError:
        print("ERROR: VALOR INGRESADO NO VALIDO")


def reg_libro(libros):
    codigo = 0
    try:
        while True:
            codigo = int(input("Ingrese el codigo del libro: "))
            if codigo in libros:
                print("Codigo de libro ya asignado")
            else:
                print("Codigo asignado correctamente")
                break

        nombre = input("Nombre del libro: ")

        while True:
            autor = input("Nombre del autor: ")
            if ver_nombre(autor):
                print("Nombre no valido")
            else:
                print("Autor asignado correctamente")
                break
        anio = int(input("año de publicacion: "))
        libros.update(
            {
                codigo: [
                    nombre.title(),
                    autor.title(),
                    anio,
                    "disponible",
                    [0, 0, 0],
                    [0, 0, 0],
                    0,
                ]
            }
        )
        print(f"Libro ID:{codigo} ha sido registrado con exito")
    except ValueError:
        print("ERROR: VALOR INGRESADO NO VALIDO")


def pres_lib(usuarios, libros):
    try:
        while True and len(usuarios) > 0:
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
                            while True:
                                print("Ingreso de fecha de prestamo:")
                                dia = int(input("Dia: "))
                                mes = int(input("Mes:"))
                                annio = int(input("Año:"))
                                if fecha_valida(dia, mes, annio):
                                    break
                                else:
                                    print("Fecha invalida")
                            libros[usu_entrada][4][0] = dia
                            libros[usu_entrada][4][1] = mes
                            libros[usu_entrada][4][2] = annio
                            libros[usu_entrada][3] = "prestado"
                            usuarios[dni][4] += 1  # cant_prestamos
                            usuarios[dni][2].append(usu_entrada)
                            print("-----------------Resumen-----------------")
                            print(f"        {dia} / {mes} / {annio}")
                            print(f"        DNI:{dni}")
                            print(f"        NOMBRE:{usuarios[dni][0]}")
                            print(f"        APELLIDOS:{usuarios[dni][1]}")
                            print(f"        CODIGO:{usu_entrada}")
                            print("------------------------------------------")
                            print("Prestamo realizado con exito")
                            dia, mes, annio = cal_f_entrega([dia, mes, annio])
                            libros[usu_entrada][5][0] = dia
                            libros[usu_entrada][5][1] = mes
                            libros[usu_entrada][5][2] = annio
                            print(f"fecha de devolucion estimada : {dia} {mes} {annio}")
                        else:
                            print("no disponible")
                    else:
                        print("El codigo ingresado no existe")
                else:
                    print("Maximo de 3 prestamos por persona")
            elif dni == 0:
                break
            else:
                print("No hay dni registrado")

    except ValueError:
        print("Error de ingreso de datos")


def devol_lib(usuarios, libros, reporte3_list):
    try:

        while True and len(usuarios) > 0:
            print("Sistema de devolucion de libros:")
            dni = int(
                input("Ingrese el DNI de la persona que va a devolver (0 = salir): ")
            )

            if dni in usuarios:
                if len(usuarios[dni][2]) == 0:
                    print("Este usuario no tiene libros prestados.")
                    continue

                print("DNI válido.")
                print(f"Libros prestados por {usuarios[dni][0]} {usuarios[dni][1]}:")

                for cod in usuarios[dni][2]:
                    print(
                        f"  Código: {cod} | Título: {libros[cod][0]} | Autor: {libros[cod][1]}"
                    )

                usu_entrada = int(input("Ingrese el código del libro a devolver: "))

                if usu_entrada in usuarios[dni][2]:
                    while True:
                        print("Ingrese la fecha de devolución:")
                        dia = int(input("Dia: "))
                        mes = int(input("Mes: "))
                        annio = int(input("Año: "))
                        if fecha_valida(dia, mes, annio) and f_penal_v(
                            [dia, mes, annio], libros[usu_entrada][5]
                        ):
                            break
                        else:
                            print("Fecha invalida")
                    #  fecha limite - fecha actual
                    dias_mora = cal_mora(libros[usu_entrada][5]) - cal_mora(
                        [dia, mes, annio]
                    )
                    # diferencia de dias desde el prestamo y la devolucion
                    reporte3_list.append(
                        max(
                            0,
                            (
                                cal_mora(libros[usu_entrada][4])
                                - cal_mora([dia, mes, annio])
                            ),
                        )
                    )
                    mora = max(0, dias_mora)
                    mora = mora * 10
                    usuarios[dni][3] += mora
                    # actualizar libro
                    libros[usu_entrada][3] = "disponible"
                    libros[usu_entrada][4] = [0, 0, 0]  # limpiar fecha

                    # eliminar de la lista del usuario
                    usuarios[dni][2].remove(usu_entrada)

                    print("-----------------Resumen-----------------")
                    print(f"        {dia} / {mes} / {annio}")
                    print(f"        DNI: {dni}")
                    print(f"        NOMBRE: {usuarios[dni][0]}")
                    print(f"        APELLIDOS: {usuarios[dni][1]}")
                    print(f"        CODIGO DEVUELTO: {usu_entrada}")
                    print(f"        TITULO: {libros[usu_entrada][0]}")
                    print("------------------------------------------")
                    print("Devolución realizada con éxito")

                else:
                    print("El código ingresado no pertenece a este usuario.")

            elif dni == 0:
                break
            else:
                print("No hay DNI registrado")

    except ValueError:
        print("Error de ingreso de datos")


def cal_penalidad():
    try:
        while True:
            print("Bienvenido al simulador de calculo de penalidad:")
            user = input("Desea estimar la mora (S: salir /cualquier tecla :continuar)")
            if user.upper() == "S":
                break
            while True:
                print("Ingrese la fecha actual a tomar como inicio:")
                dia_actual = int(input("Dia: "))
                mes_actual = int(input("Mes: "))
                annio_actual = int(input("Año: "))
                if fecha_valida(dia_actual, mes_actual, annio_actual):
                    break
                else:
                    print("Fecha no valida")
            dia_actual, mes_actual, annio_actual = cal_f_entrega(
                [dia_actual, mes_actual, annio_actual]
            )
            print("Recuerde : la mora empieza luego de 7 dias de inicio")
            while True:
                print("Ingrese la fecha de devolucion:")
                dia_dev = int(input("Dia: "))
                mes_dev = int(input("Mes: "))
                annio_dev = int(input("Año: "))
                if fecha_valida(dia_actual, mes_actual, annio_actual):
                    break
                else:
                    print("Fecha no valida")

            if f_penal_v(
                [dia_actual, mes_actual, annio_actual], [dia_dev, mes_dev, annio_dev]
            ):
                print("No valido , volver a ingresar fechas")
                continue
            else:
                dias_mora = cal_mora([dia_dev, mes_dev, annio_dev]) - cal_mora(
                    [dia_actual, mes_actual, annio_actual]
                )
                mora = max(0, dias_mora)
                mora = mora * 10
                print(
                    f"Mora estimada luego del {dia_actual}/ {mes_actual}/{annio_actual} de {dias_mora} dias es de : S/.{mora}"
                )
    except ValueError:
        print("ERROR")


def ver_reports(usuarios, libros, reporte3_list):
    while True:
        menu_reportes()
        try:
            usu_entrada = int(input("Eleccion del usuario:  "))
            match usu_entrada:
                case 1:
                    print("REPORTE:Libros más prestados (popularidad de títulos)")
                    reporte1(libros)
                case 2:
                    print("Usuarios con más préstamos (eficiencia de lectura).")
                    reporte2(usuarios)
                case 3:
                    reporte3(reporte3_list)
                case 4:
                    reporte4(usuarios)
                case 5:
                    reporte5(libros)
                case 6:
                    reporte6(libros)
                case 7:
                    break
        except ValueError:
            print("ERROR : VALOR INGRESADO NO ES UN NUMERO")


def menu(libros, usuarios, reporte3_list):
    while True:
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
                    devol_lib(usuarios, libros, reporte3_list)
                case 5:
                    cal_penalidad()
                case 6:
                    ver_reports(usuarios, libros, reporte3_list)
                case 7:
                    print("Fin del Programa")
                    break
        except ValueError:
            print("ERROR : VALOR INGRESADO NO ES UN NUMERO")


def main():
    # datos generales / libros / usuarios
    # Libros {"codigo":["nombre","autor","año","estado(disponible/prestado)",["dia","mes","año"]]}
    libros = {1: ["El Gato", "Juan", 2025, "disponible", [0, 0, 0], [0, 0, 0], 0]}
    # Usuarios {"DNI": ["nombre","Apellidos",[zona de libros prestados x codigo],deuda,c_prestamos]}
    usuarios = {70479564: ["Juan", "Espinoza Ramos", [], 0, 0]}
    # reportes_list [dias por diferencia entre fecha prestamo y entrega ]
    reporte3_list = []
    menu(libros, usuarios, reporte3_list)


main()
