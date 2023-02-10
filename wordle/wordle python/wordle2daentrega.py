import random #libreria (modulo) de aleatoriedad

'''
# crear el banco, elegir palabra aleatoria y volverla list 
# banco = ["juego", "vocal", "torso", "vivaz", "palco", "trono", "dormi", "limon", "cinco"]
'''

# elegir configuracion
t = True
while t:
    b = int(input("¿Desea usar otro archivo de configuración? (1 SÍ - 0 NO) "))
    if b == 1:
        nomcfg = input("¿Cómo se llama tu archivo de configuración? ") 
        break
    elif b == 0:        
        nomcfg = "config.txt"
        break
    else:
        pass

# abrir la configuracion
cfg = open(nomcfg, "r")
configuracion = cfg.read()
cfg.close()

# conseguir los parametros definidos en el archivo de configuracion
parametros = configuracion.split("\n")
n_letras = int(parametros[0])
n_intentos = int(parametros[1])
banco = parametros[2]

# abrir archivo de las palabras y leer el banco de palabras
archivo = open(banco, "r")
banco_ = archivo.read()
archivo.close()

palabras = banco_.split(",")
#print(palabras)

#elegir palabra aleatoria de el banco de palabras 
sln = random.choice(palabras)
sln_ = list(sln)

"""
# para ver la palabra a resolver(sln) y sus letras(sln_) 
print(sln)
print(sln_, "\n")
"""

# WORDLE---------------------------------------------------------------------------

def wordle(plb):
    
        letras = [] # list para mostrar las letras ya clasificadas que ingrese el usuario, lo reiniciamos para cada plb
        letrasfalt = sln_.copy()
        indicescorrectos = []
        
        '''
        for lt in sln_:
            letrasfalt.append(lt)
            
        print(letrasfalt)    
        '''
        
        i=0
        for letra in plb:
            #print(letrasfalt, "faltantes")
            if letra == sln_[i]: #la letra esta en el espacio correcto
                letras.append(letra+"+")
                indicescorrectos.append(i) 
                if letrasfalt.count(letra)>0:
                    letrasfalt.remove(letra)
            else:
                letras.append("")
            i+=1         
            
        #print(letras, "correctas")
        
        i=0
        for letra in plb:
    
            if letra in sln_ and i not in indicescorrectos: #la letra esta en la palabra
                if letrasfalt.count(letra)>0:
                    if letras.count("")!=0:
                        p = letras.index("")
                        letras.pop(p)
                        letras.insert(p,letra+"*")
                    letrasfalt.remove(letra)
                    
                elif letrasfalt.count(letra)==0:
                    if letras.count("")!=0:
                        p = letras.index("")
                        letras.pop(p)
                        letras.insert(p,letra+"-")
                else:
                    p = letras.index("")
                    letras.pop(p)
                    letras.insert(p,letra+"*")
                    
            elif letra not in sln_: #la letra no esta en la palabra
                p = letras.index("")
                letras.pop(p)
                letras.insert(p,letra+"-")
            i+=1
            
        #guardar en el historial
        palabra = "".join(letras)
        
        historialR.append(str(k)+". "+palabra)
        
        #imprimir palabra revisada
        print(palabra,"\n")
    
#----------------------------------------------------------------------------------------------------------
historialR = []
historial = []
k=0

while k<= n_intentos + 1:
    k+=1
    
    if k == n_intentos + 1:  #si el intento se pasa del n_intentos intento      
        print("Agotaste tus intentos. La palabra era", sln, "\n")
        k-=1
        intCorr = "la palabra no fue encontrada"
        break
    
    print ("__ Intento",k,"__\n")
    plb_ = (input("Ingrese la palabra:"))
    plb = list(plb_)
    
    if plb == sln_: #si la palabra ingresada(plb) es la palabra a resolver(sln)
        print("\nFelicidades, ganaste!!!! La palabra era", sln, "\n")
        historial.append(plb_)
        intCorr = k
        break
    
    if len(plb) != n_letras: #si la palabra no tiene n_letras letras
        print ("Tu intento debe ser de", n_letras, "letras\n")
        k-=1 #para que el numero del intento no aumente  
        
    elif "".join(plb) not in palabras: #la palabra no esta en el banco de palabras
        print ("La palabra no hace parte de la lista. Intenta con otra\n")
        k-=1
        
    else: #mostrar el resultado de ingresar plb ------------------------------------------------------------
        historial.append(plb_)
        wordle(plb)
        
# HISTORIAL ------------------------------------------------------------------------------------------------
 
print("HISTORIAL\n")

print("Palabra objetivo:", sln+",", "Intentos", str(k)+":", ", ".join(historial),"\n")

for t in historialR:
    print(t)
print("\nNumero del Intento con palabra correcta:", intCorr)