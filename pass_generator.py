import hashlib, string, random

print("""
    ====================PassPy====================

    ===========Seja Bem-Vindo ao PassPy===========

    Escolha uma das opções do nosso sistema

    [1] - Senha numérica simples
    [2] - Senha alfanumérica complexa
    [3] - Senha Hash

    Informações Importantes:
        * A senha numérica é recomendada para senha de cartão de crédito/débito
        * A senha alfanumérica é recomendada para registro em serviços e criação de contas. Escolha senha com pelo menos 15 caracteres para ter uma senha segura.
        * A Senha Hash fornece a hash de uma senha segura no algoritmo 'sha3_256'

    ==============================================
    """)

option = int(input("Escolhe uma opção do sistema: "))
pass_size = int(input('Número de caracteres: '))
special_char = '!@#$%&*()-=+,.;<>:?Ç~^}_{]['

def number_pass():
    chars = string.digits
    rnd = random.SystemRandom()
    password = ''.join(rnd.choice(chars) for i in range(pass_size))
    print(f'Sua senha segura: {password}')


def alfa_pass():
    chars = string.ascii_letters + string.digits + special_char
    rnd = random.SystemRandom()
    password = ''.join(rnd.choice(chars) for i in range(pass_size))
    print(f'Sua senha segura: {password}')


def hasher():
    chars = string.ascii_letters + string.digits + special_char
    rnd = random.SystemRandom()
    psw = ''.join(rnd.choice(chars) for i in range(20))
    num_hash = hashlib.sha3_256(psw.encode('UTF-8'))
    print(f'Sua hash segura: {num_hash.hexdigest()}')

def main():

    match option:
        case 1:
            number_pass()

        case 2:
            alfa_pass()

        case 3:
            hasher()


if __name__ == '__main__':
    main()

input("\n\nPressione enter para encerrar o programa...")
