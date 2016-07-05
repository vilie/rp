#!/bin/bash
docker build -t "hs:mongo" .
docker run -d -p 27017:27017 hs:mongo
