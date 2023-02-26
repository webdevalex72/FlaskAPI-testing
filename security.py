import hmac
from models.user import UserModel


def authenticate(username: str, password: str) -> UserModel:
    """
    Function that gets called when a user calls the /auth endpoint
    with their username and password.

    Args:
        username: User's username in string format.
        password: User's un-encrypted  password in string format.
    
    Returns:
        User's object or None
    """
    user = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user
    

def identity(playload) -> UserModel:
    """
    Function thzt gets called when user has already authenticated, and
    HMAC (Keyed-Hashing for Message Authentication) Python module verified
    their authorization header is correct.

    Args:
        A dict with 'identity' key, which is the user id.
    
    Returns:
        A UserModel object
    """
    user_id = playload['identity']
    return UserModel.find_by_id(user_id)
