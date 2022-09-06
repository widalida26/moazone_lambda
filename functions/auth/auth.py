import json
from connection import connect_engine
from models import Customers

engine = connect_engine()
session = engine.sessionmaker()

def handler(event, context):
    body_data = json.loads(event["body"])
    user_id = body_data["user_id"]

    existed = session.query(Customers).filter(Customers.user_id == user_id).all()
    consented = session.query(Customers).filter(Customers.user_id == user_id, Customers.consent == 1).all()

    if len(existed) < 1: 
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, POST, GET'
            },
            'body': json.dumps({ "message" : "not targeted" })
        }
    elif len(consented) > 1:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, POST, GET'
            },
            'body': json.dumps({ "message" : "already participated" })
        }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS, POST, GET'
            },
            'body': json.dumps({ "user_id" : user_id })
        }