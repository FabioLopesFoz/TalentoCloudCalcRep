def calculadoraMat(fun, num1, num2):
    if (fun == 1):
        res = num1+num2
    elif(fun == 2):
        res = num1-num2
    elif(fun == 3):
        res = num1*num2
    elif(fun == 4):
        res = num1/num2
    return res
exec = True
while (exec == True):
    print ("Opções: 1 - Soma -- 2 - Subtração -- 3 - Multiplicação -- 4 - Divisão -- 0 - Sair")
    fun = int(input("Digite a opção desejada: "))
    if (fun < 0) or (fun > 4):
        print("Essa opção não existe!")
    elif (fun == 0):
        exec = False
    else:
        num1 = int(input("Digite o Primeiro Valor: "))
        num2 = int(input("Digite o Segundo Valor: "))
        resultado = calculadoraMat(fun,num1,num2)
        print ("O resultado é: ", resultado)
