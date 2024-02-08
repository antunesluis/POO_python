multiplicador = 10 
divisao_Max = 11
soma = 0 

cpf = input("Digite o cpf: ")
cpf = cpf.replace(".", "").replace("-", "")

for i in range(9): 
    soma += int(cpf[i]) * multiplicador
    multiplicador -= 1 

resto = soma % divisao_Max 
primeiro_digito = divisao_Max - resto if resto > 1 else 0

multiplicador = 11
soma = 0 

for i in range(10):
    soma += int(cpf[i]) * multiplicador
    multiplicador -= 1
resto = soma % divisao_Max
segundo_digito = divisao_Max - resto if resto > 1 else 0

if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
    print("CPF VALIDO")
else:
    print("CPF INVALIDO")