import boto3
import json

def lambda_handler(event, context):

    client = boto3.resource('dynamodb')

    table = client.Table("books")
    Items = table.scan()
    print(Items)
    return {
        'statusCode': 200,
        'body': json.dumps(Items)
    }
