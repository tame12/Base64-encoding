from base64_encrypter_main import encrypt_to_base64

f_text = open("text_to_be_encrypted.txt", 'r') #read the text to be encrypted
text = f_text.read()
f_text.close()

output = encrypt_to_base64(text)

f_output = open("encrypted_text.txt", 'w') #output to txt file
f_output.write(output)
f_output.close()
