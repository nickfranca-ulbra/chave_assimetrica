import gerarChaves
import criptografar
import descriptografar
import chaves
import os
import getpass

while True:
    
    menu = input("--------------------------\nOlá. Insira uma opção para continuar:\n1 - Gerar novas chaves\n2 - Encriptar uma mensagem digitada pelo usuário\n3 - Decriptar a mensagem\n0 - Sair\n--> ")  
    if menu=='1':
        gerarChaves.gerar()
        print("Suas chaves foram geradas nos arquivos 'chave_privada.pem' e 'chave_publica.pem'")
        
    elif menu =='2':
        mensagem_secreta = getpass.getpass("Insira a mensagem que será criptografada:")
        if os.path.exists("chave_publica.pem"):
            public_key = chaves.chave_publica()
            mensagem_cifrada = criptografar.criptografar_mensagem(public_key, mensagem_secreta)

            print("Sua mensagem foi criptografada com sucesso e está no arquivo 'mensagem.enc'")
        else:
            print("Não há chave para ser criptografar a mensagem. Gere as chaves primeiro.")
    elif menu=='3':
        if os.path.exists("mensagem.enc"):
            with open("mensagem.enc", "rb") as m:
                mensagem_criptografada = m.read()
            private_key = chaves.chave_privada()
            print(private_key)
            mensagem_revelada = descriptografar.descriptografar_mensagem(private_key, mensagem_criptografada)

            print("\nMensagem Descriptografada:")
            print(mensagem_revelada)
        else:
            print("Não há mensagem para ser descriptografada. Faça a encriptação primeiro.")
    elif menu=='0':
        break
    else:
        print('Insira um comando válido!')