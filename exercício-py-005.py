#função para definir se o número é impar ou par
def func_imp_par():
    if  resultado % 2 != 0:
        return ("impar")
    else:
        return ("par")
    
#função para definir se o número é negativo ou positivo
def func_neg_pos():
    if resultado < 0:
        return ("negativo")
    else:
        return ("positivo")
    
#função para definir se o número é decimal ou inteiro
def func_decimal():
    if resultado != int(resultado):
        return ("decimal")
    else:
        return ('inteiro')
    

#funções para definir as operações selecionadas
def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero."
    
#selecione os número
a = float(input("Insira o primeiro número: "))
b = float(input("Insira o segundo número: "))

#selecione qual operação deseja fazer 
operação = input("Insira a operação que deseja realizar(soma,subtração,divisão ou multiplicação): ")

if operação == "soma":
    resultado = soma(a, b)
    print(f"Resultado: {resultado}")
elif operação == "subtração":
    resultado = subtração(a, b)
    print(f"Resultado: {resultado}")
elif operação == "multiplicação":
    resultado = multiplicação(a, b)
    print(f"Resultado: {resultado}")
elif operação == "divisão":
    resultado = divisão(a, b)
    print(f"Resultado: {resultado}")
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")

print("O número",resultado,"é", func_imp_par(),",", func_neg_pos(), "e",func_decimal(),"." )