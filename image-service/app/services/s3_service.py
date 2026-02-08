import boto3, uuid
from app.config import *

s3=boto3.client("s3",
    endpoint_url=AWS_ENDPOINT,
    region_name=REGION
)

def upload_image(data, filename):
    image_id=str(uuid.uuid4())
    key=f"{image_id}/{filename}"

    s3.put_object(Bucket=S3_BUCKET,Key=key,Body=data)
    return image_id,key


def generate_download_url(key):
    return s3.generate_presigned_url(
        "get_object",
        Params={"Bucket":S3_BUCKET,"Key":key},
        ExpiresIn=300
    )


def delete_image(key):
    s3.delete_object(Bucket=S3_BUCKET,Key=key)
