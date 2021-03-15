from werkzeug.security import safe_str_cmp  ##Library to compare string instead of using ==
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):  ##Use of "safe string compare"
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)