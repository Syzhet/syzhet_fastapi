from datetime import datetime, timedelta

from jose import jwt

from ..config import base_config


SECRET_KEY = base_config.admin.secret_key
ALGORITHM = base_config.admin.algoritm
TOKEN_EXPIRE = base_config.admin.token_expire


def create_access_token(
    data: dict,
):
    """
    Создание токена доступа из юзернейма,
    времени жизни и SECRET_KEY (алгоритм: HS256)
    """

    print('create_access_token: ', data)
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print('encoded_jwt: ', encoded_jwt)
    return encoded_jwt
