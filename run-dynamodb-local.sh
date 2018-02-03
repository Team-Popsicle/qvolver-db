#!/bin/sh

java -Djava.library.path=./DynamoDBLocal_lib -jar ../dynamo-db/DynamoDBLocal.jar -sharedDb -inMemory