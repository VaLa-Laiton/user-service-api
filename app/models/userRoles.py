from enum import Enum

class UserRole(str, Enum):
    """
    Enum que define los roles de usuario disponibles en el sistema.

    Los roles disponibles son:
    - SUPER_ADMIN: Acceso total y administración completa del sistema.
    - ADMIN: Gestión administrativa con amplios permisos.
    - TECHNICAL: Permisos técnicos para la gestión de aspectos operativos.
    - VIEWER: Acceso limitado a la visualización de información.
    """
    SUPER_ADMIN = "superAdmin"
    ADMIN = "admin"
    TECHNICAL = "technical"
    VIEWER = "viewer"
