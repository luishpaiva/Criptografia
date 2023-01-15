# É necessário instalar o pacote pycryptodome (!pip install pycryptodome)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

bits = 1024

for i in range(1, 5):
    keyPair = RSA.generate(bits)

    inicio = time.time()

    pubKey = keyPair.publickey()
    print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
    pubKeyPEM = pubKey.exportKey()
    print(pubKeyPEM.decode('ascii'))

    print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
    privKeyPEM = keyPair.exportKey()
    print(privKeyPEM.decode('ascii'))

    msg = b'Vamos ajudar o banco de Toquio!!'
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg)
    print("Encrypted:", binascii.hexlify(encrypted))

    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted = decryptor.decrypt(encrypted)
    print('Decrypted:', decrypted)

    fim = time.time()
    benchmark = fim - inicio

    print("Benchmark: ",benchmark)

    bits *= 2
    