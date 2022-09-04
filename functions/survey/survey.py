import json
import requests
import os
from datetime import datetime
from pydantic import BaseModel 
from connection import connect_engine
from models import Users
from models import SurveyInfo

engine = connect_engine()
session = engine.sessionmaker()

def dday_calculator(day):
    today = datetime.now().date()
    target_date = datetime.strptime(day, '%Y-%m-%d').date()
    dday = target_date - today
    return dday.days

def handler(event, context):
    # users 동의 여부 업데이트
    # session.query(Users).filter(Users.user_id == user_id).update({ Users.consent: 1 })
    # session.commit()

    # new survey 데이터 삽입
    dt = event["survey_data"]
    survey_info = SurveyInfo(
        gender = dt['gender'][0],
        car = dt['car'][0],
        reality = dt['reality'][0],
        child_num = int(dt['child_num']),
        income_total = int(dt['income_total']),
        income_type = dt['income_type'],
        edu_type = dt['edu_type'],
        family_type = dt['family_type'],
        house_type = dt['house_type'],
        DAYS_BIRTH = dday_calculator(dt['DAYS_BIRTH'][0:10]),
        DAYS_EMPLOYED = dday_calculator(dt['DAYS_EMPLOYED'][0:10]),
        FLAG_MOBIL = 1 if dt['FLAG_MOBIL'] == 'Yes' else 0,
        work_phone = 1 if dt['work_phone'] == 'Yes' else 0,
        phone = 1 if dt['phone'] == 'Yes' else 0,
        email = 1 if dt['email'] == 'Yes' else 0,
        occyp_type = dt['occyp_type'],
        family_size = dt['family_size'],
        begin_month = dday_calculator(dt['begin_month'][0:10]),
    )

    session.add(survey_info)
    session.commit()

    return {
        'statusCode': 201,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, POST'
        },
        'body': json.dumps({ "event" : 'success' })
    }