import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('rr42-cloud-resume')

def lambda_handler(event, context):
    response = table.get_item(
        Key = {
            'id':'0'
        }
    )
    
    visit_count = response['Item']['views'] 
    visit_count = str(int(visit_count) + 1)
    
    response = table.put_item(
        Item = {
            'id':'0',
            'views': visit_count
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        'body': json.dumps({'visit_count': visit_count})
    }