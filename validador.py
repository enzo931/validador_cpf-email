import re

def validar_email(email):
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao_email, email)

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', cpf)
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Valida os dois dígitos verificadores
    def calcular_digito(cpf, peso):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf, range(peso, 1, -1)))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    digito1 = calcular_digito(cpf[:9], 10)
    digito2 = calcular_digito(cpf[:10], 11)

    return cpf[-2:] == f"{digito1}{digito2}"

# Interface
print("=== Validador de CPF e E-mail ===")
escolha = input("Você quer validar um [1] CPF ou [2] E-mail? ")

if escolha == '1':
    cpf = input("Digite o CPF (com ou sem pontuação): ")
    if validar_cpf(cpf):
        print("✅ CPF válido!")
    else:
        print("❌ CPF inválido.")
elif escolha == '2':
    email = input("Digite o e-mail: ")
    if validar_email(email):
        print("✅ E-mail válido!")
    else:
        print("❌ E-mail inválido.")
else:
    print("Opção inválida.")
