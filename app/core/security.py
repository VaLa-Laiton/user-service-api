"""
Módulo de Herramientas de Seguridad para el Manejo de Contraseñas.

Ubicación:
    - Este módulo se encuentra en 'app/core/security.py' y proporciona funciones esenciales para el manejo seguro
      de contraseñas en la aplicación User Service API.

Responsabilidades:
    - Hashear contraseñas en texto plano utilizando el algoritmo bcrypt con 14 rounds, garantizando la robustez del hash.
    - Codificar el hash resultante en formato Base64 para facilitar su almacenamiento y transmisión en sistemas que 
      manejan texto.
    - Verificar que una contraseña en texto plano coincide con un hash previamente generado y codificado en Base64.

Estructura:
    - Función `hash_password(password)`:
          • Recibe una contraseña en texto plano.
          • Genera una sal (salt) utilizando bcrypt con 14 rounds.
          • Hashea la contraseña utilizando la sal generada.
          • Codifica el hash resultante en Base64 y lo retorna como cadena.
    - Función `verify_password(password, hashed_base64)`:
          • Recibe una contraseña en texto plano y un hash codificado en Base64.
          • Decodifica el hash de Base64 al formato binario original.
          • Utiliza bcrypt para verificar si la contraseña, al ser hasheada, coincide con el hash decodificado.
          • Retorna True si la verificación es exitosa o False en caso contrario.

Notas:
    - Se ha elegido utilizar 14 rounds en bcrypt para lograr un balance adecuado entre seguridad y rendimiento.
    - La codificación en Base64 facilita el almacenamiento y manejo del hash en sistemas que no soportan datos binarios.
    - El bloque de código comentado al inicio permite probar y ajustar el número de rounds, midiendo el tiempo de procesamiento,
      lo cual puede ser útil durante la fase de optimización.
"""

import bcrypt
import base64

# Código de prueba para evaluar el número óptimo de rounds (comentado).
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
    Hashea una contraseña en texto plano utilizando bcrypt y codifica el resultado en Base64.

    Esta función genera una sal utilizando bcrypt con 14 rounds, lo que proporciona un alto nivel de seguridad
    para el hash generado. La contraseña se codifica en 'utf-8' antes de ser procesada, y el hash resultante se
    codifica en Base64 para facilitar su almacenamiento.

    Args:
        password (str): Contraseña en texto plano.

    Returns:
        str: Contraseña hasheada y codificada en Base64.
    """
    salt = bcrypt.gensalt(rounds=14)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Codificar el hash en Base64 antes de retornarlo
    return base64.b64encode(hashed).decode('utf-8')

def verify_password(password, hashed_base64):
    """
    Verifica que una contraseña en texto plano coincida con un hash previamente generado y codificado en Base64.

    Esta función decodifica el hash codificado en Base64 y utiliza bcrypt para comparar la contraseña en texto plano,
    codificada en 'utf-8', con el hash decodificado. Retorna un valor booleano que indica si la contraseña es válida.

    Args:
        password (str): Contraseña en texto plano.
        hashed_base64 (str): Hash de la contraseña, codificado en Base64.

    Returns:
        bool: True si la contraseña es válida y coincide con el hash, False en caso contrario.
    """
    # Decodificar el hash desde Base64 para obtener el hash original en formato binario
    hashed = base64.b64decode(hashed_base64.encode('utf-8'))
    
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
