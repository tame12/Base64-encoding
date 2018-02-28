from base64_encrypter_main import decrypt_from_base64

f_text = open("encrypted_text.txt", 'r') #read the text to be encrypted
text = f_text.read()
f_text.close()

output = decrypt_from_base64(text)

f_output = open("decrypted_text.txt", 'w') #output to txt file
f_output.write(output)
f_output.close()
