aws --endpoint-url=http://localhost:4566 s3 mb s3://images
aws --endpoint-url=http://localhost:4566 s3 ls

aws --endpoint-url=http://localhost:4566 dynamodb create-table --table-name image-meta --attribute-definitions AttributeName=pk,AttributeType=S AttributeName=sk,AttributeType=S --key-schema AttributeName=pk,KeyType=HASH AttributeName=sk,KeyType=RANGE --billing-mode PAY_PER_REQUEST

aws --endpoint-url=http://localhost:4566 dynamodb list-tables
