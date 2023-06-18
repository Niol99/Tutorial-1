# # suma

# saludos , almacenamos usuario.  solicitar datos , revisar acceso , numero 1 , continua,  numero 2, operacion, respeusta final y despedida.  


print("Hola, bienvenido")

# almacenamiento de usuario y contraseña

my_usuario = "Nicolas"
my_contraseña = "9508"

#soliticaremos a la persona a digitar el usuario 

usuario = input("usuario:")
contraseña = input("contraseña:")

#condicionamos para permitir o negar procedimiento

if usuario == my_usuario and contraseña == my_contraseña:
    print("los datos son correctos")
    print("puede continuar para realizar la operacion")

    #operacion
     
    number1 = int(input("Digite el primer numero: "))
    print("Perfecto, sigamos") 
    number2 = int(input("Ahora digite el segundo numero: "))

    suma = number1 + number2  

    #resultado

    print(my_usuario , "el resultado de la suma fue: " , suma)
    print("!gracias por usar nuestra app, que vuelvas !")

else:
     print("las credenciales son incorrectas, vuelva a intentar")







# saludos , almacenamos usuario.  solicitar datos , revisar acceso , numero 1 , continua,  numero 2, operacion, respeusta final y despedida.  

print("Hola, Bienvenido ")

my_usuario = "Nicolas" 
my_contraseña = "9508"

usuario = input("Por favor su usuario: ")
contraseña = input("Por fa vor digite su contraseña: ")

if my_usuario == usuario and my_contraseña == contraseña: 
     print("a iniciado sesion correctamente")

     print("operaciones disponibles: ")
     print("1. suma")
     print("2. resta")
     print("3. division")
     print("4. multiplicacion")

     opcion = int(input("seleccione una opcion (1-4)"))

     numero1 = int(input("Digite por favor el primer numero "))
     numero2 = int(input("Digite por favor el segundo numero "))

     # la secuencia con if/elif/else 

     if   opcion == 1 :
          resultado = numero1 + numero2 
          operacion = "suma" 
     elif opcion == 2: 
          resultado = numero1 - numero2 
          operacion = "resta"
     elif opcion == 3:
          if numero2 != 0:
               resultado = numero1 / numero2
               operacion = "division"  

               # exit() sirve para terminar 
          else:
               print("Error: no se puede dividir entre cero.")
               exit()
     elif opcion == 4: 
          resultado = numero1 * numero2
          operacion = "multiplicacion"  

     else : 
          print("Opcion invalida. por favor, seleccione una opcion valida.")
          exit()

     print(usuario, " el resultado de la ", operacion, "es", resultado )

if resultado >= 4 :
               print("acabas de sumar un numero muuuuy grande, felicitaciones")
               print("Gracias por usar nuestra app, que vuelvas!")



else : 
     print ("las credenciales son incorrectas. vuelva a intentar")

     print("probando una historia para instagram")



 



















  















          











 



