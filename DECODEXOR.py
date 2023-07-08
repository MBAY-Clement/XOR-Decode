encrypted_message = b'\r\x07\x1c-\nN\x19\x04\x0fE0"\x02\x1f7\x00#\x01\x03N\x13\x0e\x1c\x01'
xor_key = 'YouCanNeverCatchJohnDoe!'

decrypted_message = bytearray()
key_length = len(xor_key)

for i, byte in enumerate(encrypted_message):
    decrypted_byte = byte ^ ord(xor_key[i % key_length])
    decrypted_message.append(decrypted_byte)

print(decrypted_message)
