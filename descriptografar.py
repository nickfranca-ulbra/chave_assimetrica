from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



def descriptografar_mensagem(private_key, mensagem_criptografada):
    try:
        mensagem_descriptografada = private_key.decrypt(
            mensagem_criptografada,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return mensagem_descriptografada.decode('utf-8')
    except Exception as e:
        print(f'A mensaem criptografada não é compativel com as chaves geradas. Cuidado!')







