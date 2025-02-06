from app.utils.validations import (
    username_validator,
    password_validator,
    full_name_validator,
    email_validator,
    phone_number_validator,
    avatar_validator
)

def isValid_user_data(user_data: dict) -> dict:
    """
    Valida los datos de un usuario según el esquema proporcionado.

    Para cada campo presente en el diccionario `user_data`, se invoca el validador correspondiente.
    Los validadores retornan un diccionario con el estado de validación (por ejemplo, 'isValid').

    Args:
        user_data (dict): Diccionario con los datos del usuario a validar.

    Returns:
        dict: Diccionario donde cada clave es un campo y el valor es el resultado de su validación.
    """
    validations = {}

    # Validar username si está presente en el schema
    if "username" in user_data:
        validations["username"] = username_validator.isValid_username(user_data["username"])

    # Validar password si está presente en el schema
    if "password" in user_data:
        validations["password"] = password_validator.isValid_password(user_data["password"])

    # Validar full name si está presente en el schema
    if "full_name" in user_data:
        validations["full_name"] = full_name_validator.isValid_full_name(user_data["full_name"])

    # Validar email si está presente en el schema
    if "email" in user_data:
        validations["email"] = email_validator.isValid_email(user_data["email"])

    # Validar phone number si está presente en el schema
    if "phone_number" in user_data:
        validations["phone_number"] = phone_number_validator.isValid_phone_number(user_data["phone_number"])

    # Validar avatar_url si está presente en el schema
    if "avatar_url" in user_data:
        validations["avatar_url"] = avatar_validator.isValid_avatar_url(user_data["avatar_url"])

    # Imprimir en consola el resultado de las validaciones para depuración.
    print("Resultado de validaciones:", validations)
    
    return validations
