import bcrypt
import base64

# """Tester para elegir el numero de rounds"""
#
# import time
# passwd = b's$cret12'
# for i in range(4,17):
#     print(f'Rounds:{i}')
#     start = time.time()
#     salt = bcrypt.gensalt(rounds=i)
#     hashed = bcrypt.hashpw(passwd, salt)
#     end = time.time()
#     print(f'Rounds:{i} | Time: {end - start:.4f} s')

def hash_password(password):
    """
    Hashea una contraseña usando bcrypt con 14 rounds y la codifica en Base64.

    Args:
        password (str): Contraseña en texto plano.

    Returns:
        str: Contraseña hasheada y codificada en Base64.
    """
    salt = bcrypt.gensalt(rounds=14)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Codificar en Base64 antes de retornarlo
    return base64.b64encode(hashed).decode('utf-8')

def verify_password(password, hashed_base64):
    """
    Verifica que una contraseña en texto plano coincida con un hash codificado en Base64.

    Args:
        password (str): Contraseña en texto plano.
        hashed_base64 (str): Contraseña hasheada y codificada en Base64.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
    """
    # Decodificar de Base64 antes de verificar
    hashed = base64.b64decode(hashed_base64.encode('utf-8'))
    
    return bcrypt.checkpw(password.encode('utf-8'), hashed)