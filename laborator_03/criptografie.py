from cryptography.fernet import Fernet

message=input("Introdu textul de cripat: ")
key = Fernet.generate_key()
fernet=Fernet(key)
encMessage=fernet.encrypt(message.encode())
print("Textul necriptat este: ", message)
print("Textul criptat este: ", encMessage)
decMessage=fernet.decrypt(encMessage).decode()
print("Textul decriptat este: ", decMessage)
