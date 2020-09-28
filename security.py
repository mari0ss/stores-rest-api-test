from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    """
    Function that gets called when a user calls th /auth endpoint
    with their username and password
    :param username: username
    :param password: password
    :return: A UserModel object if authentication succeeds, None otherwise.
    """

    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    """
    This func will run If user is authenticated , and flask -JWT verified their authorization header is correct
    :param payload: payload : A dictionary with 'identity' key , which is the user id.
    :return: A UserModel object
    """

    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
