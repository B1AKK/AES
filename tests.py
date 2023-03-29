from AES import AES_128, AES_192, AES_256, hexstr
from time import time


TESTS = (
    (
        AES_128,
        "32 43 f6 a8 88 5a 30 8d 31 31 98 a2 e0 37 07 34",
        "2b 7e 15 16 28 ae d2 a6 ab f7 15 88 09 cf 4f 3c",
        "39 25 84 1d 02 dc 09 fb dc 11 85 97 19 6a 0b 32"
    ),
    (
        AES_128,
        "00112233445566778899aabbccddeeff",
        "000102030405060708090a0b0c0d0e0f",
        "69c4e0d86a7b0430d8cdb78070b4c55a"
    ),
    (
        AES_192,
        "00112233445566778899aabbccddeeff",
        "000102030405060708090a0b0c0d0e0f1011121314151617",
        "dda97ca4864cdfe06eaf70a0ec0d7191"
    ),
    (
        AES_256,
        "00112233445566778899aabbccddeeff",
        "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f",
        "8ea2b7ca516745bfeafc49904b496089"
    )
)


FILE_TESTS = (
    (AES_128, "02 65 4f a4 78 00 1e ab b8 66 10 22 33 48 1c 2d"),
    (AES_192, "01128d0304a706bdf04090a0ba8dc0e1f1015521339151a7"),
    (AES_256, "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f")
)


if __name__ == "__main__":
    # Testing the algorithm on the example data from the AES standard
    for crypto_cls, plaintext, key, cipher in TESTS:
        aes = crypto_cls()
        if hexstr(aes.encrypt(plaintext, key)).replace(" ", "") != cipher.replace(" ", ""):
            print(f"Plaintext: {plaintext}\nExpected cipher: {cipher}\nObtained cipher: {aes.encrypt(plaintext, key)}")
        else:
            print("Success encryption")
        if hexstr(aes.decrypt(cipher, key)).replace(" ", "") != plaintext.replace(" ", ""):
            print(f"Cipher: {cipher}\nExpected plaintext: {plaintext}\nObtained plaintext: {aes.decrypt(cipher, key)}")
        else:
            print("Success decryption")

    # Testing the algorithm on a file
    with open("plaintext.txt", "rb") as f:
        plaintext = list(f.read())

    print(f"\nSize of plaintext: {len(plaintext)} bytes")
    for crypto_cls, key in FILE_TESTS:
        aes = crypto_cls()

        print(f"\nStarting encryption with {crypto_cls.__name__}")
        t = time()
        cipher = aes.encrypt(plaintext, key)
        print(f"{time() - t} seconds spent")
        print("Starting decryption")
        t = time()
        decrypted = aes.decrypt(cipher, key)
        print(f"{time() - t} seconds spent")

        while not decrypted[-1]:
            decrypted.pop()

        if plaintext == decrypted:
            print("Success!")
        else:
            print("Error: decrypted text does not equal to the plaintext")
        with open(f"{crypto_cls.__name__}_encrypted.txt", "w") as f:
            f.write(hexstr(cipher))
