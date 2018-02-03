# qvolver-db
DB Definitions for Qvolver

## Requirements
- AWS CLI: https://aws.amazon.com/cli/
- Local DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html

The `run-dynamodb-local.sh` expects the dynamoDB jar to be in a directory labelled dynamo-db, in the same parent directory as this project. A good PR for the future would be to break this into a system variable.

The run script initializes dynamoDB in in-memory mode, which means all work will be cleared upon terminating it. 