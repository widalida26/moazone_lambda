import json
import requests
import os
from pydantic import BaseModel 
from connection import connect_engine
from models import Users

engine = connect_engine()
session = engine.sessionmaker()

def handler(event, context):
    body_data = json.loads(event["body"])
    auth_code = body_data["authcode"]

    kakao_auth_url = 'https://kauth.kakao.com/oauth/token'
    auth_data = {
        "grant_type" : "authorization_code",
        "client_id" : os.environ.get('KAKAO_REST_API_KEY'),
        "redirect_uri" : os.environ.get('KAKAO_CALLBACK_URL'),
        "code" : auth_code
    }

    # 인가 코드로 토큰 요청
    response = requests.post(kakao_auth_url, data=auth_data)
    token_data = response.json()
    access_token = token_data['access_token']
    
    # 토큰으로 유저 데이터 요청
    user_profile = requests.get(
                'https://kapi.kakao.com//v2/user/me', 
                headers={'Authorization' : 'Bearer {}'.format(access_token)}
                )
    user_id = user_profile.json()['id']

    # 유저 중복 참여 체크
    existed = session.query(Users).filter(Users.user_id == user_id, Users.consent == 1).all()

    # 새로운 id 삽입
    if len(existed) < 1: 
        newUser = Users(user_id = user_id)
        session.add(newUser)
        session.commit()
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, POST, GET'
            },
            'body': 'success'
        }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, POST, GET'
            },
            'body': 'already existed'
        }

    # # id 예외처리 >>> 나중에 삭제
    # if user_id == 2408139919:
    #     return {'user_id': user_id}

