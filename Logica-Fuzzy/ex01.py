'''
    PASSO 1: Fuzzyficar
        * Tornar nebulosos os valores de entrada nítidos.
        * Iemos definir o valores de pertinência a partir dos valores de entrada:
            => Pressão no pedal do freio, Velocidade da roda, Velocidade do carro.
'''


#Veridicando os valores de pertinência nebulosos:

# Função para cálculo do valor de pertinência da pressão no pedal baixo (L).
# Sabendo que L = {(0,1), (50,0)}
# x = Valor da pressão no pedal
# Foi-se utilizada a Função trapezoidal
def valor_min_PRESSAO(x, a=0, b=50):
    res_min = (b-x)/(b-a)
    if res_min < 0:
        return 0
    else:
        return res_min

# Função para cálculo do valor de pertinência da pressão no pedal médio(M).
# Sabendo que M = {(30,0), (50,1), (70,0)}
# x = Valor da pressão no pedal
# Foi-se utilizada a Função Triangular
def valor_medio_PRESSAO(x, a=30, b=50, c=70):
    aux1 = (x-a) / (b-a)
    aux2 = (c-x) / (c-b)
    res_medio = max(min(aux1, aux2), 0)
    return res_medio


# Função para cálculo do valor de pertinência da pressão no pedal alto(H).
# Sabendo que H = {(50,0), (100,1)}
# x = Valor da pressão no pedal
# Foi-se utilizada a Função Trapezoidal
def valor_max_PRESSAO(x, a=50, b=100):
    res_max = (a-x)/(a-b)
    if res_max < 0:
        return 0
    else:
        return res_max


# Função para cálculo do valor de pertinência da velocidade da roda e do carro devagar(S).
# Sabendo que S = {(0,1), (60,0)}
# x = Valor da velocidade da roda ou valor da velocidade do carro
# Foi-se utilizada a Função trapezoidal
def valor_min_VELOCIDADE(x, a=0, b=60):
    res_min = (b-x)/(b-a)
    if res_min < 0:
        return 0
    else:
        return res_min


# Função para cálculo do valor de pertinência da velocidade da roda e do carro médio(M).
# Sabendo que S = {(0,1), (60,0)}
# x = Valor da velocidade da roda ou valor da velocidade do carro
# Foi-se utilizada a Função Triangular
def valor_medio_VELOCIDADE(x, a=20, b=50, c=80):
    aux1 = (x-a) / (b-a)
    aux2 = (c-x) / (c-b)
    res_medio = max(min(aux1, aux2), 0)
    return res_medio

# Função para cálculo do valor de pertinência da velocidade da roda e do carro rápido(F).
# Sabendo que S = {(40,0), (100,1)}
# x = Valor da velocidade da roda ou valor da velocidade do carro
# Foi-se utilizada a Função Triangular
def valor_max_VELOCIDADE(x, a=40, b=100):
    res_max = (a-x)/(a-b)
    if res_max < 0:
        return 0
    else:
        return res_max