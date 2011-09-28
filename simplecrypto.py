# encoding: utf-8

import M2Crypto

ENC = 1
DEC = 0


def aes_build_cipher(key, iv, op=ENC):
    """"""""
    return M2Crypto.EVP.Cipher(alg='aes_128_ecb', key=key, iv=iv, op=op)


def aes_encryptor(key, data):
    """
    AES 128 ECB Encryptor
    """
    iv = '\0' * 16
    cipher = aes_build_cipher(key.decode("hex"), iv, ENC)
    v = cipher.update(data)
    v = v + cipher.final()
    del cipher
    v = v.encode("hex")

    return v


def aes_decryptor(key, data):
    """
    AES 128 ECB Decryptor
    """
    iv = '\0' * 16
    data = data.decode("hex")
    cipher = aes_build_cipher(key.decode("hex"), iv, DEC)
    v = cipher.update(data)
    v = v + cipher.final()
    del cipher

    return v
