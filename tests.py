from AES import AES_128, AES_192, AES_256, hexstr, bytelist

if __name__ == "__main__":
    aes = AES_192()
    text = "00112233445566778899aabbccddeeff"
    key = "000102030405060708090a0b0c0d0e0f1011121314151617"

    cipher = aes.encrypt(text, key)
    print(hexstr(cipher))