import boto3
from datetime import datetime
from app.config import *

ddb=boto3.resource("dynamodb",
    endpoint_url=AWS_ENDPOINT,
    region_name=REGION
)

table=ddb.Table(DDB_TABLE)

def save(user_id,image_id,key,desc,tags):

    table.put_item(Item={
        "pk":f"USER#{user_id}",
        "sk":f"IMAGE#{image_id}",
        "image_id":image_id,
        "s3_key":key,
        "description":desc,
        "tags":tags,
        "created_at":datetime.utcnow().isoformat()
    })


def get(user_id,image_id):
    r=table.get_item(Key={
        "pk":f"USER#{user_id}",
        "sk":f"IMAGE#{image_id}"
    })
    return r.get("Item")


def list(user_id,limit,lek=None):

    args={
        "KeyConditionExpression":"pk=:pk",
        "ExpressionAttributeValues":{":pk":f"USER#{user_id}"},
        "Limit":limit
    }

    if lek:
        args["ExclusiveStartKey"]=lek

    r=table.query(**args)
    return r["Items"], r.get("LastEvaluatedKey")


def delete(user_id,image_id):
    table.delete_item(Key={
        "pk":f"USER#{user_id}",
        "sk":f"IMAGE#{image_id}"
    })
