import random #libreria (modulo) de aleatoriedad

# crear el banco, elegir palabra aleatoria y volverla list 
banco = ["juego", "vocal", "torso", "vivaz", "palco", "trono", "dormi", "limon", "cinco"]
sln = random.choice(banco)
sln_ = list(sln)

'''
# para ver la palabra a resolver(sln) y sus letras(sln_) 
print(sln)
print(sln_, "\n")
'''
t = True
k=0
while t:
    k+=1
    if k == 7:  #si el intento se pasa del 6 intento
        
        print("\nAgotaste tus intentos. La palabra era", sln)
        break
    
    print ("__ Intento",k,"__\n")
    plb = list(input("Ingrese la palabra:"))
    
    if plb == sln_: #si la palabra ingresada(plb) es la palabra a resolver(sln)
        print("\nFelicidades, ganaste!!!! La palabra era", sln)
        break
    
    if len(plb) != 5: #si la palabra no tiene cinco letras
        print ("Tu intento debe ser de 5 letras\n")
        k-=1 #para que el numero del intento no aumente
        
    else: #el proceso de mostrar el resultado de ingresar plb -----------
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
            

        for x in letras:
            print(x, end="")
        print("\n")
