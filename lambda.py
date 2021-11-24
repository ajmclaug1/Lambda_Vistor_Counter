import boto3
import json

#from datetime import datetime

def lambda_handler(event, context):
    #date1 = datetime.now().strftime('%d/%m/%Y')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Vistor_Counter')
    #Get No
    dytable = table.get_item(
    Key={
        'Date_Visted': 'Total'
        }
    )
    Vistors = dytable['Item']
    Vistors = Vistors.get('No_of_Vistors')
    #Increment
    Vistors += 1
    #Update Table
    table.update_item(
    Key={
            'Date_Visted': 'Total'
        },
        UpdateExpression='SET No_of_Vistors = :val1',
        ExpressionAttributeValues={
            ':val1': Vistors
        }
    )
    response = int(Vistors)
    return response 
