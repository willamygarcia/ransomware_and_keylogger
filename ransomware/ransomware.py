import pathlib
import secrets
import os
import base64
import getpass

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

def generate_salt(size=16):
    """
    Gerador do salt com o comprimento da 16 bits
    """
    return secrets.token_bytes(size)

def derive_key(salt, password):
    """
    Derive a chave da `senha` usando o `salt` passado
    """
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def load_salt():
    """
    Leia o salt em um arquivo chamando salt.salt 
    """
    return open("salt.salt", "rb").read()

def generate_key(password, salt_size=16, load_existing_salt=False, save_salt=True):
    """
    Gera uma chave a partir de um `password` e do salt.
    Se `load_existing_salt` for True, carregará o salt de um arquivo
    no diretório atual chamado "salt.salt".
    Se `save_salt` for True, gerará um novo salt
    e o salvará em "salt.salt". 
    """
    if load_existing_salt:
        salt = load_salt()
    elif save_salt:
        salt = generate_salt(salt_size)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    derived_key = derive_key(salt, password)
    return base64.urlsafe_b64encode(derived_key)

def encrypt(filename, key):
    """Dado um nome de arquivo (str) e uma chave (bytes), ele criptografa o arquivo e o grava"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
        
def encrypt_folder(foldername, key):
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Criptografando {child}")
            encrypt(child, key)
        elif child.is_dir():
            encrypt_folder(child, key)

def decrypt(filename, key):
    """Dado um nome de arquivo (str) e uma chave (bytes), ele descriptografa o arquivo e o grava"""
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("[!] Token inválido, provavelmente a senha está incorreta")
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    
def decrypt_folder(foldername, key):
    for child in pathlib.Path(foldername).glob("*"):
        if child.is_file():
            print(f"[*] Decrypting {child}")
            decrypt(child, key)
        elif child.is_dir():
            decrypt_folder(child, key)
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Script de criptografia de arquivos com senha")
    parser.add_argument("path", help="Caminho para criptografar/descriptografar, pode ser um arquivo ou uma pasta inteira")
    parser.add_argument("-s", "--salt-size", help="Se isso for definido, um novo salt com o tamanho passado será gerado", type=int)
    parser.add_argument("-e", "--encrypt", action="store_true", help="Se o arquivo/pasta deve ser criptografado, somente -e ou -d podem ser especificados.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Se o arquivo/pasta deve ser descriptografado, somente -e ou -d podem ser especificados.")
    args = parser.parse_args()
    if args.encrypt:
        password = getpass.getpass("Digite a senha para criptografia:")
    elif args.decrypt:
        password = getpass.getpass("Digite a senha que você usou para criptografia:")
    if args.salt_size:
        key = generate_key(password, salt_size=args.salt_size, save_salt=True)
    else:
        key = generate_key(password, load_existing_salt=True)
    encrypt_ = args.encrypt
    decrypt_ = args.decrypt
    if encrypt_ and decrypt_:
        raise TypeError("Por favor, especifique se você deseja criptografar o arquivo ou descriptografá-lo.")
    elif encrypt_:
        if os.path.isfile(args.path):
            encrypt(args.path, key)
        elif os.path.isdir(args.path):
            encrypt_folder(args.path, key)
    elif decrypt_:
        if os.path.isfile(args.path):
            decrypt(args.path, key)
        elif os.path.isdir(args.path):
            decrypt_folder(args.path, key)
    else:
        raise TypeError("Por favor, especifique se você deseja criptografar o arquivo ou descriptografá-lo.")
