from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import chaves


def criptografar_mensagem(public_key, mensagem):
    try:
        mensagem_bytes = mensagem.encode('utf-8')
        mensagem_criptografada = public_key.encrypt(
            mensagem_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open("mensagem.enc", "wb") as m:
            m.write(mensagem_criptografada)
        return mensagem_criptografada
    except Exception as e:
        print(f'Ocorreu um erro ao criptografar a mensagem. Erro: \n{e}')




