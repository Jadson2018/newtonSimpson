import math
import time

def newtonCotes(funcao, a, b, n):
    h = (b - a) / n
    soma = 0
    x = a
    for i in range(n + 1):
        if i == 0 or i == n:
            soma += funcao(x)
        else:
            soma += 2 * funcao(x)
        x += h
    integral = (h / 2) * soma
    return round(integral, 14)

def simpson(funcao, a, b, n):
    h = (b - a) / n
    soma = 0
    x = a
    for i in range(n + 1):
        if i == 0 or i == n:
            soma += funcao(x)
        else:
            if i % 2 == 0:
                soma += 2 * funcao(x)
            else:
                soma += 4 * funcao(x)
        x += h
    integral = (h / 3) * soma
    return round(integral, 14)

def newtonCotesView(funcao, a, b, n):
    h = (b - a) / n
    soma = 0
    x = a
    saida = "Newton Cotes\n"
    saida += "h = " + str(b) + " - " + str(a) + " / " + str(n) + " = " + str(h) + "\n"
    saida += "(" + str(h) + "/2)x["
    for i in range(n + 1):
        if i == 0 or i == n:
            soma += funcao(x)
            saida += str(funcao(x))
        else:
            soma += 2 * funcao(x)
            saida += " + " + str(funcao(x))
        x += h
    integral = (h / 2) * soma
    saida += "]\n = " + str(h / 2) + " x " + str(soma) + "\n"
    saida += "Resultado: " + str(round(integral, 14))
    return saida

def simpsonView(funcao, a, b, n):
    h = (b - a) / n
    soma = 0
    x = a
    saida = "1/3 de Simpson\n"
    saida += "h = " + str(b) + " - " + str(a) + " / " + str(n) + " = " + str(h) + "\n"
    saida += "(" + str(h) + "/3)x["
    for i in range(n + 1):
        if i == 0 or i == n:
            soma += funcao(x)
            saida += str(funcao(x))
        else:
            if i % 2 == 0:
                soma += 2 * funcao(x)
                saida += " + 2x" + str(funcao(x))
            else:
                soma += 4 * funcao(x)
                saida += " + 4x" + str(funcao(x))
        x += h
    integral = (h / 3) * soma
    saida += "]\n = " + str(h / 3) + " x " + str(soma) + "\n"
    saida += "Resultado: " + str(round(integral, 14))
    return saida

def calcular(funcao):
    try:
        a = float(input("Digite o limite inferior (a): "))
        b = float(input("Digite o limite superior (b): "))
        nt = int(input("Quantidade de partições inicial: "))
        if nt <= 0:
            raise ValueError("O valor de n não pode ser menor ou igual a zero.")
        
        n = nt
        m = n
        contNewton = 0
        contSimpson = 0

        newton_cotes_result = newtonCotes(funcao, a, b, n)
        simpson_result = simpson(funcao, a, b, m)
        tempoInicio = time.time()
        
        while (newton_cotes_result != 0.60947570824873 or simpson_result != 0.60947570824873) and contNewton < 1000 and contSimpson < 1000:
            if newton_cotes_result != 0.60947570824873:
                n += 1
                newton_cotes_result = newtonCotes(funcao, a, b, n)
                contNewton += 1
            if simpson_result != 0.60947570824873:
                m += 1
                simpson_result = simpson(funcao, a, b, m)
                contSimpson += 1
        
        if newton_cotes_result == 0.60947570824873:
            print(newtonCotesView(funcao, a, b, n))
            print("Iterações:", contNewton)
            print("Convergiu para n =", n)
            tempoNewton = time.time() - tempoInicio
            print(f"Tempo de execução: {tempoNewton:.6f} segundos")
        else:
            print("Newton Cotes")
            print("Newton cotes não convergiu com menos de 1000 iterações para início de", n - contNewton, "intervalos")
        
        if simpson_result == 0.60947570824873:        
            print(simpsonView(funcao, a, b, m))
            print("Iterações:", contSimpson)
            print("Convergiu para n =", m)
            tempoSimpson = time.time() - tempoInicio
            print(f"Tempo de execução: {tempoSimpson:.6f} segundos")
        else:
            print("1/3 de simpson")
            print("1/3 de Simpson não convergiu com menos de 1000 iterações para início de", n - contSimpson, "intervalos")
        
    except ValueError as e:
        print(f"Erro: {e}")

def main():
    funcao_input = input("Digite a função em termos de x (ex: x * math.sqrt(1 + x**2)): ")
    funcao = lambda x: eval(funcao_input)
    calcular(funcao)

main()
