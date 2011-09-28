# Python encryptor/decriptor to match Java JCE AES Encryption Results (ECB mode)

Credits to Thomas Sutton for the [original code](http://passingcuriosity.com/2009/aes-encryption-in-python-with-m2crypto/) working with base64

I have forced the iv to be '\0' * 16 but you can pass another value by
params as shown in the previous link

    # Decode the key and iv
    key = b64decode(key)
    if iv is None:
        iv = '\0' * 16
    else:
        iv = b64decode(iv)

#Usage

    encrypted_message = aes_encryptor(secret_key, msg=plain_text)
    decrypted_message = aes_decryptor(secret_key, msg=encrypted_message)

#Dependencies

- [M2Crypto](http://chandlerproject.org/bin/view/Projects/MeTooCrypto)

Comments, corrections and suggestions are always welcome