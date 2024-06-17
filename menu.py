from os import system
def menu_principal():
    opciones = {
        '1': ('Registrar trabajador', regTrabajador),
        '2': ('Listar todos los trabajadores', listEmpleados),
        '3': ('Imprimir planilla de sueldos', printSueldos),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        system("cls")
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print() # se imprime una línea en blanco para clarificar la salida por pantalla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def regTrabajador():
    bucle = True
    name = input(f'Ingrese nombre y apellido: ')
    cargo = input(f'Ingrese su cargo en la empresa: ')
    sBruto = int(input(f'Ingrese su sueldo bruto: '))
    descSalud = sBruto * 7 / 100
    descAFP = sBruto * 12 / 100
    sLiquido = sBruto + descSalud + descAFP
    lista_empleados.append({
        "Nombre Empleado": name,
        "Cargo en la Empresa": cargo,
        "Sueldo Bruto": sBruto,
        "Descuento Salud": descSalud,
        "Descuento AFP": descAFP,
        "Sueldo Liquido": sLiquido,
    })


def listEmpleados():
    print('Has elegido la opción 2')


def printSueldos():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')

lista_empleados = []
menu_principal()

