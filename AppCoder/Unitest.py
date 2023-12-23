class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def obtener_nombre(self):
        return self.nombre
        
user = Usuario("Olivia")
nombre = user.obtener_nombre()

if nombre == "Olivia":
    print("prueba exitosa")
else:
    print("prueba fallida")
    
    
##############

def sumar(a, b):
    return a + b

resultado = sumar(10, 9)

if resultado == 19:
    print("Prueba exitosa")
else:
    print("Prueba fallida")
    

##############

def calcular(numero1, numero2, operacion):
    if operacion == "+":
        return numero1 + numero2
    elif operacion =="-":
        return numero1 - numero2
    elif operacion ==":":
        return numero1 / numero2


resultado = calcular(10, 9 "+"):
    
    if resultado == 19:
        print("ok")
    else:
        print("falló")

##########################
        
resultado = calcular(100, 10 "*")
    
    if resultado == 1000:
        print("ok")
    else:
        print(f"falló {resultado}")