#!/bin/sh

docker build -t fastapi .

docker run -d --name fastapi -p 80:80 fastapi
