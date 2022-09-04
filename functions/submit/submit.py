import json
import requests
import os
from pydantic import BaseModel 
from connection import connect_engine
# from models import Users

engine = connect_engine()
session = engine.sessionmaker()

def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, GET'
        },
        'body': json.dumps('Hello from Lambda!')
    }