#!/bin/sh
name='dynamodb'
[[ $(docker ps -f "name=$name" --format '{{.Names}}') == $name ]] || docker run -d -v "$PWD":/dynamodb_local_db -p 8000:8000 --name dynamodb cnadiminti/dynamodb-local
[[ $(docker ps -f "name=$name" --format '{{.Names}}') == $name ]] || python create_tables.py
sam local start-api



