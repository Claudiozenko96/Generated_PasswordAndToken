import secrets
import string
import hashlib

#funcion para generar un valor aleatorio
def generate_random_value():
    length = int(input("Enter password length Between 5 and 30: "))
    if length > 5 and length <= 30: 
        characters = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
        return ''.join(secrets.choice(characters) for _ in range(length))
    else:
        print("Enter value error")

#funcion para selecionar el tipo de hash
def select_hash(encode):
    enter = int(input("Select hashes: 1- SHA256  2- SHA512  3- MD5: "))
    if enter == 1:
        hashed256 = hashlib.sha256(encode).hexdigest()
        return hashed256
    elif enter == 2:
        hashed512 = hashlib.sha512(encode).hexdigest()
        return hashed512
    elif enter == 3:
        hashedMD5 = hashlib.md5(encode).hexdigest()
        return hashedMD5
    else:
        print("you did not enter any hash")

#funcion para encriptar 
def encrypt_value(random_string):
    #codificar la cadena como byte antes de hashearlo
    try:
        encoded = random_string.encode('utf-8')
        hashed = select_hash(encoded)
        return hashed #devuelve el valor hasheado con sha256
    
    except Exception as e:
        print("Error encrypting value", e)    
        return None


def main():
    print("\n")
    print("\t\t<<<<<<<<<< PYTHON CODE TO ENCRYPT >>>>>>>>>>")
    print("")
    string_random = generate_random_value()

   #llamamos a la funcion y le pasamos el parametro aleatorio para encriptarlo 
    encrypt_final_string = encrypt_value(string_random)
    if encrypt_final_string :
        print("-----------------------------------------------------------------------------------------")
        print(f"Value Random: {string_random}")
        print("-----------------------------------------------------------------------------------------")
        print(f"the encrypted value is: {encrypt_final_string}")
        print("-----------------------------------------------------------------------------------------")
        print(" ")
    else:
        print("error encrypting")


if __name__ == '__main__':
    main()
