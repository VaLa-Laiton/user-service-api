from enum import Enum

class UserRole(str, Enum):
    SUPER_ADMIN = "superAdmin"
    ADMIN = "admin"
    USER = "user"
    VIEWER = "viewer"
