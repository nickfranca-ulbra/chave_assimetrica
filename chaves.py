from cryptography.hazmat.primitives import serialization

def chave_privada():
    try:
        with open("chave_privada.pem", "rb") as c:
            private_key = serialization.load_pem_private_key(
                c.read(),
                password=None
            )
        return private_key
    except Exception as e:
        print(f'Ocorreu um erro ao acessar a chave privada. Erro:\n {e}')

def chave_publica():
    try:
        with open("chave_publica.pem", "rb") as c:
            public_key = serialization.load_pem_public_key(
                c.read()
            )
        return public_key
    except Exception as e:
        print(f'Ocorreu um erro ao acessar a chave publica. Erro: \n{e}')