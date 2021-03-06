import jwt
from flask import request, jsonify
from functools import wraps

from my_settings import SERCRET, HASH_ALGORITHM


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """로그인 데코레이터

            Args:+
                func: 로그인 토큰 검증이 필요한 함

            Returns:
                user_id : 로그인 시도 유저 pk
                role_id : 로그인 시도 유저의 권한


            Exceptions:수
                DecodeError: jwt형식이 유효하지 않을때 발생
                ExpiredSignatureError: jwt의 유효시간이 만료되었을 때 발생
                DataError: 컬럼 타입과 매칭되지 않는 값이 DB에 전달되었을 때 발생
                KeyError: 엔드포인트에서 요구하는 키값이 전달되지 않았을 때 발생
            """
        try:
            token = request.headers['Authorization']
            decoded_token = jwt.decode(token, SERCRET, HASH_ALGORITHM)

            return func(*args, **kwargs, **decoded_token)

        except jwt.exceptions.DecodeError:
            return jsonify(message="TOKEN_NOT_RIGHT"), 400
        except jwt.ExpiredSignatureError:
            return jsonify(message="TOKEN_EXPIRED"), 403
        except KeyError:
            return jsonify(message="TOKEN_DOES_NOT_EXIST"), 400
        except Exception as e:
            return jsonify(message=f"{e}"), 500

    return wrapper
