#!/bin/bash
docker build -t "hs:webserver" .
docker run -p 5000:5000 hs:webserver --link mongo
