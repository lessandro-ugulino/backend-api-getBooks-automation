import boto3
import json
import uuid

def lambda_handler(event, context):

    client = boto3.resource('dynamodb')

    table = client.Table("books")

    item = {}
    title = json.loads(event['body'])
    title_name = title['title']

    item['id'] = uuid.uuid4().hex
    item['title'] = title_name

    print(item)

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }